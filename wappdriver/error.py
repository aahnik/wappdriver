''' 
This module error.py defines custom Wappdriver Exception. 
WappDriver Excpetion helps in abstracting internal exception details from the end user
---

`local` and `remote` modules from `data` subpackage, should not import `error` in order to 
prevent cyclic import

When you import this module or any function from this module, local is ensured 😊
'''
import functools
from .data import local
import logging


class WappDriverError(Exception):
    '''
    Custom Exception Class

    WappDriverError is to be raised for errors in functioning of WappDriver.

    ---
    ### Attributes

    internal - - actual exceptions and full traceback which are being abstracted away from end user

    problem  - -  what could have went wrong according to the developer 

    message -- custom message explainng what could have caused the error and how to resolve it. When displayed, message is prefixed with the words `Make sure to have:` 

    ---
    - The `problem` and current time will be the heading of any particular log
    - `internal` is not shown to the user, but logged.

    ---
    Raising an WappDriverError automatically logs the entire internal error messages with timestamps.The logs are not displayed to the user, rather they are appended to the log file.
    '''

    def __init__(self, internal, problem, message):
        self.internal = internal
        self.problem = problem
        self.message = message
        super().__init__(self.message)

        logging.basicConfig(format='\n########################################\n\n%(asctime)s - %(message)s',
                            filename=local.log_file)

        logging.exception(f'''\n{problem}\n\n{internal}''')

    def __str__(self):
        return f'''
        Please check Internet Connection and always use the latest version of wappdriver.
        ------------------------------------------------------------------------------------
        WappDriver Error  : {self.problem} \n
        Make sure to have : {self.message} \n
        For Help Visit https://aahnik.github.io/wappdriver/docs/help.html
        -----------------------------------------------------------------------------------\n
        '''


def handle_errors(problem, message):
    '''
    ### How to use ?
    -- FOR INTERNAL USE ONLY --

    Write the vulnerable code inside a function. And decorate it with `handle_error`. There should be no `return` statement inside the vulnerable function. The intended use case is for a procedural function.

    ---
    Example use 

    ```python
    # when displayed, message is prefixed with the words `Make sure to have:` 
    @handle_errors(problem='this not done',message='that')
    def vulnerable_function(arg):
        print('fishy errors')
        print(1/0)
    ```
    ---
    #### After being decorated, the vulnerable function will return `True` or `False` to the caller

    - `True` will be returned in case of no error
    - If an error is caught it will be handled and beautified message will be displayed to user
        - The internal details of the Exception and full traceback will be logged.
        - `False` will be returned to the caller.

    ---
    `handle_errors` is a Decorator Factory which is used to create a decorator that takes arguments
    '''

    def decorator_func(vulnerable_func):
        '''
        Actual Decorator to handle errors. It is nested inside a decorator factory, 
        as this decorator needs to take two arguments.

        '''
        @functools.wraps(vulnerable_func)
        def wrapper_func(*args, **kwargs):
            '''
            Wrapper Function to wrap vulnerable functions in WappDriver.
            This is internally used by WappDriver. 

            Not intended to be used by users of WappDriver
            '''
            try:
                vulnerable_func(*args, **kwargs)
                return True  # when the vulnerable code does not raise any error
            except Exception as internal:
                try:
                    raise WappDriverError(internal, problem, message)
                except Exception as err:
                    # Beautified Error message is printed and False is returned to caller
                    print(err)
                    return False
        return wrapper_func
    return decorator_func
