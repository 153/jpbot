#!/usr/bin/python3
from mastodon import Mastodon

instance_url = "https://plero.ma"

with open('client.secret', 'r') as clients:
    clients = clients.read()
if len(clients) < 5:
    ## Only needs to be ran once
    Mastodon.create_app(
        'myapp',
        api_base_url = instance_url,
        to_file = "client.secret"
    )

mastodon = Mastodon(
    client_id = "client.secret",
    api_base_url = instance_url
)

mastodon.log_in(
#    'username',  
#    'password',
    to_file = "user.secret"
    )

mastodon = Mastodon(
    client_id = "client.secret",
    access_token = "user.secret",
    api_base_url = instance_url
)

mastodon.toot("Connected")
