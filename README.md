# prawoauth2

[![version](https://img.shields.io/pypi/v/prawoauth2.svg)](https://pypi.python.org/pypi/prawoauth2/)
[![supported](https://img.shields.io/pypi/pyversions/prawoauth2.svg)](https://pypi.python.org/pypi/prawoauth2/)
![license](https://img.shields.io/pypi/l/prawoauth2.svg)

`prawoauth2` is a helper library which makes writing Reddit bots/apps using OAuth2 super easy and simple.

## Installation

    pip install prawoauth2


## Bots using `prawoauth2`

- [Goodreads Bot](https://github.com/avinassh/Reddit-GoodReads-Bot)
- [Samacharbot2](https://github.com/HunkDivine/samacharbot2)

Feel free to fork and add link to your bot/project.

## LICENSE
The mighty MIT License. Please check `LICENSE` for info.

## Credits
SmBe19's [praw-OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util) and KissTheBlade_'s [script](https://github.com/x89/Shreddit/blob/master/get_secret.py) were very helpful. [These](https://www.reddit.com/r/redditdev/comments/3bit3y/prawoauth_how_do_i_make_an_automated_bot/) [Reddit](https://www.reddit.com/r/redditdev/comments/3bipzt/help_with_oauth/) [threads](https://www.reddit.com/r/redditdev/comments/197x36/using_oauth_to_send_valid_requests/) [also](https://www.reddit.com/r/redditdev/comments/2ujhkr/important_api_licensing_terms_clarified/) helped me lot.

First I started using `praw-OAuth2Util`, but I really did not like the way it was handling configurations and tokens. So, I [forked](https://github.com/avinassh/praw-OAuth2Util) and started using my fork. And later ended up writing my own. I am no longer maintaining the fork and I recommend using this library instead.
