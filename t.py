from wappdriver import WhatsApp
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


wa = WhatsApp()

wa.__enter__()


wa.send('aahnik', 'hi', '/home/aahnik/Pictures/Screensho.png')
