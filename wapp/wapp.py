from selenium.webdriver.remote.remote_connection import LOGGER
from util import convey, updateCDIP

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as expCond
except Exception as error:
    message = " Dependancy Package selenium  not found. You can install it by \n\t pip3 install selenium"
    convey(error, message)
    quit()


try:
    import yaml
except Exception as error:
    message = " Dependancy Package pyyaml not found. You can install it by \n\t pip3 install pyyaml"
    convey(error, message)
    quit()


with open('var.yaml', 'r') as var_file:
    _var = yaml.full_load(var_file)


class Wapp():
    def __init__(self, session):
        if self.load_chrome_driver():
            if self.load_main_screen():
                log()


    def load_chrome_driver(self, session='default', tried=0):
        while tried <= 3:
            try:
                chrome_options = Options()
                chrome_options.add_argument(f'--user-data-dir={session}')
                self.driver = webdriver.Chrome(
                    options=chrome_options, executable_path=_var['chrome_driver_path'])
                return True 
            except Exception as error:
                print("Chrome Driver could not be successfuly loaded...")
                updateCDIP()
                tried += 1
        return False


    def load_main_screen(self, wait=10):
        try:
            self.driver.get(_var['whatsapp_web_url'])
            WebDriverWait(self.browser, wait).until(
                expCond.presence_of_element_located((By.CSS_SELECTOR, _var['cpbleSlctbleTxt'])))
            status = True
        except Exception as error:
            convey(
                error, "Could not load main screen of WhatsApp Web because of some errors")
            status = False
        finally:
            return status
