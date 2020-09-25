''' 
The errors that occur during Data Handling are handled by the decorators defined in this module
'''


def handle_connection(func):
    def wrapper_func(*args):
        try:
            return func()
        except Exception as err:
            print(f'''
            -----------------------------------
                            😞

            Could not fetch data from Internet.
            Please check your connection

            {err}

            For help visit
            https://aahnik.github.io/wappdriver/docs/help.html
            -----------------------------------
            ''')
            quit()
    return wrapper_func


def handle_dependancy(func):
    def wrapper_func(*args):
        try:
            return func()
        except Exception as err:
            print(f'''
            -----------------------------------
                            😞

            Dependancies Missing

            {err}

            Please run 
                pip install pyyaml requests

            And then try again

            For help visit
            https://aahnik.github.io/wappdriver/docs/help.html
            -----------------------------------
            ''')
            quit()
    return wrapper_func
