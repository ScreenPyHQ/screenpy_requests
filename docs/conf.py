# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("./ext"))
sys.path.insert(0, os.path.abspath("../"))

from screenpy_requests.__version__ import __version__, __author__, __copyright__

autodoc_mock_imports = ["selenium", "screenpy", "screenpy_pyotp"]


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "screenpy_requests"
copyright = __copyright__
author = __author__
release = __version__


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "autodoc_skip_protocols",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

rst_prolog = """.. External references
.. |request| replace:: `Session.request <https://requests.readthedocs.io/en/master/api/#requests.Session.request>`__
.. |Requests| replace:: `Requests <https://requests.readthedocs.io/en/master/>`__
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = []

autodoc_member_order = "bysource"
add_module_names = False


# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "screenpy": ("https://screenpy-docs.readthedocs.io/en/latest/", None),
    "requests": ("https://docs.python-requests.org/en/latest/", None),
}
