# Configuration file for the Sphinx documentation builder.

project = 'ancestry sign in problems'
author = 'ancestry sign in problems'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

language = 'en'

html_title = "ancestry sign in problems"

# Sitemap
html_baseurl = "https://ancestry-sign-in-problems-ancestry-sign-in-problems.readthedocs-hosted.com/en/latest/"
sitemap_url_scheme = "{link}"

