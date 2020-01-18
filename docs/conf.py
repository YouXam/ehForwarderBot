#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# EH Forwarder Bot documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 28 10:17:32 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from os import path

import sphinxcontrib.plantuml
from sphinx import addnodes
from typing import Sequence
from sphinx.locale import get_translation

sys.path.insert(0, os.path.abspath('..'))

__version__ = "0.0.0"

exec(open('../ehforwarderbot/__version__.py').read())
MESSAGE_CATALOG_NAME = "efb_docs_config"
_ = get_translation(MESSAGE_CATALOG_NAME)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosummary',
              'sphinx.ext.graphviz',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.intersphinx',
              'sphinx_autodoc_typehints',
              'sphinxcontrib.restbuilder',
              'sphinxcontrib.plantuml',
              'sphinx_search.extension']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'EH Forwarder Bot'
copyright = _('2016 — 2020 Eana Hufwe and the EH Forwarder Bot contributors')
author = _('Eana Hufwe, and the EH Forwarder Bot contributors')
docs_title = _('EH Forwarder Bot Documentation')
description = _('An extensible message tunneling chat bot framework.')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

version = ".".join(__version__.split(".")[:2])
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `to\do` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_static_path = ['_static']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
# html_theme = 'readable'
# html_logo = "_static/logo.png"
html_theme = 'alabaster'
html_sidebars = {
    'index': [
        'about_index.html',
        'navigation.html',
        'searchbox.html',
        'donate.html',
        'translate.html',
    ],
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
        'translate.html',
    ]
}
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'logo_text_align': 'left; font-size: 1.5em',
    'touch_icon': 'logo.png',
    'github_button': True,
    'github_type': 'star',
    'github_user': 'blueset',
    'github_repo': 'ehforwarderbot',
    'description': description,
    'donate_url': 'https://github.com/blueset/.github',
    'github_banner': "github_banner.svg",
    'show_related': True,
    'show_relbars': True,
    'extra_nav_links': {
        _('Community wiki'): 'https://efb.1a23.studio/wiki',
        _('Modules repository'): 'https://efb-modules.1a23.studio/',
    }
}

# import sphinx_py3doc_enhanced_theme
# html_theme = "sphinx_py3doc_enhanced_theme"
# html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

# sys.path.append(os.path.abspath('_themes'))
# html_theme_path = ['_themes']
# html_theme = 'kr'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ehForwarderBotDoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ehForwarderBot.tex', docs_title, author, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ehforwarderbot', docs_title, author, 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ehForwarderBot', docs_title,
     author, 'ehForwarderBot', description,
     'Miscellaneous'),
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Sphinx-intl settings
locale_dirs = ['locale/']
gettext_compact = False
gettext_additional_targets = ['literal-block', 'image']

conversion = {
    'az': 'az_AZ', 'es': 'es_VE', 'id': 'id_ID',
    'it': 'it_IT', 'ja': 'ja_JP', 'ms': 'ms_MY',
    'ro': 'ro_RO', 'tr': 'tr_TR', 'zh': 'zh_CN',
    'en': 'en_US'
}

# # Locale fallback settings
# def locale_fallback_decorator(fun):
#
#     def wrapper(self, **kwargs):
#         self.config.language = conversion.get(self.config.language, self.config.language)
#         return fun(self, **kwargs)
#     return wrapper
#
#
# sphinx.application.Sphinx._init_i18n = locale_fallback_decorator(sphinx.application.Sphinx._init_i18n)

autosectionlabel_prefix_document = True

# This config value contains the locations and names of other projects that
# should be linked to in this documentation.
#
# Relative local paths for target locations are taken as relative to the base
# of the built documentation, while relative local paths for inventory
# locations are taken as relative to the source directory.
#
# When fetching remote inventory files, proxy settings will be read from the
# $HTTP_PROXY environment variable.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

graphviz_output_format = "svg"
plantuml_output_format = "svg"
plantuml_latex_output_format = "pdf"

_plantuml_node = sphinxcontrib.plantuml.plantuml


def preserve_original_messages(self) -> None:
    """Preserve original translatable messages."""
    self.original_uml = self['uml']
    self.original_caption = self.get('caption', None)


def apply_translated_message(self, original_message: str, translated_message: str) -> None:
    """Apply translated message."""
    if self.original_uml == original_message:
        self['uml'] = translated_message
    elif self.original_caption == original_message:
        self['caption'] = translated_message


def extract_original_messages(self) -> Sequence[str]:
    """Extract translation messages.

    :returns: list of extracted messages or messages generator
    """
    l = (self['uml'],)
    if 'caption' in self:
        l += (self['caption'],)
    return l


sphinxcontrib.plantuml.plantuml.__bases__ = (addnodes.translatable,) + sphinxcontrib.plantuml.plantuml.__bases__
sphinxcontrib.plantuml.plantuml.preserve_original_messages = preserve_original_messages
sphinxcontrib.plantuml.plantuml.apply_translated_message = apply_translated_message
sphinxcontrib.plantuml.plantuml.extract_original_messages = extract_original_messages


def setup(self):
    package_dir = path.abspath(path.dirname(__file__))
    locale_dir = os.path.join(package_dir, 'locale')
    self.add_message_catalog(MESSAGE_CATALOG_NAME, locale_dir)
    self.add_message_catalog("sphinx", locale_dir)
    print("==== loaded message catalog")
    self.config.language = conversion.get(self.config.language, self.config.language)
    self.config.overrides['language'] = conversion.get(self.config.overrides.get('language', None),
                                                       self.config.overrides.get('language', None))
