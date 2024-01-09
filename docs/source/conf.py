# Configuration file for the Sphinx documentation builder.

import datetime

# -- Project information

project = 'MotoSuiveur® Solutions documentation'
year = datetime.datetime.now().year
copyright = f'{year}, SIGUREN technologies Ltd.'
author = 'SIGUREN technologies Ltd.'

master_doc = "index"
version = '0.1.1'
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
#    'piccolo_theme',
    'sphinx_material',
    'sphinx_tags',
    'sphinx_design',
]


tags_create_tags = True

tags_extension = ["rst", "ipynb"]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']


#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

#numfig = True

# -- Options for HTML output

html_theme = 'sphinx_material'
#html_theme = 'piccolo_theme'
#html_theme = 'sphinx_material'

# -- Options for EPUB output
#epub_show_urls = 'footnote'

html_logo = '_img/Peter/siguren_logo_white.png'

# The name of an image file (within the static path) to use as favicon of the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
#html_favicon = os.path.join(html_theme_path[0], html_theme, 'static', 'img', 'favicon.ico')

#html_favicon = '_img/favicon.ico'

html_theme_options = {

#    "html_minify": False,
#    "html_prettify": True,
#    "css_minify": True,
    "logo_icon": "&#xe869",
#    "repo_type": "github",
    "color_primary": "2439bb",
    "color_accent": "red",
    "theme_color": "2439bb",
    "master_doc": False,
    'nav_title': 'MotoSuiveur® Solutions User Documentation',
    "heroes": {
        "index": "A fail-safety solution for your most demanding hoists.",
        "troubleshooting/index": "Get out of tight situations.",
    },
    #"version_dropdown": True,
    #"version_json": "_static/versions.json",
    #"version_info": {
    #    "Release": "https://bashtage.github.io/sphinx-material/",
    #    "Development": "https://bashtage.github.io/sphinx-material/devel/",
    #    "Release (rel)": "/sphinx-material/",
    #    "Development (rel)": "/sphinx-material/devel/",
    #},
#    "table_classes": ["plain"],

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,

}

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

#latex_elements = {
#    'figure_align':'H',
#}

#hoverxref_auto_ref = True

#hoverxref_role_types = {
#    'hoverxref' : 'modal',
#    'ref' : 'tooltip',
#}