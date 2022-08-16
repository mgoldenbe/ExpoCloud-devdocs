# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

project = 'ExpoCloud'
copyright = '2022, Meir Goldenberg'
author = 'Meir Goldenberg'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx_paramlinks']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'myclassic'
html_static_path = ['_static']
autodoc_member_order = 'bysource'
autodoc_type_aliases = {'AgentAssignment': 'AgentAssignment'}
add_module_names = False
add_function_parentheses = False
autodoc_class_signature = "separated"

# include constructor
# https://stackoverflow.com/a/5599712/2725810
def skip(app, what, name, obj, would_skip, options):
    if name in ["__init__", "__str__", "__repr__", "__lt__", "__le__"]:
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)