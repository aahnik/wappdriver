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