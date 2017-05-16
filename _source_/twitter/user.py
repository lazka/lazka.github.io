#-*- coding:utf-8 -*-

import re

from docutils import nodes

from . import errors



PLAIN = r'\@?[0-9a-zA-Z_]+'
PLAIN_FORMAT = re.compile(PLAIN)
ID_AND_DISPLAY = re.compile(r'(?P<display>.+) <(?P<userid>{0})>'.format(PLAIN))



class twnode(nodes.Inline, nodes.Element):
    pass



def make_node(userid, display=None):

    node = twnode()

    node.userid = userid.lstrip('@')

    if display is None:
        node.display = '@' + node.userid
    else:
        node.display = display

    return node




def tw_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    m = ID_AND_DISPLAY.match(text)

    if m is not None:
        display = m.group('display')
        userid = m.group('userid')

        return [make_node(userid, display)], []

    m = PLAIN_FORMAT.match(text)

    if m is not None:

        return [make_node(m.group(0))], []


    raise errors.TwitterError(u'invalid format: {0}'.format(text))



def visit(self, node):

    html = u'''<a href="https://twitter.com/{0}">{1}</a>'''.format(node.userid, node.display)


    self.body.append(html)



def depart(self, node):
    pass
