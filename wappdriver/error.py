''' 
This module error.py defines custom Wappdriver Exception. 
WappDriver Excpetion helps in abstracting internal exception details from the end user
---

This module can be used by any other module except `local` from `data` subpackage
'''

from .data import local
import logging

local.ensure() # to prevent errors and first time setup

logging.basicConfig(format='\n########################################\n\n%(asctime)s - %(message)s',
                    filename=local.log_file)


class WappDriverError(Exception):
    '''
    Exception raised for errors in functioning of WappDriver.

    Attributes:
    internal - - actual exceptions and full traceback which are being abstracted away from end user
    problem  - -  what could have went wrong according to the developer
    message -- custom message explainng what could have caused the error and how to resolve it

    ----------

    Use : When any error is caught in WappDriver, an WappDriverError is raised.

    ```python

    try:
        d = 2/0
        # code that might trigger some error

    except Exception as internal:   
        try:
            raise WappDriverError(internal=internal,
                                problem="could not load this / this failed ...",
                                message="check that ... / have you ..? ")
        except Exception as err:
            print(err)
    ```

    Raising WappDriverError automatically logs the entire internal error messages with timestamps.
    The logs are not displayed to the user, rather they are appended to the log file.



    '''

    def __init__(self, internal, problem, message):
        self.internal = internal
        self.problem = problem
        self.message = message
        super().__init__(self.message)

        logging.exception(f'''\n{problem}\n\n{internal}''')

    def __str__(self):
        return f'''
        ------------------------------------------------------------------------------------
        WappDriver Error Occured

        {self.message}

        Please make sure to use the latest version of wappdriver
        For Help Visit https://aahnik.github.io/wappdriver/docs/help.html
        -----------------------------------------------------------------------------------\n
        '''
