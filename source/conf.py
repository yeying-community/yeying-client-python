# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'yeying-client-python'
copyright = '2025, yeying'
author = 'yeying'

import os
import sys
sys.path.insert(0, os.path.abspath('../yeying'))  # 指向代码目录

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # 自动提取注释
    'sphinx.ext.napoleon'    # 支持Google/Numpy风格注释
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # 使用ReadTheDocs主题
html_static_path = ['_static']
