## Tips and more

To see `prawoauth2` in action check the [`examples` directory](https://github.com/avinassh/prawoauth2/tree/master/examples) or [Reddit Goodreads Bot](https://github.com/avinassh/Reddit-GoodReads-Bot).

To see what all class methods are available or any advanced usage, check `API Reference`.

### How to save configuration and settings

`prawoauth2` does not force developer to save tokens/settings in specific format or location. It gives full freedom to the developer to handle them and save them wherever he wishes. So you are free to save them in plain text file, ini, json, yaml or python. `prawoauth2` also does not save the refreshed tokens anywhere, so it is developer's responsibility to save the new access tokens. I prefer saving all the tokens in a file called `tokens.py` and bot related settings in `settings.py`. Both of these files will stay in the same directory where bot is run.

    # tokens.py
    app_key = '3...Y'
    app_secret = 'L...T'
    access_token = 'E...N'
    refresh_token = 'F...R'

    # settings.py
    scopes = ['identity', 'submit', 'read']
    user_agent = 'Super Reddit Bot (by /u/avinassh)'

However you are free to save them anywhere you want, `/opt`, `/etc/prawoauth2` or `~/`.


### Keeping track of refreshed access tokens

`prawoauth2` handles getting new `access_token` whenever it is expired. Usually, 99% of the times you don't need to keep track of new `access_token`. As long as you have valid `refresh_token`, the script will run fine since `prawoauth2` will handle everything. However in case you want to get the new codes, you can use `PrawOAuth2Mini.get_access_codes` method:

    # `oauth_helper` is an instance of `PrawOAuth2Mini`
    oauth_helper.get_access_codes()
    # returns a dictionary
    # {'access_token': 'E...N', 'refresh_token': 'F...R'}


### How to handle sensitive information

I have mentioned earlier that you should never make `app_key`, `app_secret`, `access_token` and `refresh_token` public. These are like credentials of your (or your bot's) Reddit account. So you should keep them super secret. 

There are two ways to handle them in code. You can save them in a python file, however you have to make sure that you are not adding that file to version control. For example, if you are using Git, then make sure you [gitignore](http://git-scm.com/docs/gitignore) the said file. 

    # .gitignore
    tokens.py

Another way would be to use [Environment variables](https://en.wikipedia.org/wiki/Environment_variable). Once you have retrieved the tokens, set the environment variables by running following in your terminal:

    $export APP_KEY=3...Y
    $export APP_SECRET=L...T
    $export ACCESS_TOKEN=E...N
    $export REFRESH_TOKEN=F...R

And make use of these in your script:

    # tokens.py
    import os

    app_key = os.getenv('APP_KEY')
    app_secret = os.getenv('APP_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    refresh_token = os.getenv('REFRESH_TOKEN')


### When to use `refresh`

The `access_token` expires for every 60 minutes (this is set by Reddit), so you can do `refresh` operation to get the new tokens. You don't really need to keep track of expiry time, when the tokens are expired, `OAuthInvalidToken` exception will be thrown. Catch it and do `refresh`. 

    try:
        some_reddit_related_op()
    except praw.errors.OAuthInvalidToken:
        # `oauth_helper` is an instance of `PrawOAuth2Mini`
        oauth_helper.refresh()

On the other hand, you can call the `refresh` before every operation, however it will get you new tokens only when old ones are about to expire.

    try:
        oauth_helper.refresh()
        some_reddit_related_op()
    except praw.errors.OAuthInvalidToken:
        oauth_helper.refresh()

If you want to refresh tokens even though if they are not expired, then pass parameter `force` to `True`, this prevents `prawoauth2` to check if they are expired or not:

    oauth_helper.refresh(force=True)


### Keeping the bot running always

As explained in earlier section `prawoauth2` has a mechanism to the refresh access token whenever it is expired, so that your bot is always healthy, functional and running. However it is also important to make sure that your bot is always running, whether some exception occurs in middle of operation or your machine/VPS/AWS instance reboots. I recommend you to use [`supervisord`](http://supervisord.org/). `supervisord` will start your bot script whenever your machine is starts, it restarts the bot in case if bot exits due to error. It will also help you maintain logs.

Following is a [sample `supervisord` config](https://github.com/avinassh/Reddit-GoodReads-Bot/blob/master/supervisor.conf) file for a Reddit bot:

    [program:goodreads_reddit_bot]
    command=/usr/bin/python3 /opt/goodreads_bot/main.py
    directory=/opt/goodreads_bot/
    stdout_logfile=/opt/goodreads_bot/log/stdout.log
    stderr_logfile=/opt/goodreads_bot/log/stderr.log
    redirect_stderr=true
    stdout_logfile_maxbytes=1MB
    stdout_logfile_backups=10
    stderr_logfile_maxbytes=1MB
    autostart=true
    autorestart=true