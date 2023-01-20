# Configuration file for the Sphinx documentation builder.

import datetime

# -- Project information

project = 'MotoSuiveur Solutions documentation'
year = datetime.datetime.now().year
copyright = f'{year}, SIGUREN technologies Ltd.'
author = 'SIGUREN technologies Ltd.'

master_doc = "index"
version = '0.1.0'
release = version

# -- General configuration


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
#    'piccolo_theme',
    'sphinx-material',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

numfig = True

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
#html_theme = 'piccolo_theme'
html_theme = 'sphinx-material'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_logo = 'siguren_logo_white.png'

html_theme_options = {
#    'banner_text': 'We just launched a newletter, <a href="https://mynewsletter.com/">please subscribe</a>!',
#    'banner_hiding': 'temporary'
# rtd theme options ---------------------------------------------------------------------------
#    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#    'analytics_anonymize_ip': False,
#    'logo_only': True,
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'vcs_pageview_mode': '',
#    'style_nav_header_background': '#2439bb',
    # Toc options
#    'collapse_navigation': True,
#    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
#    'titles_only': False
}

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    ('print.css', {'media': 'print'}) # modifies pdf output?? 
]