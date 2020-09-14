'''This module update.py provides functions to  make the data files dynamic.
'''

from . import local, remote


def update_cdp(path=None):
    '''cdp stands for chrome_driver_path
    Method to set the chrome driver path, applies to your current virtual environment only
    Optional Agumemts: path ( the value of path should be the absolute path to the 
    installation of Chrome Driver executable)

    If path is not passed while calling the function, it will be taken from user input
    '''
    if not path:
        path = input('Paste the absoulte path of Chrome Driver Executable: \n')
    local.set_cdp(path)


def update_vars():
    ''' Checks for updates in var.yml, if availaible, updates the local data
    Usually takes a few seconds to run, calling this function 
    at the beginning of your script ensures that the values of xpath and css selectors used 
    for automation are up to date with the latest version of WhatsApp Web.
    '''
    local_version = local.get_local_version()
    remote_version = remote.get_remote_version()

    try:
        if remote_version > local_version:
            local.set_var(remote.get_var())
            local.set_local_version(remote_version)
        return True

    except Exception as err:
        print(err)
        return False
