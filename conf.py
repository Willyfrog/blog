# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'Willyfrog'
WWW_ROOT = 'http://blog.willyfrog.es/'

AUTHOR = 'Willyfrog'
EMAIL = 'nadaird@willyfrog.es'

#FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1',]
FILTERS = ['reStructuredText+Pygments', 'hyphenate', 'h1',]
METASTYLE = 'native'
VIEWS = {
    '/': {'filters': 'summarize', 'view': 'index',
          'pagination': '/page/:num/'},

    '/:year/:slug/': {'views': ['entry', 'draft']},

    '/tag/:name/': {'filters': 'summarize', 'view':'tag',
                    'pagination': '/tag/:name/:num/'},

    '/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    # # per tag Atom or RSS feed. Just uncomment to generate them.
    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/articles/': {'view': 'archive', 'template': 'articles.html'},

    '/sitemap.xml': {'view': 'sitemap'},

    # # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    '/:slug/': {'view': 'page'},

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags},

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'},

    # # translations!
    # '/:year/:slug/:lang/': {'view': 'translation'},
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%Y-%mo-%d, %H:%M'

#CONTENT_EXTENSION = ".md"
#CONTENT_IGNORE = ["*.md~", ".#*.md"]

CONTENT_EXTENSION = ".rst"
CONTENT_IGNORE = ["*.rst~", ".#*.rst", ".#*.css" ]

DEPLOYMENT = {
    'willyfrog': 'rsync -vzr -e ssh --delete $OUTPUT_DIR vfrog:/var/www/willyfrog/blog/'
    }
