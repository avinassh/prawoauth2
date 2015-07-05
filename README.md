# prawoauth2

`prawoauth2` is a helper library which makes writing Reddit bots/apps using OAuth2 super easy and simple.

## Installation

    pip install prawoauth2

## How, What and Why?

`prawoauth2` comes with two components, `PrawOAuth2Mini` and `PrawOAuth2Server`. `PrawOAuth2Server` authorizes your app/script with the Reddit account and gives you access token. `PrawOAuth2Mini` uses these tokens for all next transactions with Reddit. Remember, for a bot, you only need `access_token`.

Why it is written like that? If you are writing a bot and running it on a headless server, something like Amazon AWS or Openshift, you cannot authorize your script with the Reddit account, as it tries to open the browser for authorization. This is one time only operation(if you pass the parameter `permanent`). So, I decided to break this into two parts. Run the `PrawOAuth2Server` locally on your computer, get the `access_token` and save it somewhere. Later, `PrawOAuth2Mini` can make use of the `access_token` for further transactions. And it does not require browser at all, so that it can run in a headless server without any hiccups.

TLDR; `PrawOAuth2Server` meant to be run only once locally on your main machine to fetch the `access_token` and `PrawOAuth2Mini` later and for everything. 

## Usage
TODO

## LICENSE
The mighty MIT License. Please check `LICENSE` for info.

## Credits
SmBe19's [praw-OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util) and KissTheBlade_'s [script](https://github.com/x89/Shreddit/blob/master/get_secret.py) were very helpful. [These](https://www.reddit.com/r/redditdev/comments/3bit3y/prawoauth_how_do_i_make_an_automated_bot/) [Reddit](https://www.reddit.com/r/redditdev/comments/3bipzt/help_with_oauth/) [threads](https://www.reddit.com/r/redditdev/comments/197x36/using_oauth_to_send_valid_requests/) [also](https://www.reddit.com/r/redditdev/comments/2ujhkr/important_api_licensing_terms_clarified/) helped me lot.

First I started using `praw-OAuth2Util`, but I really did not like the way it was handling configurations and tokens. So, I [forked](https://github.com/avinassh/praw-OAuth2Util) and started using my fork. And later ended up writing my own. I am no longer maintaining the fork and I recommend using this library instead.