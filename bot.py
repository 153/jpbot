#!/usr/bin/python3
import time, datetime
from datetime import datetime
import masto
import justirc

bot = justirc.IRCConnection()
def get_time():
    return datetime.now().strftime("%Y%m%d-%H%M%S")

log = "log.txt"

def on_connect(bot):
    bot.set_nick("Anonymous")
    bot.send_user_packet("Anon")
    print("Connected to sageru")

def on_welcome(bot):
    bot.join_channel("#jp")
    print("Joined #jp")

def on_message(bot, channel, sender, message):
    if message.split()[0] == "!tweet":
        if len(message) < 7:
            bot.send_message(channel, "Tweets to @jp@plero.ma")
        else:
            message = message[7:]
            print(message)
            with open(log, "a") as log_it:
                log_it.write(str(" ".join([get_time(), message+"\n"])))
            masto.mastodon.toot(message)
            bot.send_message(channel, "It has been tweeted. https://plero.ma/users/jp")

bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)

bot.connect("irc.sageru.org")
bot.run_loop()
