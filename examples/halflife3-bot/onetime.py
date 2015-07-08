#!/usr/bin/env python

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
print(oauthserver.get_access_codes())
