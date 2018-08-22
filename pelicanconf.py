#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'donna j bridge'
SITENAME = 'memomorphosis'
SITESUBTITLE = 'how experience becomes memory'
SITEURL = ''

STATIC_PATHS = ['images', 'pdfs', 'articles']
ARTICLE_PATHS = ['articles']
PATH = 'content/'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'attila'
HEADER_COLOR = 'black'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Blogroll
SOCIAL = (('email', 'donnajb@gmail.com'),
    ('twitter', 'https://twitter.com/donnajobridge'),
    ('linkedin', 'https://br.linkedin.com/in/donna-bridge'),
    ('github', 'https://github.com/donnajobridge'))


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}


# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Comments
# DISQUS_SITENAME = "attilademo"

# Analytics
# GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = 'attila'

### Theme specific settings

HEADER_COVER = '../images/elephant.jpg'

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "../images/peak.png",
    "image": "assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "linkedin": "unavailable",
    "github": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

# Custom Header

# HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png',
# 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}
