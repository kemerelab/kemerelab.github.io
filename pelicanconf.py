AUTHOR = 'Caleb Kemere'
SITENAME = 'KemereLab'
SITEURL = ""

THEME = "theme"

STATIC_PATHS = ['images', 'pubs']

PATH = "content"
RELATIVE_URLS = True

TIMEZONE = 'America/Chicago'

PLUGINS = ["data_files"]
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'codehilite',
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.legacy_attrs': {},
    }

}

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = []

