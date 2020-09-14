from .data import update
from pyfiglet import Figlet


def first_time_set_up():
    update.update_vars()

    f = Figlet(font='big')
    print(f.renderText('wappdriver'))

    update.update_cdp()
