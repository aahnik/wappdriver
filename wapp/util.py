from datetime import datetime



def convey(error, message):
    print(f"\n {message} \n")
    print("For Help Contact Aahnik Daw, the author...")
    print("Email: aahnikdaw@gmail.com \n")
    print("\t\tPress ENTER to skip")

    if input("Enter d to see details about Exceptions caught.\n") == 'd':
        print(f'\n{error}\n')


