import requests
import json
import re


"""
Compiles a list of teams and forwarding phone numbers into a dictionary.
VO's public api doesn't provide all the endpoints required for this to work yet,
so instead of using an API key, we're doing traditional user/pass.
"""


class VictorOpsApi(object):
    def __init__(self, vo_user, vo_pass, vo_org):
        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/json'
        self.session.auth = (vo_user, vo_pass)
        self.org = vo_org
        self.oncalllist = {}
        self.contact_info = {}
        self.decoder = json.JSONDecoder()

    def get_teams(self):
        teams = self.session.get(url="https://portal.victorops.com/api/v1/org/{org}/teams".format(org=self.org))
        teamdict = self.decoder.decode(teams.text)
        oncalllist = {}
        for team in teamdict:
            oncall = [x.get('oncall') for x in team['oncall'] if x.get('oncall') is not None]
            name = team['slug']
            oncalllist[name] = oncall

        self.oncalllist = oncalllist

    def get_contact_info(self):
        self.get_teams()
        for key, value in self.oncalllist.items():
            user = value[0]
            methods = self.session.get(
                url="https://portal.victorops.com/api/v1/org/kualico/profile/{user}/methods".format(user=user))
            methods_dict = self.decoder.decode(methods.text)
            for method in methods_dict:
                phone_pattern = re.compile(r"^[\s0-9+-]+$")
                if phone_pattern.match(method['value']):
                    self.contact_info[key] = method['value'][3:]


def schedule(vo_user, vo_pass, vo_org):
    print("Getting VictorOps Data")
    print("Please stand by, this might take up to a minute")
    vo = VictorOpsApi(vo_user, vo_pass, vo_org)
    vo.get_contact_info()
    return vo.contact_info
