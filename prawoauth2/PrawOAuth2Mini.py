#!/usr/bin/env python

import time

import praw

__all__ = ['PrawOAuth2Mini']

REDIRECT_URL = 'http://127.0.0.1:9999/authorize_callback'
SCOPES = ['identity', 'read']
EXPIRY_DURATION = 3500


class PrawOAuth2Mini:

    """
    Creates a `PrawOAuth2Mini` instance. `PrawOAuth2Mini` meant to be
    used in the bot and it needs valid `access_token` and `refresh_token`
    to operate. Once the `access_token` is expired, it will be refreshed
    using the `refresh_token`

    :param reddit_client: An Instance of praw
    :param app_key: App Secret (or also known as Client Id) of your
        app. Find them here: https://www.reddit.com/prefs/apps/
    :param app_secret: App Key (or also known as Client Secret) of your
        app. Find them here: https://www.reddit.com/prefs/apps/
    :param access_token: Once you have authorized your Reddit account with
        the app/bot/script using `PrawOAuth2Server`, you get a valid
        `access_token` (which expires after 60 minutes).
    :param refresh_token: Once you have authorized your Reddit account with
        the app/bot/script using `PrawOAuth2Server`, you get a valid
        `refresh_token`.
    :param scopes: List of scopes for OAuth. Default is `['identity', 'read']`.
        https://praw.readthedocs.org/en/latest/pages/oauth.html#oauth-scopes
    :param redirect_url: Redirect URL used in authorization process using
        `PrawOAuth2Server`. Default is `http://127.0.0.1:9999/authorize_callback` 
        (which is recommended by praw).

    Make sure you provide same `scopes` and `redirect_url` which you used
    with `PrawOAuth2Server`.
    """

    def __init__(self, reddit_client, app_key,
                 app_secret, access_token,
                 refresh_token, scopes=SCOPES,
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
        self.reddit_client.set_oauth_app_info(client_id=self.app_key,
                                              client_secret=self.app_secret,
                                              redirect_uri=self.redirect_url)

    def _set_access_credentials(self):
        self.reddit_client.set_access_credentials(
            scope=self.scopes, access_token=self.access_token,
            refresh_token=self.refresh_token)
        self._set_validity()

    def _set_access_credentials_first_time(self):
        try:
            self._set_access_credentials()
        except praw.errors.OAuthInvalidToken:
            self.refresh()

    def _get_refresh_access(self):
        return self.reddit_client.refresh_access_information(
            refresh_token=self.refresh_token)

    def refresh(self, force=False):
        """Refreshes the `access_token` and sets the praw instance `reddit_client`
        with a valid one.

        :param force: Boolean. Refresh will be done only when last refresh was
            done before `EXPIRY_DURATION`, which is 3500 seconds. However
            passing `force` will overrides this and refresh operation will be
            done everytime.
        """
        if self._is_token_expired() or force:
            tokens = self._get_refresh_access()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            self._set_access_credentials()

    def get_access_codes(self):
        """Returns the `access_token` and `refresh_token`.

        :returns: A dictionary containing `access_token` and `refresh_token`.
        """
        return {'access_token': self.access_token,
                'refresh_token': self.refresh_token}
