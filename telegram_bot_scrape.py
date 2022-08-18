# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import telepot
import time
import requests


def send_telegram_msg(bot_token, chat_id, msg, parse_mode=None):
    r = requests.post(
        "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&parse_mode={2}".format(bot_token, chat_id, parse_mode),
        {"text": msg})

# We open the html file and read its contents with the read method.
HTMLFile = open("messages8.html", "r")
index = HTMLFile.read()
# BeautifulSoup object is created, the HTML data is passed to the constructor. The second option specifies the parser.
S = BeautifulSoup(index, 'lxml')
# set telegram token to telepot
bot = telepot.Bot('5195978214:AAHZ-5AyXw0foQqIVpKDZByZkPHBJmkpgNw')

# this for to loop around each tag div and has class body
for tag in S.findAll("div", {"class": "body"}):

    div_tag = '{0}'.format(tag)
    # to get tag img from tag div
    image = '{0}'.format(tag.img)
    # to get its text content.
    text_message = '{0}'.format(tag.text.encode('utf-8'))
    date = ""
    # to check if div has title {date}
    if 'title="' in div_tag:
        date = tag.div.attrs["title"][:10]
        # date = text.replace("\n", " ").split('title="', 20)[1][:10]

    # print for show result
    print (date + "" + text_message.replace("\n", " "))
    print ('####################################')

    # to collect message elements
    full_message = date + "" + text_message.replace("\n", " ")
    send_telegram_msg("5195978214:AAHZ-5AyXw0foQqIVpKDZByZkPHBJmkpgNw", "-1001527032139",
                               full_message)

    # To check if there is a tag img inside div
    if 'src' in image:
        # full_image_name = image.split('src="', 15)[1].replace('"', "")
        # full_image_name = full_image_name[:full_image_name.index('g') + 1]
        full_image_name = tag.img.attrs["src"]
        bot.sendPhoto("-1001527032139", photo=open(full_image_name, 'rb'))

        print (full_image_name)

    time.sleep(3)
