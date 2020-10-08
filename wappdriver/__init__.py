'''
Wondering how to send WhatsApp messages using Python using only few lines of code? You have come to the right place!

`wappdriver` enables you to send WhatsApp messages programmatically, using only 3 lines of code.

A python package that helps you automate sending messages through WhatsApp Web 

WappDriver now supports sending images , videos, documents and other file types... 

Learn usage (https://aahnik.github.io/wappdriver/docs/Documentation.html)

'''

__version__ = "0.5.6"

# from .context import Wapp
from .data.local import set_chrome_driver_path, update_vars
# from .error import handle_errors
# from .driver import WappDriver
from .whatsapp import category,WhatsApp

# AAHNIK 2020
