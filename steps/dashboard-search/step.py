#!/usr/bin/env python

import requests
import os
import time
from relay_sdk import Interface, Dynamic as D

relay = Interface()

apiURL = relay.get(D.connection.apiURL)
apiKey = relay.get(D.connection.apiKey)

params = {
    'type': 'dash-db'
}

try:
    tags = relay.get(D.tags)
    params['tag'] = tags
except requests.exceptions.HTTPError:
    pass

print("Query params: ", params)

r = requests.get(
    apiURL + '/search',
    headers={'Authorization': 'Bearer ' + apiKey},
    params=params
)

print('Emitted event to Grafana API, got response: ', r.text)

relay.outputs.set('response', r.json())

r.raise_for_status()
