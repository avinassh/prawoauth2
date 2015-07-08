#Half Life 3

This bot replies to anyone who mentions `Half Life` in their comment, also prints on the screen for the feedback. 

## Usage

Edit the `tokens.py` with your `app_key` and `app_secret`. Run the `onetime.py` and it will print `tokens` on the screen. Copy them and edit `tokens.py`.

Remember, this needs a Web Browser access, so you cannot run this on a headless server. Run this thing locally.

    $python onetime.py
    {u'access_token': u'2...o', u'scope': set([u'submit', u'identity']), u'refresh_token': u'2...c'}

Then you can run the `bot.py`. Now you have got the `access_token`, you can `bot.py` in your server/AWS/Openshift/<anything headless>, without any hiccups. Once `access_token` and other credentials are at place and correct, this will run forever.

    $python bot.py
    shit, someone mentioned Half Life 3 again :@

## Caution
Never ever make your `app_secret`, `access_token` and `refresh_token` public and never commit them to git.