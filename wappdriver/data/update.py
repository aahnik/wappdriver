'''This module update.py provides functions to  make the data files dynamic.
The values of the selectors are updated from the internet, first time when the user runs wappdriver

Updates can be performed manually by calling `update_vars()`
'''

from . import local, remote




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
