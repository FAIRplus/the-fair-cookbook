from os import path
import yaml
from yaml.loader import SafeLoader
import json
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.util import logging

logger = logging.getLogger(__name__)
logger.info('Hello, this is "rdmkit_panel" extension!')


class RDMkitPanel(Directive):
    has_content = False
    option_spec = {
        "inline": directives.unchanged_required
    }

    def _create_content(self):
        self.parse_yaml()
        content = []
        RDMkit_block = self.get_rdmkit_html()
        if RDMkit_block:
            if not 'inline' in self.options:
                content.append('<div class="card w-100 border-2 col-md-4 p-0 docutils">')
            content.extend([
                    '<div class="card-header bg-primary pa_dark docutils text-center">',
                            '<img alt="RDMkit logo" height="40px" src="/_static/images/logo/RDMkit_logo.svg">',
                    '</div>',
                    '<div class="card-body docutils">',
                        '<p class="mb-0">Learn more about:</p>',
                        self.get_rdmkit_html(),
                    '</div>'
            ])
            if not 'inline' in self.options:
                content.append('</div>')
        return content

    def get_rdmkit_html(self):
        """
        Creates the rdmkit html snippets for each link
        :return str: 
        """
        if self.fcb_rdmkit_links.items():
            output = '<ul>'
            for rdmkit_title, rdmkit_filename in self.fcb_rdmkit_links.items():
                output += f'<li><a href="https://rdmkit.elixir-europe.org/{rdmkit_filename}" target="_blank">{rdmkit_title}</a></li>'
            output += '</ul>'
            return output


    def parse_yaml(self):

        here_path = path.dirname(path.abspath(__file__))
        yaml_path = path.join(here_path, '..', '_static', 'faircookbook_rdmkit_mapping.yml')
        json_path = path.join(here_path, '..', '_static', 'recipes.json')

        with open(yaml_path, 'r') as f:
            yaml_data = yaml.load(f, Loader=SafeLoader)
        with open(json_path, 'r') as f:
            json_data = json.load(f)

        latest_recipe = list(json_data)[-1]
        fcb_id = json_data[latest_recipe]['identifier']

        self.fcb_rdmkit_links = {}

        for rdmkit_page in yaml_data:
            for fcb_link in rdmkit_page['links']:
                if fcb_link['fcb_id'] == fcb_id:
                    self.fcb_rdmkit_links[rdmkit_page['rdmkit_title']] = rdmkit_page['rdmkit_filename']

    def _parse_content_into_nodes(self, new_content):
        if len(self.content) > 0:
            common_filename = self.content.items[0][0]
            for index, (filename, linenumber) in enumerate(self.content.items):
                assert filename == common_filename, "Unexpected behavior of sphinx."
                assert linenumber == index        , "Unexpected behavior of sphinx."
        else:
            common_filename = None
        self.content.data = []
        self.content.items = []
        for idx, line in enumerate(new_content):
            self.content.data.append(line)
            self.content.items.append((common_filename, idx))
        node = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, node)
        return node.children

    def run(self):
        new_content = self._create_content()
        new_nodes = self._parse_content_into_nodes(new_content)
        return new_nodes

def setup(app):
    app.setup_extension("sphinx_panels")
    app.add_directive("rdmkit_panel", RDMkitPanel)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


escape_character_to_make_a_string_red_start = "\033[91m"
escape_character_to_make_a_string_red_end   = "\033[0m"


def _make_string_red(string):
    return escape_character_to_make_a_string_red_start + string + escape_character_to_make_a_string_red_end
