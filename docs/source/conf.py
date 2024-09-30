# Configuration file for the Sphinx documentation builder.

import datetime

# -- Project information

project = 'MotoSuiveur® Solutions documentation'
year = datetime.datetime.now().year
copyright = f'{year}, SIGUREN technologies technologies Ltd.'
author = 'SIGUREN technologies technologies Ltd.'

master_doc = 'index'
version = '0.1.3'               # gets overwritten by readthedocs when published online?
release = version 


# -- General configuration

#site_url = 'https://siguren-documentation.readthedocs.io/' 

extensions = [
    #'sphinx.ext.duration',          # Measures the duration of the Sphinx build process.
    #'sphinx.ext.doctest',           # Tests snippets in the documentation by running them as Python doctests.
    #'sphinx.ext.autodoc',           # Automatically generates documentation from docstrings in your Python source code files.
    #'sphinx.ext.autosummary',       # Generates summary tables for modules/classes/methods/etc. in your documentation.
    #'sphinx.ext.intersphinx',       # Links to the documentation of other projects, useful for cross-referencing external Sphinx documentation.
    #'sphinx.ext.autosectionlabel',  # Automatically creates labels for each section header.
    'hoverxref.extension',          # Adds tooltip previews for cross-references in the documentation.
    'sphinx_tags',                  # Adds support for conditional tags in documentation (enables content to be included/excluded based on tags).
    'sphinx_design',                # Provides additional design elements and layout options for Sphinx documentation.
    # 'sphinx_sitemap',             # Generates a sitemap.xml file for the documentation for SEO purposes.
    'sphinxcontrib.mermaid',
]



tags_create_tags = True

tags_extension = ["rst", "ipynb"]

templates_path = ['_templates']

hoverxref_roles = ['term']

#numfig = True

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'navigation_depth': 3,
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

html_logo = '_img/MS_by_sig_logo.png'

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
    #('print.css', {'media': 'print'}) # modifies pdf output?? 
]

# latex_engine = "xelatex"

latex_elements = {
    'figure_align':'H',
}

hoverxref_auto_ref = True

hoverxref_role_types = {
    'hoverxref' : 'modal',
    'ref' : 'tooltip',
}