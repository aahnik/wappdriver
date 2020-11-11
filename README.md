# wappdriver

API for WhatsApp Web Automation

Wondering how to send WhatsApp messages using Python using only three lines of code? **You have come to the right place!**

[![Tests](https://img.shields.io/badge/tests-passing-green)](https://aahnik.github.io/wappdriver/docs/Tests.html)
[![Maintenance](https://img.shields.io/maintenance/yes/2020)](https://github.com/aahnik/wappdriver/graphs/commit-activity)
[![GitHub Release](https://img.shields.io/github/v/release/aahnik/wappdriver)](https://github.com/aahnik/wappdriver/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/aahnik/wappdriver/badge)](https://www.codefactor.io/repository/github/aahnik/wappdriver)
[![MIT LICENSE](https://img.shields.io/pypi/l/ansicolortags.svg)](/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Usage 😎

wappdriver is a python package that helps you automate sending messages through WhatsApp Web.

_It enables you to send WhatsApp messages programmatically, using only three lines of code._

It is very simple to use

```python
from wappdriver import WhatsApp
with WhatsApp() as bot:
    bot.send('aahnik',  # name of recipient
             'hi send by a bot')  # message
# The name of the recipient should be in your contacts
```

Read **[full documentation 📖](https://aahnik.github.io/wappdriver/usage/02_sending_messages/)** to learn how to send emojis, media and files.

## Installation ⏬

You can easily install wappdriver from the [PyPI](https://pypi.org/project/wappdriver/).

```shell
pip install wappdriver
```

For Mac and Linux, you may need to use `pip3`.

## Requirements 🧑‍💻

You must have the following installed in your system for wappdriver to work.

- [Chrome Browser](https://www.google.com/chrome/)
- [Chrome Driver](https://chromedriver.chromium.org/)

Make sure to have matching versions of the Chrome Browser and Chrome Driver.
I recommend using the latest stable release for both to get the best performance.

WappDriver does not support other Browsers. Please use Chrome for a smooth experience.

## Setup ⚙️

After you have installed wappdriver and the requirements stated above, you can start using wappdriver straight away.

When you will run your code for the first time, you will be asked for Chrome Driver Path.
When the WhatsApp web screen loads for the first time, you have to scan the QR code from you smartphone's WhatsApp application, to log into your WhatsApp account. [Learn more](https://aahnik.github.io/wappdriver/usage/01_first_time_setup/).

<!-- Read more about [first time setup](https://aahnik.github.io/wappdriver/usage/01_first_time_setup/) on the official docs page. -->

## Getting Help 💁🏻

First of all, read the [Help Page](https://aahnik.github.io/wappdriver/help/).
You may try to search your question in the search bar on the page.

For further assistance you may [ask a question](https://github.com/aahnik/wappdriver/issues/new/choose) the issues section.

## Contributing 🤩

Please look at [Code of Conduct](https://github.com/aahnik/wappdriver/blob/master/.github/CODE_OF_CONDUCT.md#contributor-covenant-code-of-conduct) and [Contributing Guidelines](https://github.com/aahnik/wappdriver/blob/master/.github/CONTRIBUTING.md#how-to-contribute-to-wappdriver-).

Please read the explanation of the detailed working of `wappdriver` from the [Developer's Guide.](https://aahnik.github.io/wappdriver/dev/wappdriver/)

## Legal ⚖️

This project is distributed under [MIT License](https://github.com/aahnik/wappdriver/blob/main/LICENSE).

This code is in no way affiliated with, authorized, maintained, sponsored, or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software.
