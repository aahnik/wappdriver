def first_time_set_up(up):
    print("\n Thank You for using wapp-driver. Welcome !! ")
    print(
        "\n You have to enter the Chrome Driver Path once: only for the first time")
    up.update_cdp()
    print("Sucessfully Saved")
    up.fetch_vars()
    print("Latest values of Dynamic Variables fetched from internet !\n")
    print("If you want to change Chrome Driver Path or update Dynamic Variables")
    print("     then please visit    aahnik.github.io/wappdriver ")


def convey(error, message):
    print(f"\n {message} \n")
    print(f'\n{error}\n')
    print("\n For help visit aahnik.github.io/wappdriver ")

