#!/usr/bin/env python

import requests
import os
import time
from relay_sdk import Interface, Dynamic as D

relay = Interface()

apiURL = relay.get(D.connection.apiURL)
apiKey = relay.get(D.connection.apiKey)

timeStart = round(time.time() * 1000)
try:
    timeStart = int(relay.get(D.time.start))
except requests.exceptions.HTTPError:
    pass

timeEnd = timeStart
try:
    timeEnd = int(relay.get(D.time.end))
except requests.exceptions.HTTPError:
    pass

if timeEnd < timeStart:
    timeEnd = timeStart

payload = {
    'text': relay.get(D.text),
    'time': timeStart,
    'timeEnd': timeEnd,
}

try:
    dashboardId = int(relay.get(D.dashboardId))
    payload['dashboardId'] = dashboardId
except requests.exceptions.HTTPError:
    pass

try:
    panelId = int(relay.get(D.panelId))
    payload["panelId"] = panelId
except requests.exceptions.HTTPError:
    pass

try:
    tags = relay.get(D.tags)
    payload['tags'] = tags
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
