# wappdriver

API for WhatsApp Web Automation

Wondering how to send WhatsApp messages using Python using only three lines of code? **You have come to the right place!**

[![Tests](https://img.shields.io/badge/tests-passing-green)](https://aahnik.github.io/wappdriver/docs/Tests.html)
[![Maintenance](https://img.shields.io/maintenance/yes/2020)](https://github.com/aahnik/wappdriver/graphs/commit-activity)
[![GitHub Release](https://img.shields.io/github/v/release/aahnik/wappdriver)](https://github.com/aahnik/wappdriver/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/aahnik/wappdriver/badge)](https://www.codefactor.io/repository/github/aahnik/wappdriver)

## It is very simple to use

```python
from wappdriver import WhatsApp
with WhatsApp() as bot:
    bot.send('aahnik',  # name of recipient
             'hi send by a bot')  # message
# The name of the recipient should be in your contacts
```

_`wappdriver` enables you to send WhatsApp messages programmatically, using only three lines of code._

A python package that helps you automate sending messages through WhatsApp Web 😎

## How to install

```shell
pip install wappdriver
```

For Mac and Linux, you may need to use `pip3`.

[PyPI](https://pypi.org/project/wappdriver/)

[![MIT LICENSE](https://img.shields.io/pypi/l/ansicolortags.svg)](/LICENSE)

<!-- ----
**Advise**: If you are thinking about making high-quality smooth automations switch to Telegram. WhatsApp is the worst messenger available to humanity. WhatsApp does not provide any Official free API. And to operate with WhatsApp Web you need your phone to be connected to the internet. And the QR code login mechanism makes it even slower. On the other hand, Telegram is cloud-based, and simply just better.

I literally hate WhatsApp. Its my frustration with WhatsApp that forces me to write this message. Switch to Telegram, Enjoy a better life. Checkout my [Telegram Bots](https://github.com/aahnik/lovely-telegram#lovely-telegram).

---- -->

## Requirements

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- **[Chrome Browser](https://www.google.com/chrome/)**
- [Chrome Driver](https://chromedriver.chromium.org/)

Make sure to have matching versions of the Chrome Browser and Chrome Driver.
I recommend using the latest stable release for both to get the best performance.

WappDriver does not support other Browsers. Please use Chrome for a smooth experience

## Help

Read the [Help Page](https://aahnik.github.io/wappdriver/help/)

For further assistance you can [ask a question](https://github.com/aahnik/wappdriver/issues/new/choose) the issues section.

## Why wappdriver

- fast and reliable
- WhatsApp's website structure may change, the selectors can be updated over the internet dynamically, without changing code.
- chrome Driver path setting is hassle-free
- actively maintained
- fast support, if you need help
- send messages with bold, italics, or strikethrough
- send emojis
- send images, videos, and gifs
- send documents and files
- can set a custom time out  to make wappdriver run properly on old computers or with a slow internet connection
- more new features will be added soon

[Read](https://aahnik.github.io/wappdriver/usage/01_first_time_setup/) the full Documentation to know about all the features.

## Contributing

Please look at [Code of Conduct](https://github.com/aahnik/wappdriver/blob/master/.github/CODE_OF_CONDUCT.md#contributor-covenant-code-of-conduct) and [Contributing Guidelines](https://github.com/aahnik/wappdriver/blob/master/.github/CONTRIBUTING.md#how-to-contribute-to-wappdriver-)

Please read the explanation of the detailed working of `wappdriver` from the [Developer's Guide.](https://aahnik.github.io/wappdriver/For_Developers/)

## Legal

This code is in no way affiliated with, authorized, maintained, sponsored, or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software.

This project is distributed under [MIT License](https://github.com/aahnik/wappdriver/blob/main/LICENSE)
