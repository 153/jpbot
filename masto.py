#!/usr/bin/python3
from mastodon import Mastodon

instance_url = "https://plero.ma"

## Run once, then comment out.
# Mastodon.create_app(
#     'my',
#     api_base_url = instance_url
#     to_file = "client.secret"
# )

mastodon = Mastodon(
    client_id = "client.secret",
    api_base_url = instance_url
)

mastodon.log_in(
    'jp', #ignoreline
    'Pnw6d34ByHIFWAeV3C0p', #ignoreline
    to_file = "user.secret"
    )

mastodon = Mastodon(
    client_id = "client.secret",
    access_token = "user.secret",
    api_base_url = instance_url
)

#mastodon.toot("hello world")
