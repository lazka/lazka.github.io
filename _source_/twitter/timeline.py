#-*- coding:utf-8 -*-

from docutils import nodes

from docutils.parsers import rst


class timeline(nodes.General, nodes.Element):
    pass



def visit(self, node):

    tag = u'''<a class="twitter-timeline" href="https://twitter.com/twitterapi" data-widget-id="{0}">
    Tweets by @twitterapi
    </a>'''.format(node.widget_id)

    self.body.append(tag)



def depart(self, node):
    pass



class TimelineDirective(rst.Directive):

    name = 'timeline'
    node_class = timeline

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}


    def run(self):

        node = self.node_class()

        node.widget_id = self.arguments[0]

        return [node]

