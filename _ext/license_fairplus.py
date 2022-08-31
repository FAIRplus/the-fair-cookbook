from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import sphinx.errors
from sphinx.util import logging
from os.path import abspath, relpath
import os

from global_variables_fairplus import CONTROLLED_LICENSE_LIST

logger = logging.getLogger(__name__)
logger.info('Hello, this is "license_fairplus" extension!')


class LicenseFairplus(Directive):
    """
    This directive is supposed to work like this:

    ````{license_fairplus}
    CC-BY-4.0
    ````

    Failure to stick to this format will raise an Exception. 
    Allowed licenses can be found in global_variables_fairplus.py 
    """

    has_content = True
    final_argument_whitespace = False
    option_spec = {}

    def _parse_content(self):
        # cc_logos_path = "/Users/philippe/Documents/git/FAIRplus-org/the-fair-cookbook/_static/images/logo/"
        try:
            this_file = self.content.items[0][0]
            current_file = self.content.items[0][0]
            # current_file_path = os.path.abspath(os.getcwd())
            # relative_path = relpath(cc_logos_path, current_file)
            # print("RELATIVE:", current_file, "|", current_file_path,    "|", cc_logos_path, "|", relative_path )
        except:
            this_file = None

        assert len(self.content) == 1, sphinx.errors.ExtensionError(_make_string_red(
            f"The content of this directive must consist of one line exactly. This error occurred in file {this_file} ."
                ))
                
        line = self.content[0].strip()
        
        assert line in CONTROLLED_LICENSE_LIST, sphinx.errors.ExtensionError(_make_string_red(
                    f"The license '{line}' is not registered in the CONTROLLED_LICENSE_LIST."
                ))

        self.license = line

        return 

    def _create_content(self):
        content = [f"````{{dropdown}} **License**",
                   CONTROLLED_LICENSE_LIST[self.license],
                   "````"
                   ]

        # content = [CONTROLLED_LICENSE_LIST[self.license]]
        return content

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
        self.license = ""
        self._parse_content()
        new_content = self._create_content()
        new_nodes = self._parse_content_into_nodes(new_content)
        return new_nodes


def setup(app):

    app.add_directive("license_fairplus", LicenseFairplus)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


def _make_string_red(string):
    escape_character_to_make_a_string_red_start = "\033[91m"
    escape_character_to_make_a_string_red_end = "\033[0m"
    return escape_character_to_make_a_string_red_start + string + escape_character_to_make_a_string_red_end
