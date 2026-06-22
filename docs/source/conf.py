# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Balai Hub Mahjong Handbook'
copyright = '2026, Balai Hub'
author = 'Balai Hub'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'style_nav_header_background': '#008080',  # Dark green color
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_elements = {
    'extraclassoptions': 'openany,oneside',
    'classoptions': 'openany,oneside',
    'preamble': r'''
\let\cleardoublepage\clearpage
''',
}