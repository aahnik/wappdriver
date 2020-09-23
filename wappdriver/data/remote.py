'''This module remote.py provides access to remote. It fetches latest data from the internet'''

import requests

prefix = 'https://raw.githubusercontent.com/aahnik/wappdriver/main/.github/'

version_url = f'{prefix}ver'
var_url = f'{prefix}var'


def version():
    '''
    Returns remote version
    '''
    return float(requests.get(url=version_url).text)


def fetch_vars():
    '''
    Returns the content of remote vars as a string
    '''
    return requests.get(url=var_url).text
