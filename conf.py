# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pages Playground'
copyright = '2023, Thomas Sasse'
author = 'Thomas Sasse'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = set()

extensions.add('sphinx.ext.autosectionlabel')
autosectionlabel_prefix_document = True     # Use prefixes for references to other files
                                            # Note: the first ":" always divides filepath and titlename
autosectionlabel_maxdepth = 0               # bound referable header level (e.g. to allow non-unique titles)
                                            # 0 -> all Titles are referable and must be unique!

extensions.add('sphinx.ext.intersphinx')
intersphinx_mapping = {
    'sphinx':       ('https://www.sphinx-doc.org/en/master', None)
}

templates_path = ['_templates']
exclude_patterns = ["_res"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = []
