from os import path
import yaml
from yaml.loader import SafeLoader
import json
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import sphinx.errors
import sphinx_panels.panels
from sphinx.util import logging

logger = logging.getLogger(__name__)
logger.info('Hello, this is "rdmkit_panel" extension!')


class RDMkitPanel(Directive):
    has_content = False

    def _create_content(self):
        self.parse_yaml()
        content = []
        content.extend([
            self.get_rdmkit_html()
        ])
        return content

    def get_rdmkit_html(self):
        """
        Creates the rdmkit html snippets for each link
        :return str: a dictionary with as keys the RDMkit page names and as value the url
        """

        
        for rdmkit_title, rdmkit_filename in self.fcb_rdmkit_links.items():
            output = '<ul>'
            output += f'<li><a href="https://rdmkit.elixir-europe.org/{rdmkit_filename}">{rdmkit_title}</a></li>'
            output += '</ul>'
            return output


    def parse_yaml(self):

        here_path = path.dirname(path.abspath(__file__))
        yaml_path = path.join(here_path, '..', '_static','faircookbook_rdmkit_mapping.yml')
        json_path = path.join(here_path, '..', '_static', 'recipes.json')

        with open(yaml_path, 'r') as f:
            yaml_data = yaml.load(f, Loader=SafeLoader)
        with open(json_path, 'r') as f:
            json_data = json.load(f)

        latest_recipe = list(json_data)[-1]
        fcb_id = latest_recipe['identifier']

        self.fcb_rdmkit_links = {}

        for rdmkit_page in yaml_data:
            for fcb_link in rdmkit_page:
                if fcb_link['fcb_id'] == fcb_id:
                    self.fcb_rdmkit_links[rdmkit_page['rdmkit_title']] = rdmkit_page['rdmkit_filename']


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
