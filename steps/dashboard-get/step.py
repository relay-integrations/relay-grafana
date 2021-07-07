#!/usr/bin/env python
import requests
import os
import time
from urllib.parse import urljoin
from relay_sdk import Interface, Dynamic as D

relay = Interface()

apiURL = relay.get(D.connection.apiURL)
apiKey = relay.get(D.connection.apiKey)

uid = relay.get(D.uid)

r = requests.get(
    urljoin(apiURL, f'/api/dashboards/uid/{uid}'),
    headers={'Authorization': 'Bearer ' + apiKey},
)

print('Emitted event to Grafana API, got response: ', r.text)

relay.outputs.set('response', r.json())

r.raise_for_status()
