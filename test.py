# make sure to change the values before running

from wappdriver import WhatsApp

with WhatsApp() as bot:
    bot.send('aahnik',  # name of recipient
             'hi send by a bot :-p',  # message

             # absolute url of an image that exists on your computer
             '/home/aahnik/Pictures/image_icon.png',  # 115 Kb

             # absolute url of a video that exists on your computer
             '/home/aahnik/Downloads/example_types/file_example_MP4_640_3MG.mp4',  # 3.1 MB

             # absolute url of a pdf that exists on your computer
             '/home/aahnik/Downloads/docs/django.pdf'  # 7 MB
             )
