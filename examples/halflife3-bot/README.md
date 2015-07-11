#Half Life 3

This bot replies to anyone who mentions `Half Life` in their comment, also prints on the screen for the feedback. 

## Usage

Set your OS environment variables `HL3_APP_KEY` and `HL3_APP_SECRET`:

    $export HL3_APP_KEY=D...w HL3_APP_SECRET=F...s

Run the `onetime.py` and it will print `tokens` on the screen. Remember, this needs a Web Browser access, so you cannot run this on a headless server. Run this thing locally only.

    $python onetime.py
    {u'access_token': u'2...o', u'scope': set([u'submit', u'identity']), u'refresh_token': u'2...c'}

Now set the OS environment variables with these tokens too, `HL3_ACCESS_TOKEN` and `HL3_REFRESH_TOKEN`:

    $export HL3_ACCESS_TOKEN=2...I HL3_REFRESH_TOKEN=2...U

Then you can run the `bot.py`. Now you have got the `access_token`, you can `bot.py` in your server/AWS/Openshift/<anything headless>, without any hiccups. Once `access_token` and other credentials are at place and correct, this will run forever.

    $python bot.py
    shit, someone mentioned Half Life 3 again :@

## Caution
Never ever make your `app_secret`, `access_token` and `refresh_token` public and never commit them to git.