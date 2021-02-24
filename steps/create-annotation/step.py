#!/usr/bin/env python
# posts an event to datadog from relay

import requests, os, time
from relay_sdk import Interface, Dynamic as D

relay = Interface()

apiURL = relay.get(D.connection.apiURL)
apiKey = relay.get(D.connection.apiKey)

payload = {
  'text': relay.get(D.text),
  'time': round(time.time() * 1000)
}

# these should default to a false-y 0 if not overridden by user
if relay.get(D.dashboardID):
  payload['dashboardID'] = int(relay.get(D.dashboardID))

if relay.get(D.panelID):
  payload['panelID'] = int(relay.get(D.panelID))

try:
  labels = relay.get(D.labels)
  payload['labels'] = labels
except requests.exceptions.HTTPError:
  pass

print("Posting payload: ", payload)

r = requests.post(
  apiURL + '/annotations',
  headers={'Authorization': 'Bearer ' + apiKey},
  json=payload
)

print('Emitted event to Grafana API, got response: ', r.text)

relay.outputs.set(name="resultText", value=r.text)
relay.outputs.set(name="resultCode", value=r.status_code)

r.raise_for_status()