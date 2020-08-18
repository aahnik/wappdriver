from .driver import WappDriver
from .update import local_varVer_val, update_cdp, fetch_vars

if local_varVer_val == 0.0:
    print("\n Thank You for using wapp-driver. Welcome !! ")
    print("\n You have to enter the Chrome Driver Path once: only for the first time")
    update_cdp()
    print("Sucessfully Saved")
    fetch_vars()
    print("Latest values of Dynamic Variables fetched from internet !\n")
    print("If you want to change Chrome Driver Path or update Dynamic Variables")
    print("     then please visit    aahnik.github.io/wapp-driver ")


# AAHNIK 2020
