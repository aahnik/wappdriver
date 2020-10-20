'''
API for WhatsApp Web Automation

---

Wondering how to send WhatsApp messages using Python using only few lines of code? **You have come to the right place!**

_`wappdriver` enables you to send WhatsApp messages programmatically, using only 3 lines of code._

**A python package that helps you automate sending messages through WhatsApp Web 😎**

[README](https://aahnik.github.io/wappdriver/) for more information about 
New Features,
How to install,
Warning,
Requirements,
How to use,
Contributing and
Help.

This page is detailed documentation of the internals of wappdriver, automatically generated from docstrings.

This page is intended for developer's who want to contribute code to wappdriver. 

If you wish to just use wappdriver, read the [Usage Guide](https://aahnik.github.io/wappdriver/docs/Documentation.html#usage-documentation)



'''

__version__ = "0.6.0"

# from .context import Wapp
from .data.local import set_chrome_driver_path, update_vars
# from .error import handle_errors
# from .driver import WappDriver
from .whatsapp import category, WhatsApp

# AAHNIK 2020
