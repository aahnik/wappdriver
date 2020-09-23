'''This module local.py provides access to local data. It can read and write local data'''
import os
from datetime import datetime
from .. import __version__


dir = os.path.expanduser('~/.wappdriver')
log_file = os.path.join(dir, 'log_file.txt')
cdp_file = os.path.join(dir, 'cdp.txt')

if not os.path.exists(dir):
    os.mkdir(dir)

if not os.path.exists(log_file):
    with open(log_file, 'w+') as f:
        f.write(f'''
        --------------------------
        Log File Created
        {datetime.now()}
        wappdriver : {__version__}
        ---------------------------\n
        ''')


def set_chrome_driver_path(path=None):
    '''
    Writes the absolute path of installation of Chrome Driver Executable
    in `chrome_driver_path.txt` file in `.wappdriver` directory 
    which exists at the home directory of the user
    ---

    - if the argument `path` is provided, sets the value to path
    - otherwise prompts for user input
    ---

    Validation of `path` and whether correct version is installed or not 
    are done by `test_browser` module of the `tests` package
    '''
    if not path:
        while path != '':
            path = input('''
            -------------------------------------------------------------
            Paste the absolute path of the installation of Chrome Driver
            You have to enter this only once
            -------------------------------------------------------------
            ''').strip()

    with open(cdp_file, 'w+') as f:
        f.write(path)


def get_chrome_driver_path():
    '''Returns the chrome driver path
    first line from `chrome_driver_path.txt` file in `.wappdriver` directory 
    which exists at the home directory of the user.
    ---
    If error arises, calls `set_chrome_driver_path()`
    '''
    try:
        with open(cdp_file,'r') as f:
            

