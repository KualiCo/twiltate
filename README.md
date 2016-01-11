# Twiltate
## unified ops/support phone numbers
Twiltate uses Twilio as a frontend for all on-call members on your team. You give out one phone number, and it always rings to whoever is on call. For information on costs associated with this method see [here](https://www.twilio.com/help/faq/voice/how-much-am-i-charged-for-call-forwarding)

## Getting Started
In Twilio, create/update your phone numbers common name to match the corresponding team name. If no match is found, no numbers will be updated.
Clone the repo, and run 
```pip install -r requirements.txt;
cp keys.json.example keys.json```
Edit keys.json with relevant data, and just run twiltate.py! (better still, put it in a cron job)

## Features
 * Number rotation
 * Text message confirmation

## Notes
Currently supports python 2.7 and VictorOps, although this can be made to reference any scheduler.
The data simply needs to be a dictionary in {"team name":"818-555-1212"} format.

Pull/feature requests/issues welcome!
