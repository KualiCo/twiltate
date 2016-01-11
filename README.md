# Twiltate, unified ops/support phone numbers
Twiltate uses Twilio as a frontend for all on-call members on your team. You give out one phone number, and it always rings to whoever is on call.

## Getting Started
Clone the repo, and run 
```pip install -r requirements.txt
cp keys.json.example keys.json
```
Edit keys.json with relevant data, and just run twiltate.py

## Notes
Currently supports python 2.7 and VictorOps, although this can be made to reference any scheduler.
The data simply needs to be a dictionary in {"team name":"818-555-1212"} format.

Pull requests/issues welcome!