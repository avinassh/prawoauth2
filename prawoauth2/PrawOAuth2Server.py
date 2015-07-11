#!/usr/bin/env python

import webbrowser

import tornado.ioloop
import tornado.web

__all__ = ['PrawOAuth2Server']

REDIRECT_URL = 'http://127.0.0.1:65010/authorize_callback'
SCOPES = ['identity']
REFRESHABLE = True
CODE = None


class AuthorizationHandler(tornado.web.RequestHandler):

    def get(self):
        global CODE
        CODE = self.get_argument('code')
        self.write('successful (:')
        tornado.ioloop.IOLoop.current().stop()


class PrawOAuth2Server:

    def __init__(self, reddit_client, app_key, app_secret,
                 state, redirect_url=REDIRECT_URL, scopes=SCOPES,
                 refreshable=REFRESHABLE):
        self.reddit_client = reddit_client
        self.app_key = app_key
        self.app_secret = app_secret
        self.state = state
        self.redirect_url = redirect_url
        self.scopes = set(scopes)
        self.refreshable = refreshable
        self.code = None

        self._set_app_info()

    def _set_app_info(self):
        self.reddit_client.set_oauth_app_info(client_id=self.app_key,
                                              client_secret=self.app_secret,
                                              redirect_uri=self.redirect_url)

    def _get_auth_url(self):
        return self.reddit_client.get_authorize_url(
            state=self.state, scope=self.scopes,
            refreshable=self.refreshable)

    def start(self):
        global CODE
        url = self._get_auth_url()
        webbrowser.open(url)
        tornado.ioloop.IOLoop.current().start()
        self.code = CODE

    def get_access_codes(self):
        return self.reddit_client.get_access_information(code=self.code)

application = tornado.web.Application([
    (r'/authorize_callback', AuthorizationHandler),
])
application.listen(65010)
