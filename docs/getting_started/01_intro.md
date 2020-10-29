# wappdriver

API for WhatsApp Web Automation

Wondering how to send WhatsApp messages using Python using only three lines of code? **You have come to the right place!**

[![Tests](https://img.shields.io/badge/tests-passing-green)](https://aahnik.github.io/wappdriver/docs/Tests.html)
[![Maintenance](https://img.shields.io/maintenance/yes/2020)](https://github.com/aahnik/wappdriver/graphs/commit-activity)
[![GitHub Release](https://img.shields.io/github/v/release/aahnik/wappdriver)](https://github.com/aahnik/wappdriver/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/aahnik/wappdriver/badge)](https://www.codefactor.io/repository/github/aahnik/wappdriver)

## It is very simple to use

<!-- ![using wappdriver](https://raw.githubusercontent.com/aahnik/wappdriver/main/docs/images/wappdriver.png). -->

```python
from wappdriver import WhatsApp
with WhatsApp() as bot:
    bot.send('aahnik',  # name of recipient
             'hi send by a bot')  # message
```

!!! note
      The name of the recipient should be in your contacts

_`wappdriver` enables you to send WhatsApp messages programmatically, using only three lines of code._

A python package that helps you automate sending messages through WhatsApp Web 😎

## How to install

```shell
pip install wappdriver
```

For Mac and Linux, you may need to use `pip3`.

[PyPI](https://pypi.org/project/wappdriver/)

[![MIT LICENSE](https://img.shields.io/pypi/l/ansicolortags.svg)](/LICENSE)

!!! warning
      - WhatsApp does not allow you to log in to the same account from multiple chrome tabs.
        So **make sure to close any chrome tab having WhatsApp Web open**. Not doing so will lead to errors.
      - Your phone which is having that WhatsApp account must stay connected to the internet for WhatsApp Web to work
      - Do not spam others. Use `wappdriver` for educational purposes only

## Requirements

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- **[Chrome Browser](https://www.google.com/chrome/)**
- [Chrome Driver](https://chromedriver.chromium.org/)

Make sure to have matching versions of the Chrome Browser and Chrome Driver.
I recommend using the latest stable release for both to get the best performance.

WappDriver does not support other Browsers. Please use Chrome for a smooth experience

## Help

Read the [Help Page](https://aahnik.github.io/wappdriver/help/)

For furthur assistance you can [ask a question](https://github.com/aahnik/wappdriver/issues/new/choose) the issues section.
