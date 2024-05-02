AUTHOR = 'Caleb Kemere'
SITENAME = 'KemereLab'
SITEURL = ""

THEME = "theme"
STYLESHEET_URL = "/theme/css/pico.blue.css"

STATIC_PATHS = ['images', 'pubs']

PATH = "content"
RELATIVE_URLS = True

TIMEZONE = 'America/Chicago'

# PLUGINS = ["data_files"]

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = []

