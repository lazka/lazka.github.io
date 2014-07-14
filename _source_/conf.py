# -*- coding: utf-8 -*-

extensions = []
source_suffix = '.rst'
master_doc = 'index'
project = u'~'
copyright = u'2014, Christoph Reiter'
version = '0.1'
release = '0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_theme_path = ['.']

html_sidebars = {
   '**': [
       'about.html', 'navigation.html',
   ]
}

html_theme_options = {
   'github_button': False,
   'show_powered_by': False,
}

html_show_sourcelink = False
html_copy_source = False
