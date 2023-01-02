# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx学习手册'
copyright = '2022, LiJiapeng'
author = '李嘉鹏'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx.ext.autodoc', 'sphinx.ext.graphviz']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output -------------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    'papersize':'a4paper',
    'pointsize':'11pt',
    'preamble': r'''
    \usepackage{ctex}
    ''',
}

# -- Options for apidoc output -------------------------------------------------

import os
import sys
sys.path.append(os.path.abspath("pymodule"))

# -- Options for graphviz output -------------------------------------------------

graphviz_output_format = 'svg'