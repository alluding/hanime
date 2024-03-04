project = 'hanime'
author = 'alluding'
version = '2.0.0'
copyright = f'Copyright © {author}'

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.linkcode",
    "myst_parser",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 3
# thanks pomice (cloudwithax) :]


html_theme = 'furo'
html_static_path = ['_static']

source_suffix = '.md'
master_doc = 'index'
