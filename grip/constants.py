# The common titles and supported extensions,
# as defined by https://github.com/github/markup
SUPPORTED_TITLES = ['README', 'Home']
SUPPORTED_EXTENSIONS = ['.md', '.markdown']


# The default filenames when no file is provided
DEFAULT_FILENAMES = [title + ext
                     for title in SUPPORTED_TITLES
                     for ext in SUPPORTED_EXTENSIONS]


# The default directory to load Grip settings from
DEFAULT_GRIPHOME = '~/.grip'


# The default URL of the Grip server
DEFAULT_GRIPURL = '/__/grip'


STYLE_URLS_SOURCE = 'https://github.com/joeyespo/grip'
STYLE_URLS_RE = (
    '<link.+href=[\'"]?([^\'" >]+)[\'"]?.+media=[\'"]?(?:screen|all)[\'"]?.'
    '+rel=[\'"]?stylesheet[\'"]?.+/>')
STYLE_ASSET_URLS_RE = (
    'url\([\'"]?(/static/fonts/octicons/[^\'" \)]+)[\'"]?\)')
STYLE_ASSET_URLS_SUB_FORMAT = 'url("{}\\1")'
STYLE_ASSET_URLS_INLINE_FORMAT = (
    'url\([\'"]?((?:/static|{})/[^\'" \)]+)[\'"]?\)')
