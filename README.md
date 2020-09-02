# API for WhatsApp Web Automation 
[![Generic badge](https://img.shields.io/badge/tests-passing-<COLOR>.svg)](https://aahnik.github.io/wappdriver/)

_Send WhatsApp messages programmatically, using only 3 lines of code._ 


**A python package that helps you automate sending messages through WhatsApp Web 😎**

[![Maintenance](https://img.shields.io/maintenance/yes/2020)](https://github.com/aahnik/wappdriver/graphs/commit-activity) [![GitHub Release](https://img.shields.io/github/v/release/aahnik/wappdriver)](https://github.com/aahnik/wappdriver/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/aahnik/wappdriver/badge)](https://www.codefactor.io/repository/github/aahnik/wappdriver) 





**It's very simple to use**

```python
import wappdriver as wa
bot = wa.WappDriver()
bot.send_message(to='aahnik',msg='Hi ! sent by a bot :-p ')
# the recipients name must be saved in your contacts ...

```
![wapp_driver_scrnsht](https://user-images.githubusercontent.com/66209958/90502857-2879a600-e16c-11ea-8f7f-7bbf2a993a13.png)

**How to install ??**

```
pip3 install wappdriver
```
[PyPI](https://pypi.org/project/wappdriver/) 

[![MIT LICENSE](https://img.shields.io/pypi/l/ansicolortags.svg)]() 


---



## WARNING  ⚠️
WhatsApp does not allow you to login into the same account from multiple chrome tabs.
So **make sure to close any chrome tab which has WhatsApp Web open**, before executing the following  line when your session cookies(data for automatic login, without requiring you to scan QR code multiple times) are saved in your current directory.

`bot = wa.WappDriver()`

Not doing so may lead to errors or the program may hang. 

You will be required to scan the QR Code for the first time only, thereafter the data saved within the `wappDefaultSession` sub-directory will be used for automatic login. You can delete this folder to delete all cookies. 

---

**Requirements:**

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- [Chrome Browser](https://www.google.com/chrome/) 
- [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/)

Make sure to have matching versions of Chrome Browser and Chrome Driver.
I recommend to use the latest version of both, for the best performance

----






**Special Thanks to @VISWESWARAN1998**
I learned a lot from his [repo](https://github.com/aahnik/Simple-Yet-Hackable-WhatsApp-api) and had initially started working on it.
But as my PRs were not accepted as my needs were different, I created a seperate project totally independent from that repo.


