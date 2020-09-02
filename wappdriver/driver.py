from .util import first_time_set_up, convey
from . import update as up

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expCond
from selenium.webdriver.common.keys import Keys

import yaml


class WappDriver():

    def __init__(self, session='wappDefaultSession', timeout=100):

        if up.local_varVer_val == 0.0:
            first_time_set_up(up)

        self.chrome_driver_path = open(up.chrome_driver_path).readline()
        with open(up.var) as file:
            _var = yaml.full_load(file)

        self.whatsapp_web_url = _var['whatsapp_web_url']
        self.mainScreenLOaded = _var['mainScreenLOaded']
        self.searchSelector = _var['searchSelector']
        self.mBox = _var['mBox']

        # the webdriver waits for an element to be detected on screen on until timeout

        self.timeout = timeout

        if self.load_chrome_driver(session):
            if self.load_main_screen():
                print("Yo!! sucessfully loaded WhatsApp Web")
            else:
                self.driver.quit()
        else:
            self.driver.quit()

    def load_chrome_driver(self, session, tried=0):
        while tried <= 3:
            try:
                chrome_options = Options()
                chrome_options.add_argument(f'--user-data-dir={session}')
                self.driver = webdriver.Chrome(
                    options=chrome_options, executable_path=self.chrome_driver_path)
                return True
            except Exception as error:
                tried += 1
                message = f"""Chrome Driver could not be successfuly loaded 
                Make sure that you have latest and matching versions of Chrome and Chrome Driver 
                CHROME DRIVER INSTALLATION PATH IS INVALID !!
                """
                convey(error, message)
                up.update_cdp()

        return False

    def load_main_screen(self):
        try:
            self.driver.get(self.whatsapp_web_url)
            WebDriverWait(self.driver, self.timeout).until(
                expCond.presence_of_element_located((By.CSS_SELECTOR, self.mainScreenLOaded)))
            return True
        except Exception as error:
            message = "Could not load main screen of WhatsApp Web because of some errors, make sure to Scan QR"
            convey(error, message)

            return False

    # selecting a person after searching contacts
    def load_selected_person(self, name):

        search_box = self.driver.find_element_by_css_selector(
            self.searchSelector)

        # we will send the name to the input key box
        search_box.send_keys(name)

        try:
            person = WebDriverWait(self.driver, self.timeout).until(expCond.presence_of_element_located(
                (By.XPATH, f'//*[@title="{name}"]')))
            person.click()
            return True

        except Exception as error:
            message = f"""{name} not loaded, MAY BE NOT IN YOUR CONTACTS , 
                If you are sure {name} is in your contacts, Try checking internet connection
                
               OR  May be some other problem ...  """

            convey(error, message)

            search_box.send_keys((Keys.BACKSPACE)*len(name))
            # clearing the search bar by backspace, so that searching the next person does'nt have any issue
            return False

    def send_message(self, to, msg=''):

        if self.load_selected_person(to):

            msg_box = WebDriverWait(self.driver, self.timeout).until(
                expCond.presence_of_element_located((By.XPATH, self.mBox)))
            lines = msg.split('\n')

            for line in lines:
                msg_box.send_keys(line)  # write a line
                msg_box.send_keys(Keys.SHIFT + Keys.ENTER)  # go to next line

            msg_box.send_keys(Keys.ENTER)  # send message
