#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Benjamin Cogrel'
SITENAME = 'Benjamin Cogrel'
SITESUBTITLE = 'Contemporary automation'
#Not overloaded by the i18n extension
SITEROOTURL = 'https://blog.bcgl.fr' 
SITEURL = SITEROOTURL 

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ontop', 'http://ontop.inf.unibz.it/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/bcogrel'),
         ('github', 'https://github.com/bcogrel'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (
    ('English', '/'),
    ('Français', '/fr/'),
)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

TYPOGRIFY = True

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'


PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'fr': {
        'SITESUBTITLE': 'Automatisation contemporaine',
        'LINKS_WIDGET_NAME': 'Quelques liens',
        'SOCIAL_WIDGET_NAME': 'Comptes en ligne',
        'COPYRIGHT': '''Sauf mention contraire, le contenu de ce site est
        publié sous la <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">licence
        CC-BY-NC-SA</a>''',
        'DISCLAIMER': '''Les propos exprimés sur ce site le sont à titre
        personnel.'''
        }
    }



THEME = 'themes/plumage'
# Plumage specific 
COPYRIGHT = '''Unless contrary mentioned, the content of this site is published
under a <a
href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-BY-NC-SA license</a>'''
DISCLAIMER = '''This a personal site, all opinions expressed here are mine.'''
SOCIAL_WIDGET_NAME = 'Public accounts'
LINKS_WIDGET_NAME = 'Few links'
