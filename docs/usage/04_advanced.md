# Advanced

## Tired bot

If your computer or internet is very slow, you may face timeout exceptions, or messages not being sent properly. In this case we call our bot exhausted or tired.
 
You can solve this by overriding the default timeout value.This can be done by passing an optional argument to the `WhatsApp` context manager.

```python
from wappdriver import WhatsApp

with WhatsApp(timeout=100) as bot:
    bot.send('aahnik',  'Exhausted ?')
```
The default value of timeout is 50s ( when you dont pass the argument)

If bot is exhausted, increase timeout.

## Update Variables 

When you run `wappdriver` for the first time, the values of selectors is fetched from the internet.

If you want to update them
```python
from wappdriver import update_vars
update_vars()
```
If any new updates are availaible, they will be downloaded.

## Set Chrome Driver Path

When you will use `wappdriver` for the first time, it will ask you to input the path of Chrome Driver Executable in your system.

You can set the path programmatically 
```python
from wappdriver import set_chrome_driver_path
path = '/home/aahnik/Downloads/chrome_driver' 
set_chrome_driver_path(path)
```

**Replace the value of variable `path` with the path of chrome driver in your system.**

## In Brief

Pass name of recipient as first argument and after that you can pass as many message arguments as you wish. 

- The name of recipient must be saved in your contacts.
- Each message argument must be a string. 
- If you want to send a file, pass the absolute path of the file to the function.
        
---
Example Use:

```python

with WhatsApp() as bot:
    bot.send('aahnik',  # name of recipient

            'hi send by a bot',  # message

            # absolute path of an image on computer
            '/home/aahnik/image.png',  

            # absolute path of a video on computer
            '/home/aahnik/video.mp4',  

            # absolute path of pdf on computer
            '/home/aahnik/django.pdf'  
            )
```


The first argument you need to pass is the recipient's name which must be saved in your phone.

After that you can pass as many string arguments you want for message. 
The string can be:
- a text message or 
- the file path if you want to send a image, video, GIF, documents etc.
- you can send multiple files, just pass them as arguments
- You must use Absolute File Paths
  
`wappdriver` will automatically detect whether a string is a message or a file path.

---

<!-- **If you are a developer and want to contribute code, read [Developer Guide](https://aahnik.github.io/wappdriver/dev/wappdriver/)** -->