# Sending Messages

## Sending a Simple Message

The code snippet below is enough to show you how.

```python
from wappdriver import WhatsApp
with WhatsApp() as bot:
    bot.send('aahnik',  # name of recipient
             'hi send by a bot')  # message
# The name of the recipient should be in your contacts
```

## Messages with bold, italics and strike-through

To send formatted text, use the same techniques you use while typing on your smartphone.

Simply enclose the words with special characters as shown

```txt
*bold*
_italics_
-strike-
```

![Screenshot from 2020-10-08 21-02-54](https://user-images.githubusercontent.com/66209958/95480607-b2463280-09a9-11eb-8bc6-b3fd2a9bbaac.png)

## Sending Emojis

To send an emoji simply copy it from the internet and paste it in your message string.

Here are some commonly used emojis

```text
🙄 😂 😫 🤔 🔥  😌 😍 🤣 😭 😂 🙏 💕 💜 👉
```

## Sending to Multiple People

You can easily send a message to multiple people

```python
from wappdriver import WhatsApp

recipients = ['friend','mom','dad', 'boss', 'client']

with WhatsApp() as bot:
    for person in recipients:
        bot.send(person, f'hi {person} send by a bot')
```
