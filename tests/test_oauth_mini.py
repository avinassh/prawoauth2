#!/usr/bin/env python

import os

import praw
from prawoauth2 import PrawOAuth2Mini

supported_subreddits = 'testtesttest'
user_agent = ('This is a test script, written for testing prawoauth2.'
              'https://github.com/avinassh/prawoauth2/'
              '(by /u/avinassh)')
scopes = ['identity', 'submit', 'read']

app_key = os.getenv('APP_KEY')
app_secret = os.getenv('APP_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
refresh_token = os.getenv('REFRESH_TOKEN')
test_subreddit = os.getenv('TEST_SUBREDDIT')


def test_oauth_mini():
    reddit_client = praw.Reddit(user_agent=user_agent)
    oauth_helper = PrawOAuth2Mini(
        reddit_client, app_key=app_key, app_secret=app_secret,
        access_token=access_token, refresh_token=refresh_token, scopes=scopes)
    try:
        subreddit = reddit_client.get_subreddit(test_subreddit)
        comment = list(subreddit.get_comments(limit=1)).pop()
    except praw.errors.OAuthInvalidToken:
        oauth_helper.refresh()
    assert comment
    assert comment.reply('reply from a bot, please ignore')
