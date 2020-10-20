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
    '''
    Wappdriver is a python package that helps you automate sending messages through WhatsApp Web. It's very simple to use. 

    You are advised to use the context manager.

    Example:
    ```python
    with WhatsApp() as bot:
        bot.send('aahnik',  # name of recipient
            'hi send by a bot',  # message
                )
    ```

    Visit https://aahnik.github.io/wappdriver for more details

    '''

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
        quit()

    def send(self, to, *args):
        r'''
        Pass name of recipient as first argument and after that you can pass as many message arguments as you wish. 

        - The name of recipient must be saved in your contacts.
        - Each message argument must be a string. 
        - If you want to send a file, pass the absolute path of the file to the function.

        ---

        Example Use:

        ```python
        with WhatsApp() as bot:
            bot.send('aahnik',  # name of recipient

            'hi send by a bot',  # message

            # absolute path of an image on computer
            '/home/aahnik/image.png',  

            # absolute path of a video on computer
            '/home/aahnik/video.mp4',  

            # absolute path of pdf on computer
            '/home/aahnik/django.pdf'  )

        ```

        Note: 

        - In Windows absolute paths looks like: 
            `C:\Users\mathew\img.png`

        - While in Linux or Mac they look like:
            `/home/aahnik/img.png`

        The first argument you need to pass is the recipient's name which must be saved in your phone.

        After that you can pass as many string arguments you want for message. 
        The string can be:
        - a text message or 
        - the file path if you want to send a image, video, GIF, documents etc.
        - you can send multiple files, just pass them as arguments
        - You must use Absolute File Paths

        `wappdriver` will automatically detect whether a string is a message or a file path.

        For more details visit : https://aahnik.github.io/wappdriver
        '''

        if self.wappdriver.load_person(to):
            with tqdm(total=len(args)) as progress:
                for arg in args:
                    if category(arg) == 'text':
                        self.wappdriver.send_text(arg)
                    else:
                        self.wappdriver.send_file(arg, category(arg))
                        size_mb = os.stat(arg).st_size*1e-6
                        time.sleep((self.timeout/10)*size_mb)
                    progress.update(1)

    def __exit__(self, exception_type, exception_value, traceback):
        time.sleep(5)
        print('Closing WhatsApp')
        self.wappdriver.driver.close()
