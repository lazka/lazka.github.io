extensions = []
source_suffix = '.rst'
master_doc = 'index'
project = u'Home'
copyright = u''
version = '0.1'
release = '0.1'
exclude_patterns = ['.venv']
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_theme_path = ['.']
html_static_path = ['static']

html_sidebars = {
   '**': [
       'about.html', 'navigation.html',
   ]
}

html_theme_options = {
    'github_button': False,
    'show_powered_by': False,
    'extra_nav_links': {
        'Search': 'search.html',
    }
}

html_show_sourcelink = False
html_copy_source = False
html_title = "lazka.github.io"

extensions = []
