'''This module remote.py provides access to remote. It fetches latest data from the internet'''

import requests

prefix = 'd9fb98d88f620d0320bf305ada414299/raw/616fadf34d3a46ae6e02b63580e0d318d0a4a0cf'

URL = f'https://gist.githubusercontent.com/aahnik/{prefix}/'

version_url = f'{URL}wapp-driver-var-ver'
var_url = f'{URL}wapp-driver-var.yml'

def get_remote_version():
    return float(requests.get(url=version_url).text)


