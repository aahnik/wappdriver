'''This module local.py provides access to local data. It can read and write local data'''
import os
from datetime import datetime
from .. import __version__


dir = os.path.expanduser('~/.wappdriver')
log_file = os.path.join(dir, 'log_file.txt')


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
