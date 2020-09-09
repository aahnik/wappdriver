from . import update
from pyfiglet import Figlet

def first_time_set_up():
    f = Figlet(font='big')
    print(f.renderText('wapp'))
    print(f.renderText('driver'))

    print(
        "\n You have to enter the Chrome Driver Path once: only for the first time")
    update.update_cdp()
    print("Sucessfully Saved")
    update.fetch_vars()
    

def convey(error, message):
    print(f"\n {message} \n")
    print(f'\n{error}\n')
    print("\n For help visit aahnik.github.io/wappdriver ")
