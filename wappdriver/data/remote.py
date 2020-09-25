'''This module remote.py provides access to remote. It fetches latest data from the internet'''

from .data_error import handle_connection, handle_dependancy


@handle_dependancy
def rqst():
    import requests
    return requests


prefix = 'https://raw.githubusercontent.com/aahnik/wappdriver/main/.github/'

version_url = f'{prefix}ver'
var_url = f'{prefix}var'


@handle_connection
def version():
    '''
    Returns remote version
    '''
    ver = float(rqst().get(url=version_url).text)
    return ver


@handle_connection
def fetch_vars():
    '''
    Returns the content of remote vars as a string
    '''
    dynamic_vars = rqst().get(url=var_url).text
    return dynamic_vars


