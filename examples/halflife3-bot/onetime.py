#!/usr/bin/env python

# import os

import praw
from prawoauth2 import PrawOAuth2Server

from tokens import app_key, app_secret
from settings import user_agent, scopes

reddit_client = praw.Reddit(user_agent=user_agent)
oauthserver = PrawOAuth2Server(reddit_client, app_key=app_key,
                               app_secret=app_secret, state=user_agent,
                               scopes=scopes)

# start the server, this will open default web browser
# asking you to authenticate
oauthserver.start()
tokens = oauthserver.get_access_codes()
print(tokens)

# may be set the env variables here only?
# os.environ['HL3_ACCESS_TOKEN'] = tokens['access_token']
# os.environ['HL3_REFRESH_TOKEN'] = tokens['refresh_token']
