#!/usr/bin/env python

import time

import praw

__all__ = ['PrawOAuth2Mini']

REDIRECT_URL = 'http://127.0.0.1:9999/authorize_callback'
SCOPES = ['identity']
EXPIRY_DURATION = 3500


class PrawOAuth2Mini:

    def __init__(self, reddit_client, app_key,
                 app_secret, access_token,
                 refresh_token='', scopes=SCOPES,
                 redirect_url=REDIRECT_URL):
        self.reddit_client = reddit_client
        self.app_key = app_key
        self.app_secret = app_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.scopes = set(scopes)
        self.redirect_url = redirect_url
        self.validity = 0

        self._set_app_info()
        self._set_access_credentials_first_time()

    def _set_validity(self):
        self.validity = time.time() + EXPIRY_DURATION

    def _is_token_expired(self):
        return time.time() > self.validity

    def _set_app_info(self):
        self.reddit_client.set_oauth_app_info(self.app_key, self.app_secret,
                                              self.redirect_url)

    def _set_access_credentials(self):
        self.reddit_client.set_access_credentials(self.scopes,
                                                  self.access_token,
                                                  self.refresh_token)
        self._set_validity()

    def _set_access_credentials_first_time(self):
        try:
            self._set_access_credentials()
        except praw.errors.OAuthInvalidToken:
            self.refesh()

    def _get_refresh_access(self):
        return self.reddit_client.refresh_access_information(
            self.refresh_token)

    def refresh(self):
        if self._is_token_expired():
            tokens = self._get_refresh_access()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            self._set_access_credentials()
