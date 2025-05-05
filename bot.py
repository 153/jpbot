#!/usr/bin/python3
import time, datetime
from datetime import datetime
import masto
import justirc
import requests
import re

server = ""
channel = ""
nick = ""
user = ""
log = "log.txt"
time_s = "%Y%m%d-%H%M%s"

twitter_url = ""

notif_check = 0

bot = justirc.IRCConnection()

def get_time():
    return datetime.now().strftime(time_s)
def on_connect(bot):
    bot.set_nick(nick)
    bot.send_user_packet(user)
    print("Connected to server")

def on_welcome(bot):
    bot.join_channel(channel)
    print("Joined", channel)

def on_message(bot, channel, sender, message):
    check_mentions(bot, channel)
    
    if message.split()[0] == "!tweet":
        if len(message) < 7:
            bot.send_message(channel, f"Tweets to {twitter_url}")
        else:
            message = message[7:]
            print(message)
            with open(log, "a") as log_it:
                log_it.write(str(" ".join([get_time(), message+"\n"])))
            if "http" or "#" in message:
                masto.mastodon.status_post(visibility="unlisted", status=message)
            else:
                masto.mastodon.status_post(visibility="public", status=message)
            bot.send_message(channel, f"It has been tweeted. {twitter_url}")

def check_mentions(bot, channel):
    global notif_check
    now = int(time.time())
    if (now - notif_check) > 30:
        notif_check = now
        new_ats = masto.mastodon.notifications(mentions_only=True)
        for a in new_ats:
            sender = "@" + a["status"]["account"]["acct"]
            msg = a["status"]["pleroma"]["content"]["text/plain"]
            msg = ": ".join([sender, msg])
            bot.send_message(channel, msg)
        masto.mastodon.notifications_clear()
            
bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)

masto.mastodon.notifications_clear()
notif_check = int(time.time())


bot.connect(server)
bot.run_loop()
