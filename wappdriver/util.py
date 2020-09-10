from . import update
from pyfiglet import Figlet


def first_time_set_up():
    update.fetch_vars()

    f = Figlet(font='big')
    print(f.renderText('wappdriver'))

    update.update_cdp()


def convey(error, message):
    print(f"\n {message} \n")
    print(f'\n{error}\n')
    print("\n For help visit aahnik.github.io/wappdriver ")
