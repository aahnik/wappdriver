'''
local
'''

from wappdriver.error import handle_errors
import requests
import yaml
import os
import logging
from . import __version__
from verlat import latest



wapp_dir = os.path.expanduser('~/wappdriver.data')
cdp_file = os.path.join(wapp_dir, 'cdp.txt')
selectors_file = os.path.join(wapp_dir, 'selectors.yml')
sessions_dir = os.path.join(wapp_dir, 'sessions')


proj = latest('wappdriver')
latver = proj['version']
if latver != __version__:
    logging.critical(f'''You are using an unsupported version. \n\n
    Please use latest stable version.
    To upgrade wappdriver please run \n
        pip install wappdriver=={latver}
        
    Read the documentation to be aware of any changes.
    https://aahnik.github.io/wappdriver/changelog''')
    quit()


def ensure():
    '''
    Executed whenever local is imported, please run `ensure()` to ensure the required local files exists.
    If those files do not exist, ensures the creation of them with proper initial values.
    '''
    logging.info('setting up local')

    if not os.path.exists(wapp_dir):
        os.mkdir(wapp_dir)
        logging.info(f'{wapp_dir} created')

    if not os.path.exists(cdp_file):
        set_chrome_driver_path()

    if not os.path.exists(selectors_file):
        update_selectors()

    if not os.path.exists(sessions_dir):
        os.mkdir(sessions_dir)


@handle_errors('could not set chrome driver path', '', ensure)
def set_chrome_driver_path(path=''):
    '''
    Sets the chrome driver path

    '''

    while path == '':
        path = input('''
        -------------------------------------------------------------
        Paste the absolute path of the installation of Chrome Driver
        You have to enter this only once
        -------------------------------------------------------------
        ''').strip()

    with open(cdp_file, 'w+') as f:
        f.write(path)


def chrome_driver_path():
    '''
    Returns the chrome driver path
    '''
    with open(cdp_file, 'r') as f:
        return f.readline().strip()


@handle_errors('Could not get chrome driver path', '', ensure)
def write_selectors(in_vars):
    '''
    Takes a string and writes that into `selectors.yml` in wappdriver data directory
    '''
    with open(selectors_file, 'w+') as f:
        f.write(in_vars)


def get_selectors():
    ''' 
    Returns the dictionary of selectors loaded from selectors.yml
    '''

    with open(selectors_file, 'r') as f:
        return yaml.full_load(f)


def fetch_selectors():
    '''
    Returns the content of remote selector file as a string
    '''
    prefix = 'https://raw.githubusercontent.com/aahnik/wappdriver/main/wappdriver/'
    selector_file_url = f'{prefix}selectors.yml'
    selectors = requests.get(url=selector_file_url).text
    return selectors


@handle_errors('Could not write selectors to local file', '', ensure)
def update_selectors():
    ''' Overwrites the local `selectors.yml` file with the value fetched from remote
    Usually takes a few seconds to run, calling this function 
    at the beginning of your script ensures that the values of xpath and css selectors used 
    for automation are up to date with the latest version of WhatsApp Web.

    Returns True on success
    If failed
    - returns False
    - raises and catches WappDriver Error, and prints it. 

    '''

    logging.info('fetching data')
    write_selectors(fetch_selectors())
