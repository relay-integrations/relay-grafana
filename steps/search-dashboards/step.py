#!/usr/bin/env python

import requests
import os
import time
from relay_sdk import Interface, Dynamic as D

relay = Interface()

apiURL = relay.get(D.connection.apiURL)
apiKey = relay.get(D.connection.apiKey)

params = {
    'type': 'dash_db'
}

try:
    tag = relay.get(D.tag)
    params['tag'] = tag
except requests.exceptions.HTTPError:
    pass

print("Query params: ", params)

r = requests.get(
    apiURL + '/search',
    headers={'Authorization': 'Bearer ' + apiKey},
    params=params
)

print('Emitted event to Grafana API, got response: ', r.text)

r.raise_for_status()
