from datetime import datetime
import yaml


def convey(error, message):
    print(f"\n {message} \n")
    print("For Help Contact Aahnik Daw, the author...")
    print("Email: aahnikdaw@gmail.com \n")
    print("\t\tPress ENTER to skip")

    if input("Type in 'detail' + press ENTER to see Exceptions caught.") == 'detail' or "'detail'":
        print(f'\n{error}\n')


def updateCDIP():  # Chrome Driver Installation Path
    path = input("""
    Please enter the absolute path where chrome driver is installed Copy and paste the path 
    For help copy this URL (  ) and paste in your browser to watch the tutorial video """)

    with open('var.yaml', 'r') as var_file:
        _var = yaml.full_load(var_file)
        new = {'chrome_driver_path': f'{path}'}
        _var.update(new)
        yaml.dump(_var, var_file)


def log(*msgs):
    now = datetime.now()
    with open('logs.txt', 'a+') as file:
        file.write(f"\n {now} {'-'*20} |START| {'-'*20} \n\n")
        for msg in msgs:
            file.write(f"{msg}\n")
        file.write(f" {'-'*50}|END|{'-'*20} \n")
