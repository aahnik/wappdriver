'''This module driver.py contains the WappDriver class, which is responsible for driving the core
features of the application.
You have to create an instance of the WappDriver class, to do any meaningful activity such as
sending a text message or media(Image/GIF/Video) or PDF document
'''
from wappdriver.error import WappDriverError
from . import error  # when error is imported local is ensured
from .data import local

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class WappDriver():
    ''' The WappDriver class serves as an unofficial API to WhatsApp.
    It interacts with the webdriver to send messages
    '''

    def __init__(self, session='default', timeout=50):

        self.chrome_driver_path = local.get_chrome_driver_path()

        _var = local.get_local_vars()

        self.whatsapp_web_url = _var['whatsapp_web_url']
        self.mainScreenLoaded = _var['mainScreenLoaded']
        self.searchSelector = _var['searchSelector']
        self.mBox = _var['mBox']

        # the webdriver waits for an element to be detected on screen on until timeout
        self.timeout = timeout

        if self.load_chrome_driver(session):
            if self.load_main_screen():
                print("Yo!! sucessfully loaded WhatsApp Web")
            else:
                self.driver.quit()

    def load_chrome_driver(self, session):
        session_path = os.path.join(local.sessions_dir, session)

        try:
            chrome_options = Options()
            chrome_options.add_argument(f'--user-data-dir={session_path}')

            self.driver = webdriver.Chrome(
                options=chrome_options, executable_path=self.chrome_driver_path)

            return True

        except Exception as internal:
            try:
                raise WappDriverError(internal,
                                      problem='Chrome Driver could not be successfuly loaded',
                                      message='Make sure to have correct version of Chrome and Chrome Driver')
            except Exception as err:
                print(err)
                return False

    def load_main_screen(self):
        try:
            self.driver.get(self.whatsapp_web_url)

            WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.mainScreenLoaded)))
            return True

        except Exception as internal:
            try:
                raise WappDriverError(internal,
                                      problem='WhatsApp main screen could not be successfuly loaded',
                                      message='Make sure to have correct version of Chrome and Chrome Driver')
            except Exception as err:
                print(err)
                return False

    # selecting a person after searching contacts

    def load_person(self, name):

        search_box = self.driver.find_element_by_css_selector(
            self.searchSelector)

        # we will send the name to the input key box
        search_box.send_keys(name)

        try:
            person = WebDriverWait(self.driver, self.timeout).until(expected_conditions.presence_of_element_located(
                (By.XPATH, f'//*[@title="{name}"]')))
            person.click()
            return True

        except Exception as error:
            message = f'''{name} not loaded, MAY BE NOT IN YOUR CONTACTS , 
                If you are sure {name} is in your contacts, Try checking internet connection
                
               OR  May be some other problem ...  '''

            search_box.send_keys((Keys.BACKSPACE)*len(name))
            # clearing the search bar by backspace, so that searching the next person does'nt have any issue
            return False

    def send_message(self, to, msg):
        '''Method to send a text message to a contact.
        Requires two arguments: to and msg

        Example Use :
        bot.send_message(to='contact',msg='hi')
        or 
        bot.send_message('contact','hi')
        where bot is an object of WappDriver class
        '''

        if self.load_person(to):
            msg_box = WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, self.mBox)))
            lines = msg.split('\n')

            for line in lines:
                msg_box.send_keys(line)  # write a line
                msg_box.send_keys(Keys.SHIFT + Keys.ENTER)  # go to next line

            msg_box.send_keys(Keys.ENTER)  # send message

            return True

    def send_media(self, to, path, caption=None):
        '''Method to send a media object to a contact.
        Supports: Image, GIF, Video
        Requires two arguments: to and path
        Optional argument: caption

        Example Use :
        bot.send_media(to='contact',path='path/to/media',caption='wow')
        or
        bot.send_media('contact','path/to/media','wow')
        where bot is an object of WappDriver class

        Not giving the caption is allowed
        '''

        if self.load_person(to):
            pass

    def send_file(self, to, path):
        '''Method to send any kind of file to a contact.
        Supports: ALl formats
        Requires two arguments: to and path

        Example Use :
        bot.send_file(to='contact',path='path/to/file')
        or
        bot.send_file('contact','path/to/file')
        where bot is an object of WappDriver class

        Not giving the caption is allowed
        '''

    def send_contact(self, to, contact):
        pass

    def send_url(self, to, url):
        pass
