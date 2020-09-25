'''
This module contains the context manager for creating a bot ie an instance of WappDriver Class
'''

from .driver import WappDriver
import os
from tqdm import tqdm
import time


def category(arg):
    '''
    Returns a string (or None if invalid)

    - `text`   for plain text or url
    - `media`  for path of image or video file path
    - `file`   for path of any other file type 

    '''

    if os.path.isfile(arg):
        if os.stat(arg).st_size <= 1.6e+7:
            file_type = os.path.splitext(arg)[1]
            if file_type in ['.png', '.jpg', '.jpeg', '.gif', '.mp4']:
                return 'media'
            else:
                return 'file'
        else:
            print('Files of more than 16 MB are not allowed in WhatsApp')
            quit()
    
    return 'text'


class WhatsApp():

    def __init__(self, timeout=50, session='default'):
        self.timeout = timeout
        self.session = session

    def __enter__(self):
        with tqdm(total=10) as progress:
            self.wappdriver = WappDriver(self.timeout)
            progress.update(3)
            if self.wappdriver.load_chrome_driver(self.session):
                progress.update(3)
                if self.wappdriver.load_main_screen():
                    progress.update(4)
                    return self
        self.wappdriver.driver.close()

    def send(self, to, *args):
        if self.wappdriver.load_person(to):
            with tqdm(total=len(args)) as progress:
                for arg in args:
                    if category(arg) == 'text':
                        self.wappdriver.send_text(arg)
                    else:
                        self.wappdriver.send_file(arg, category(arg))
                        size_mb = os.stat.st_size(arg)*1e-6
                        time.sleep((self.timeout/10)*size_mb)
                    progress.update(1)

    def __exit__(self, exception_type, exception_value, traceback):
        time.sleep(30)
        print('Closing WhatsApp')
        self.wappdriver.driver.close()
