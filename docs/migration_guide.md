## Migration from HTTP to OAuth2

If you have an existing Reddit bot and if you wish to migrate to OAuth2, follow the simple steps.

1. Stop using `praw.login`. Your current code probably uses Reddit account (your's or your bot's) username and password with `praw.login` and you have to remove that. With OAuth2, there should NO references to Reddit username and password in your code:

        reddit_client = praw.Reddit(user_agent=user_agent)
        reddit_client.login(reddit_username, reddit_password)

2. Figure out what all `scopes` you need. Scopes specify what all permissions your app (or bot script) needs from user's Reddit account(or your bot account), like read private messages, spend gold credits etc. You can read about different scopes on praw's [official documentation](https://praw.readthedocs.org/en/stable/pages/oauth.html#oauth-scopes). For example, if your bot replies to comments and also responds to private messages, then it will need atleast these scopes:

        scopes = ['identity', 'read', 'submit', 'privatemessages']

3. Next you need [register](https://www.reddit.com/prefs/apps/) your app/script/bot in Reddit. Once done, you will have `app_key` and `app_secret`. For more detailed instruction refer to [`User Guide`](http://prawoauth2.readthedocs.org/usage_guide.html).

4. Build `onetime.py` script. As name suggests, you need to run this script only once for the first time. You should run this script locally, on your computer. Refer to [Running PrawOAuth2Server](http://prawoauth2.readthedocs.org/usage_guide.html#running-prawoauth2server) in `User Guide`. Once done, you will get `access_token` and `refreh_token`. 

5. Now use `app_key`, `app_secret`, `app_key` and `app_secret` in your existing code to create a new instance of `PrawOAuth2Mini`. Refer to [Using PrawOAuth2Mini](http://prawoauth2.readthedocs.org/usage_guide.html#using-prawoauth2mini) in `User Guide`.

        reddit_client = praw.Reddit(user_agent=user_agent)
        oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,
                                      app_secret=app_secret,
                                      access_token=access_token,
                                      refresh_token=refresh_token,
                                      scopes=scopes)


That's all! Now rest of your code would require no changes and it will work as usual.