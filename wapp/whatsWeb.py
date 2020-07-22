from .util import convey
from .var import _var
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as expCond
    from selenium.webdriver.common.keys import Keys
except Exception as error:
    message = " Dependancy Package selenium  not found. You can install it by \n\t pip3 install selenium"

    convey(error, message)
    quit()


class Wapp():

    chrome_driver_path = _var['chrome_driver_path']
    whatsapp_web_url = _var['whatsapp_web_url']
    mainScreenLOaded = _var['mainScreenLOaded']
    searchSelector = _var['searchSelector']
    personLoaded = _var['personLoaded']
    mBox = _var['mBox']

    def __init__(self, session='wappDefaultSession', timeout=100):

        # the webdriver waits for an element to be detected on screen on until timeout
        self.timeout = timeout

        if self.load_chrome_driver(session):
            if self.load_main_screen():
                print("yo")
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
                    options=chrome_options, executable_path=Wapp.chrome_driver_path)
                return True
            except Exception as error:
                tried += 1
                message = f"""Chrome Driver could not be successfuly loaded ... Tried {tried} times
                Make sure that you have latest version of Chrome and Chrome Driver 

                If you have NOT updated the  Chrome Driver Installation Path please  do so

                """

                convey(error, message)

        return False

    def load_main_screen(self):
        try:
            self.driver.get(_var['whatsapp_web_url'])
            WebDriverWait(self.driver, self.timeout).until(
                expCond.presence_of_element_located((By.CSS_SELECTOR, Wapp.mainScreenLOaded)))
            return True
        except Exception as error:
            message = "Could not load main screen of WhatsApp Web because of some errors, make sure to Scan QR"
            convey(error, message)

            return False

    # selecting a person after searching contacts
    def load_selected_person(self, name):

        search_box = self.driver.find_element_by_css_selector(
            Wapp.searchSelector)
        # we will send the name to the input key box

        search_box.send_keys(name+Keys.ENTER)

        try:
            # checking whether new person is loaded or not
            personLoaded = Wapp.personLoaded.replace("{name}", name)
            WebDriverWait(self.driver, self.timeout).until(expCond.presence_of_element_located(
                (By.XPATH, personLoaded)))
            return True

        except Exception as error:
            message = f"""{name} not loaded, MAY BE NOT IN YOUR CONTACTS ...
                If you are sure {name} is in your contacts, Try checking internet connection """
            convey(error, message)

            search_box.send_keys((Keys.BACKSPACE)*len(name))
            # clearing the search bar by backspace, so that searching the next person does'nt have any issue
            return False

    def send_message(self, to, msg=''):

        self.load_selected_person(to)

        msg_box = WebDriverWait(self.driver, self.timeout).until(
            expCond.presence_of_element_located((By.XPATH, Wapp.mBox)))
        lines = msg.split('\n')

        for line in lines:
            msg_box.send_keys(line)  # write a line
            msg_box.send_keys(Keys.SHIFT + Keys.ENTER)  # go to next line

        msg_box.send_keys(Keys.ENTER)  # send message
