def first_time_set_up(up):
    print("\n Thank You for using wapp-driver. Welcome !! ")
    print(
        "\n You have to enter the Chrome Driver Path once: only for the first time")
    up.update_cdp()
    print("Sucessfully Saved")
    up.fetch_vars()
    print("Latest values of Dynamic Variables fetched from internet !\n")
    print("If you want to change Chrome Driver Path or update Dynamic Variables")
    print("     then please visit    aahnik.github.io/wapp-driver ")


def convey(error, message):
    print(f"\n {message} \n")
    print("For Help Contact Aahnik Daw, the author...")
    print("Email: aahnikdaw@gmail.com \n")
    print("\t\tPress ENTER to skip")

    if input("Enter d to see details about Exceptions caught.\n") == 'd':
        print(f'\n{error}\n')
