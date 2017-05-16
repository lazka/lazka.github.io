#-*- coding:utf-8 -*-
u'''
embedding twitter's tweet in sphinx

usage:

First of all, add `sphinx_tweet_embed` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['sphinxcontrib.twitter']


then use `tweet` directive and `tw` role.

.. code-block:: rst

   .. tweet:: https://twitter.com/pypi/status/315214320826978305

   You can use display-thread flag to display replyes.

   .. tweet:: https://twitter.com/pypi/status/315214320826978305

   :tw:`@shomah4a`

   .. timeline:: 319830355039371264


finally, build your sphinx project.


.. code-block:: sh

   $ make html
'''

__version__ = '0.4.0'
__author__ = '@shomah4a'
__license__ = 'LGPLv3'



def setup(app):

    from . import tweet, user, timeline

    app.add_javascript('https://platform.twitter.com/widgets.js')

    app.add_node(tweet.tweet,
                 html=(tweet.visit, tweet.depart))
    app.add_directive('tweet', tweet.TweetDirective)

    app.add_node(timeline.timeline,
                 html=(timeline.visit, timeline.depart))
    app.add_directive('timeline', timeline.TimelineDirective)

    app.add_node(user.twnode,
                 html=(user.visit, user.depart))
    app.add_role('tw', user.tw_role)
