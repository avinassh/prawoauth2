prawoauth2
==========

|version| |supported| |license|

``prawoauth2`` is a helper library which makes writing Reddit bots/apps
using OAuth2 super easy and simple.

Documentation
-------------

``prawoauth2`` comes with extensive documentation and is available on `Read The Docs <http://prawoauth2.readthedocs.org/>`__


Installation
------------

::

    pip install prawoauth2

Bots using ``prawoauth2``
-------------------------

-  `Goodreads Bot <https://github.com/avinassh/Reddit-GoodReads-Bot>`__
-  `Samacharbot2 <https://github.com/HunkDivine/samacharbot2>`__
-  `GfyBot <https://github.com/skylarmb/GfyBot>`__
-  `GiantBombSidebar <https://github.com/SDFortier/GiantBombSidebar>`__
-  `Not Max Trollbot <https://github.com/blendermf/not-max-trollbot>`__
-  `EnhanceImageBot <https://github.com/Sprunth/EnhanceImageBot-reddit>`__
-  `BB Reddit Automod <https://github.com/digitalmonarch/bb-reddit-automod>`__

Feel free to fork and add link to your bot/project.

LICENSE
-------

The mighty MIT License. Please check ``LICENSE`` for info.

Credits
-------

SmBe19's `praw-OAuth2Util <https://github.com/SmBe19/praw-OAuth2Util>`__
and KissTheBlade\_'s
`script <https://github.com/x89/Shreddit/blob/master/get_secret.py>`__
were very helpful.
`These <https://www.reddit.com/r/redditdev/comments/3bit3y/prawoauth_how_do_i_make_an_automated_bot/>`__
`Reddit <https://www.reddit.com/r/redditdev/comments/3bipzt/help_with_oauth/>`__
`threads <https://www.reddit.com/r/redditdev/comments/197x36/using_oauth_to_send_valid_requests/>`__
`also <https://www.reddit.com/r/redditdev/comments/2ujhkr/important_api_licensing_terms_clarified/>`__
helped me lot. Most of text in `Installation` is copied from `Python Requests <http://www.python-requests.org/en/latest/user/install/>`__. Github user `qevo <https://github.com/qevo>`__ has `helped <https://www.reddit.com/r/learnpython/comments/3en8ai/how_do_i_generate_documentation_for_my_library/cuvzxrh>`__ me generating docs.

First I started using ``praw-OAuth2Util``, but I really did not like the
way it was handling configurations and tokens. So, I
`forked <https://github.com/avinassh/praw-OAuth2Util>`__ and started
using my fork. And later ended up writing my own. I am no longer
maintaining the fork and I recommend using this library instead.

.. |version| image:: https://img.shields.io/pypi/v/prawoauth2.svg
   :target: https://pypi.python.org/pypi/prawoauth2/
.. |supported| image:: https://img.shields.io/pypi/pyversions/prawoauth2.svg
   :target: https://pypi.python.org/pypi/prawoauth2/
.. |license| image:: https://img.shields.io/pypi/l/prawoauth2.svg
