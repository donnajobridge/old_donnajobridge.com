#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'donna j bridge'
SITENAME = 'Donna J. Bridge, Ph.D.'
SITEURL = ''

STATIC_PATHS = ['images', 'pdfs', 'articles']
ARTICLE_PATHS = ['articles']
PATH = 'content/'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'theme'


MENUITEMS = (
    ('about', '/pages/about.html'),
    ('contact', '/pages/contact.html'),
    ('friends', '/pages/friends.html')
    )
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True

# Blogroll
SOCIAL = (('email', 'donnajb@gmail.com'),
    ('twitter', 'https://twitter.com/donnajobridge'),
    ('linkedin', 'https://br.linkedin.com/in/donna-bridge'),
    ('github', 'https://github.com/donnajobridge'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
BIO = "Cognitive Neuroscientist"
PROFILE_IMAGE = "donna.jpg"

DISQUS_SITENAME = "donnajobridge"

PLUGINS = ['pelican_gist']
