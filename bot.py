#!/usr/bin/python3
import time, datetime
from datetime import datetime
import masto
import justirc
import requests
import re

server = "irc.sageru.org"
channel = "#jp"
nick = "Anonymous"
user = "anon"
log = "log.txt"
time_s = "%Y%m%d-%H%M%s"

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
    if message.split()[0] == "!tweet":
        if len(message) < 7:
#            bot.send_message(channel, "Tweets to @jp@plero.ma")
            bot.send_message(channel, "Twitter bot")
        else:
            message = message[7:]
            print(message)
            with open(log, "a") as log_it:
                log_it.write(str(" ".join([get_time(), message+"\n"])))
            masto.mastodon.toot(message)
            bot.send_message(channel, "It has been tweeted.")

bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)

bot.connect(server)
bot.run_loop()
