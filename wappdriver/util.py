from . import update
from . import driver
from pyfiglet import Figlet


def first_time_set_up():
    update.fetch_vars()

    f = Figlet(font='big')
    print(f.renderText('wappdriver'))

    update.update_cdp()

    try:
        chrome_driver_path = open(
            update.chrome_driver_path_file, 'r').readline()
        driver.webdriver.chrome(executable_path=chrome_driver_path)

    except Exception as error:
        message = "Chrome Driver could not be successfully loaded, may be path incorrect"
        convey(error, message)


def convey(error, message):
    print(f"\n {message} \n")
    print(f'\n{error}\n')
    print("\n For help visit aahnik.github.io/wappdriver ")
