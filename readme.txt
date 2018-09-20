masto.py has "instance_url" as well as "username" and "password" feields
to modify...

./client.secret and ./user.secret are necessary to allow posting.

Requires halcy's Mastodon.py and a mastodon or Pleroma account+server
of your choosing 

bot.py accepts server URL, nickname, username, and channel name.
  !tweet something
posts a message to the Mastodon account you configured in
masto.py. 


pip3 install Mastodon
nano masto.py
nano bot.py
chmod +x masto.py
chmod +x bot.py
python3 masto.py
python3 bot.py

