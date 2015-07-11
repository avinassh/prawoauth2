#!/usr/bin/env python

import praw
from prawoauth2 import PrawOAuth2Mini

from tokens import app_key, app_secret, access_token, refresh_token
from settings import scopes, user_agent

reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,
                              app_secret=app_secret, access_token=access_token,
                              scopes=scopes, refresh_token=refresh_token)


def half_life_loop():
    oauth_helper.refresh()
    for comment in reddit_client.get_comments('all'):
        if 'half life' in comment.body.lower():
            print('shit, someone mentioned Half Life 3 again :@')
            comment.reply('Don\'t mention Half Life 3!')

while True:
    try:
        half_life_loop()
    except praw.errors.OAuthInvalidToken:
        # token expired, refresh 'em!
        oauth_helper.refresh()
