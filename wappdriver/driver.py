'''This module driver.py contains the WappDriver class, which is responsible for driving the core features of the application.
You have to create an instance of the WappDriver class, to do any meaningful activity such as
sending a text message or media(Image/GIF/Video) or PDF document
'''


from .error import handle_errors
from .data.local import get_chrome_driver_path, get_local_vars, sessions_dir,ensure

import time
import os

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.common.keys import Keys

except Exception:
    print(f'''Could not find Selenium
            Run
                pip install selenium
        ''')


class WappDriver():
    ''' The WappDriver class serves as an unofficial API to WhatsApp.
    It interacts with the webdriver to send messages
    '''

    def __init__(self, timeout):
        ensure()
        self.chrome_driver_path = get_chrome_driver_path()
        self._var = get_local_vars()
        self.timeout = timeout
        self.last_person = ''

    @handle_errors('ChromeDriver not loaded', 'correct version of Chrome and Chrome Driver')
    def load_chrome_driver(self, session):
        session_path = os.path.join(sessions_dir, session)
        chrome_options = Options()
        chrome_options.add_argument(f'--user-data-dir={session_path}')
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path=self.chrome_driver_path)

    @handle_errors('WhatsApp not loaded', 'correct version of Chrome and Chrome Driver')
    def load_main_screen(self):
        self.driver.get(self._var['whatsapp_web_url'])
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self._var['mainScreenLoaded'])))

    @handle_errors('Person search failed', '')
    def search_person(self, name):
        search_box = self.driver.find_element_by_css_selector(
            self._var['searchSelector'])
        search_box.send_keys(Keys.CONTROL+Keys.BACK_SPACE)
        search_box.send_keys(name)

    @handle_errors(problem='Person not loaded', message='person in your contacts')
    def load_person(self, name):
        if name != self.last_person:
            if self.search_person(name):
                person_button = WebDriverWait(self.driver, self.timeout).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, self._var['person'].replace('name', name))))
                person_button.click()
                self.last_person = name

    @handle_errors('Message not sent', 'no invalid emojis')
    def send_text(self, msg):
        msg_box = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, self._var['messageBox'])))
        lines = msg.split('\n')
        for line in lines:
            msg_box.send_keys(line)  # write a line
            msg_box.send_keys(Keys.SHIFT + Keys.ENTER)  # go to next line
            msg_box.send_keys(Keys.ENTER)  # send message

    @handle_errors('Button click failed', '')
    def click_button(self, button):
        button = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, self._var[button])))
        button.click()

    @handle_errors('Could not send file', 'the file you are trying to send, and you must use absolute file path')
    def send_file(self, path, inp_categ, caption=None):
        if self.click_button('attach'):
            input_field = WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, self._var[inp_categ])))
            input_field.send_keys(path)
            self.click_button('send')
