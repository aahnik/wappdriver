'''This module remote.py provides access to remote. It fetches latest data from the internet'''

from .data_error import handle_connection, handle_dependancy


@handle_dependancy
def rqst():
    import requests
    return requests


prefix = 'https://raw.githubusercontent.com/aahnik/wappdriver/main/wappdriver/'

var_url = f'{prefix}selectors.yml'




@handle_connection
def fetch_selectors():
    '''
    Returns the content of remote vars as a string
    '''
    dynamic_vars = rqst().get(url=var_url).text
    return dynamic_vars


