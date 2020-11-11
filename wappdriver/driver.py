'''This module driver.py contains the WappDriver class, which is responsible for driving the core features of the application.
You have to create an instance of the WappDriver class, to do any meaningful activity such as
sending a text message or media(Image/GIF/Video) or PDF document
'''


import logging
from .error import handle_errors
from .local import chrome_driver_path, get_selectors, sessions_dir, ensure

import time
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

    def __init__(self, timeout):
        ensure()
        self._selector = get_selectors()
        self.timeout = timeout
        self.last_person = ''

    @handle_errors('ChromeDriver not loaded', '')
    def load_chrome_driver(self, session):
        logging.info('loading chrome driver')
        if 'user' in self._selector.keys():
            session_path = self._selector['user']
            logging.warning('You are using a special feature')
        else:
            session_path = os.path.join(sessions_dir, session)
            logging.warning(f'You are using {session_path}')
        chrome_options = Options()
        chrome_options.add_argument(f'--user-data-dir={session_path}')
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path=chrome_driver_path())

    @handle_errors('WhatsApp not loaded', '')
    def load_main_screen(self):
        logging.info('loading whatsapp web')
        self.driver.get(self._selector['whatsapp_web_url'])
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self._selector['mainScreenLoaded'])))

    @handle_errors('Person search failed', '', quit)
    def search_person(self, name):
        logging.info(f'searching for person {name}')
        search_box = self.driver.find_element_by_xpath(
            self._selector['searchSelector'])
        search_box.send_keys(Keys.CONTROL+Keys.BACK_SPACE)
        search_box.send_keys(name)

    @handle_errors(problem='Person not loaded', message='May be person in your contacts')
    def load_person(self, name):
        logging.info(f'loading person {name}')
        if name != self.last_person:
            if self.search_person(name):
                person_button = WebDriverWait(self.driver, self.timeout).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, self._selector['person'].replace('name', name))))
                person_button.click()
                self.last_person = name

    @handle_errors('Message not sent', 'ChromeDriver only supports characters in the BMP. So many emojis may be invalid.')
    def send_text(self, msg):
        logging.info(f'sending message {msg[:10]}')
        msg_box = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, self._selector['messageBox'])))
        lines = msg.split('\n')
        for line in lines:
            msg_box.send_keys(line)  # write a line
            msg_box.send_keys(Keys.SHIFT + Keys.ENTER)  # go to next line
            msg_box.send_keys(Keys.ENTER)  # send message

    @handle_errors('Button click failed', '')
    def click_button(self, button):
        logging.info(f'clicking on button {button}')
        button = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, self._selector[button])))
        button.click()

    @handle_errors('Could not send file', 'the file you are trying to send, and you must use absolute file path')
    def send_file(self, path, inp_categ, caption=None):
        logging.info(f'sending {inp_categ} {path}')
        if self.click_button('attach'):
            input_field = WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, self._selector[inp_categ])))
            input_field.send_keys(path)
            self.click_button('send')
