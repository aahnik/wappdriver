# API for WhatsApp Web Automation 

[![Generic badge](https://img.shields.io/badge/send_text-yes-GREEN.svg)](https://aahnik.github.io/wappdriver/)
[![Generic badge](https://img.shields.io/badge/send_images-no-RED.svg)](https://aahnik.github.io/wappdriver/)
[![Generic badge](https://img.shields.io/badge/send_videos-no-RED.svg)](https://aahnik.github.io/wappdriver/)
[![Generic badge](https://img.shields.io/badge/send_documents-no-RED.svg)](https://aahnik.github.io/wappdriver/)
[![Generic badge](https://img.shields.io/badge/use_emojis-few-YELLOW.svg)](https://aahnik.github.io/wappdriver/)
[![Generic badge](https://img.shields.io/badge/speed-medium-ORANGE.svg)](https://aahnik.github.io/wappdriver/)

_Send WhatsApp messages programmatically, using only 3 lines of code._ 

**A python package that helps you automate sending messages through WhatsApp Web 😎**

[![Maintenance](https://img.shields.io/maintenance/yes/2020)](https://github.com/aahnik/wappdriver/graphs/commit-activity) 
[![GitHub Release](https://img.shields.io/github/v/release/aahnik/wappdriver)](https://github.com/aahnik/wappdriver/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/aahnik/wappdriver/badge)](https://www.codefactor.io/repository/github/aahnik/wappdriver) 


### It's very simple to use

```python
import wappdriver as wa
bot = wa.WappDriver()
bot.send_message(to='aahnik',msg='Hi ! sent by a bot :-p ')
# the recipients name must be saved in your contacts ...

```
![wapp_driver_scrnsht](https://user-images.githubusercontent.com/66209958/90502857-2879a600-e16c-11ea-8f7f-7bbf2a993a13.png)

### How to install ??

```
pip3 install wappdriver
```
[PyPI](https://pypi.org/project/wappdriver/) 

[![MIT LICENSE](https://img.shields.io/pypi/l/ansicolortags.svg)](/LICENSE) 


### WARNING  ⚠️

WhatsApp does not allow you to login into the same account from multiple chrome tabs.
So **make sure to close any chrome tab which has WhatsApp Web open**, before executing the following  line when your session cookies(data for automatic login, without requiring you to scan QR code multiple times) are saved in your current directory.

`bot = wa.WappDriver()`

Not doing so may lead to errors or the program may hang. 

You will be required to scan the QR Code for the first time only, thereafter the data saved within the `wappDefaultSession` sub-directory will be used for automatic login. You can delete this folder to delete all cookies. 


### Requirements

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- [Chrome Browser](https://www.google.com/chrome/) 
- [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/)

Make sure to have matching versions of Chrome Browser and Chrome Driver.
I recommend to use the latest version of both, for the best performance



### Tests
Tests are very important for any application. Jacob Kaplan-Moss said "Code without tests is broken by design". And this statement can't be more true.

So we have multiple tests to check whether this application is _working as expected_. But these tests need certain _user input_ to run such as names of people saved in your WhatsApp contacts. ( To avoid spamming, this application *allows sending messages only to your WhatsApp contacts* ).

These tests __could not be automatically run__ on server via Travis CI or GitHub Actions due to certain constraints due to the nature of WhatsApp and this application. [Know Why ?](https://github.com/aahnik/wappdriver/wiki/Testing-:-Why-not-fully-automated-%3F)

__I run the tests on a regular basis and manually update the feature badges__ at the top of this README, to indicate whether that particular feature is successfully working or not. 

If you find that any of the features is not working as expected, _feel free to create an issue_. Nonetheless, you could easily *clone this repo* and **run the tests locally** after configuring the variables in `testConfig.yml` file inside `tests` directory. To learn how to run tests [click here](). 



### Want to contribute ? 
Look at [Code of Conduct](/CODE_OF_CONDUCT.md)




### Special Thanks to @VISWESWARAN1998
I learned a lot from his [repo](https://github.com/aahnik/Simple-Yet-Hackable-WhatsApp-api) and had initially started working on it. In future, due to certain requirements, I created a seperate repo, with a different working all together.

### Help

For _help_ you can **email me** at [meet.aahnik@gmail.com](mailto:meet.aahnik@gmail.com) or **chat** on [Telegram](https://t.me/AahnikDaw).You can expect a reply within 48 hours.
