import wappdriver as wa
bot = wa.WappDriver()
bot.send_message(to="aahnik", msg="Hi ! sent by a bot :-p") # sending to a person in contact list
bot.send_message(to="nobody", msg="Hi ! sent by a bot :-p") # sending to nobody is designed to fail. 
# Have fun
