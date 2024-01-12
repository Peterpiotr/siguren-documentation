# Configuration file for the Sphinx documentation builder.

import datetime

# -- Project information

project = 'MotoSuiveur® Solutions documentation'
year = datetime.datetime.now().year
copyright = f'{year}, SIGUREN technologies Ltd.'
author = 'SIGUREN technologies Ltd.'

master_doc = "index"
version = '0.1.x'
release = version 


# -- General configuration


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'hoverxref.extension',
    'sphinx_tags',
    'sphinx_design',
    'sphinx_typo3_theme',
]


tags_create_tags = True

tags_extension = ["rst", "ipynb"]

templates_path = ['_templates']

#numfig = True

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_typo3_theme'

html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2439bb',
    # Toc options
    #'collapse_navigation': False,
    'sticky_navigation': True,
    #'navigation_depth': 4,
    #'includehidden': False,
    #'titles_only': False
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_logo = '_img/Peter/siguren_logo_white.png'

# The name of an image file (within the static path) to use as favicon of the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
#html_favicon = os.path.join(html_theme_path[0], html_theme, 'static', 'img', 'favicon.ico')

html_favicon = '_img/favicon.ico'

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_use_index = True

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    ('print.css', {'media': 'print'}) # modifies pdf output?? 
]

latex_elements = {
    'figure_align':'H',
}

hoverxref_auto_ref = True

hoverxref_role_types = {
    'hoverxref' : 'modal',
    'ref' : 'tooltip',
}