#!/usr/bin/env python

import webbrowser

import tornado.ioloop
import tornado.web

__all__ = ['PrawOAuth2Server']

application = None
REDIRECT_URL = 'http://127.0.0.1:65010/authorize_callback'
SCOPES = ['identity', 'read']
REFRESHABLE = True
CODE = None


class AuthorizationHandler(tornado.web.RequestHandler):

    def get(self):
        global CODE
        CODE = self.get_argument('code')
        self.write('successful (:')
        tornado.ioloop.IOLoop.current().stop()


class PrawOAuth2Server:

    """Creates an instance of `PrawOAuth2Server` which is responsible for
    getting `access_token` and `refresh_token` given valid `app_key` and
    `app_secret`. This is meant to be run once only.

    :param reddit_client: An Instance of praw
    :param app_key: App Secret (or also known as Client Id) of your
        app. Find them here: https://www.reddit.com/prefs/apps/
    :param app_secret: App Key (or also known as Client Secret) of your
        app. Find them here: https://www.reddit.com/prefs/apps/
    :param state: Some unique string which represents your client. You
        could use `user_agent` which you used when creating the praw
        instance.
    :param scopes: List of scopes for OAuth. Default is `['identity']`.
        https://praw.readthedocs.org/en/latest/pages/oauth.html#oauth-scopes
    :param redirect_url: Redirect URL used in authorization process using
        `PrawOAuth2Server`. Default is `http://127.0.0.1:9999/authorize_callback`
        (which is recommended by praw).
    :param refreshable: Boolean. Specifies whether you want `access_token`
        to be refreshable or not. If it is set to `False` then you have to
        use `PrawOAuth2Server` again to generate new `access_token`.
        Default is `True`.
    """

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
        self._set_up_tornado()

    def _set_app_info(self):
        self.reddit_client.set_oauth_app_info(client_id=self.app_key,
                                              client_secret=self.app_secret,
                                              redirect_uri=self.redirect_url)

    def _set_up_tornado(self):
        global application
        application = tornado.web.Application([
            (r'/authorize_callback', AuthorizationHandler),
        ])
        application.listen(65010)

    def _get_auth_url(self):
        return self.reddit_client.get_authorize_url(
            state=self.state, scope=self.scopes,
            refreshable=self.refreshable)

    def start(self):
        """Starts the `PrawOAuth2Server` server. It will open the default
        web browser and it will take you to Reddit's authorization page,
        asking you to authorize your Reddit account(or account of the bot's)
        with your app(or bot script). Once authorized successfully, it will
        show `successful` message in web browser.
        """
        global CODE
        url = self._get_auth_url()
        webbrowser.open(url)
        tornado.ioloop.IOLoop.current().start()
        self.code = CODE

    def get_access_codes(self):
        """Returns the `access_token` and `refresh_token`. Obviously, this
        method should be called after `start`.

        :returns: A dictionary containing `access_token` and `refresh_token`.
        """
        return self.reddit_client.get_access_information(code=self.code)
