#!/usr/bin/env python

from providers.victorOps import schedule
from twilio.rest import TwilioRestClient
import json


class UpdateTwilio(object):
    def __init__(self, key, token):
        self.key = key
        self.token = token
        self.client = TwilioRestClient(key, token)
        self.numbers = self.client.phone_numbers.list()
        self.voice_urls = "http://twimlets.com/forward?PhoneNumber={on_call}&CallerId={caller_id}&"

    def update_numbers(self, team_numbers):
        for number in self.numbers:
            try:
                name = number.friendly_name.lower()
                callerid = number.phone_number[2:]
                oncall = team_numbers[name]
                url = self.voice_urls.format(on_call=oncall, caller_id=callerid)
                if not number.voice_url == url:
                    ok = number.update(voice_url=url)
                    if text_confirmation:
                        self.client.messages.create(body="Urgent calls for your team are now routed to you", to=oncall, from_=callerid)
                    print("Updated", oncall, name)
            except KeyError:
                print("OPS group ", name, " has no scheduled phone number to reference")

# Get keys for twilio
with open('keys.json') as f:
    credentials = json.load(f)

tw_keys = credentials['twilio']
text_confirmation = False  # this will text the person who is now on call after the change is made.
vo_keys = credentials['victorops']

# Fire!
vo_schedule = schedule(vo_keys['vo_user'], vo_keys['vo_pass'], vo_keys['vo_org'])
s = UpdateTwilio(tw_keys['TWILIO_ACCOUNT_SID'], tw_keys['TWILIO_AUTH_TOKEN'])
s.update_numbers(team_numbers=vo_schedule)
