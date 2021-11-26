import os

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import sphinx.errors
from sphinx.util import logging


logger = logging.getLogger(__name__)
logger.info('Hello, this is "figure_fairplus" extension!')


class FigureFairplus(Directive):
    """
    This directive is supposed to work like this:

    ````{figure_fairplus} aspera.md-figure1.mmd
    name: aspera-figure1
    subtitle: Aspera Data Transfer Process.
    ````
    
    Failure to stick to this format will raise an Exception.

    """

    has_content = True
    final_argument_whitespace = False
    option_spec = {}

    def _create_content(self):
        if self.is_vectorgraphic:
            filename = self.filename + ".svg"
            links_to_high_resolution_pictures = "" + \
                f"{{download}}`[download as png] <{self.filename + '.hi-res.png'}>` "        + \
                f"{{download}}`[download as mermaid diagram] <{self.filename}>` "             + \
                f"{{download}}`[download as svg vector graphic] <{self.filename + '.svg'}>` "

        else:
            filename = self.filename
            links_to_high_resolution_pictures = ""


        content = [f"```{{figure}} {filename}",
        "---",
        f"name: {self.name}",
        f"alt: {self.subtitle}",
        "---",
        f"{self.subtitle} {links_to_high_resolution_pictures}",
        "```"
        ]
        return content

    def _parse_content(self):

        print(self.content)
        print(self.content.items)
        assert len(self.content) == 3, _make_string_red("The {figure_fairplus} directive expects to consist of three lines, like this:\n"+
            " ````{figure_fairplus} example.md-figure1.mmd \n name: example-figure1 \n subtitle: Example Figure has explanatory text. \n ````")

        filename_string = self.content[0]
        name_string     = self.content[1]
        subtitle_string = self.content[2]

        ## check file
        context = self.content.items[0][0]
        path_to_file = os.path.abspath(os.path.join(os.path.dirname(context), filename_string))

                
        ## TODO workaround until finalized
        if ".mmd.png" in filename_string:
            self.is_vectorgraphic = False
            filename_string = "/dummy.jpeg"
            path_to_file = "/Users/robert/git/the-fair-cookbook/dummy.jpeg"
        ############################################
        
        assert os.path.exists(path_to_file), _make_string_red(f"image file does not exist: {filename_string}")
        self.filename = filename_string

        file_extension = os.path.splitext(filename_string)[1].lower()[1:] 
        if file_extension == "mmd":
            self.is_vectorgraphic = True
            expected = path_to_file + ".hi-res.png"
            assert os.path.exists(expected), _make_string_red(f"image file does not exist: {expected}")
            expected = path_to_file + ".lo-res.png"
            assert os.path.exists(expected), _make_string_red(f"image file does not exist: {expected}")
            expected = path_to_file + ".svg"
            assert os.path.exists(expected), _make_string_red(f"image file does not exist: {expected}")
        elif file_extension == "png" or file_extension == "jpg" or file_extension == "jpeg":
            self.is_vectorgraphic = False
        else:
            raise "Unknown file extension for an image"


        ## check name
        assert name_string.startswith("name: "), _make_string_red("The second line of the {figure_fairplus} directive has to start with 'name: '.")
        self.name = name_string[6:]
        
        ## check subtitle
        assert subtitle_string.startswith("subtitle: "), _make_string_red("The third line of the {figure_fairplus} directive has to start with 'subtitle: '.")
        self.subtitle = subtitle_string[10:]
        





    def _parse_content_into_nodes(self, new_content):
        if len(self.content) > 0:
            common_filename = self.content.items[0][0]
            for index, (filename, linenumber) in enumerate(self.content.items):
                assert filename   == common_filename, "Unexpected behavior of sphinx."
                assert linenumber == index          , "Unexpected behavior of sphinx."
        else:
            common_filename = None
        self.content.data = []
        self.content.items = []
        for idx, line in enumerate(new_content):
            self.content.data.append(line)
            self.content.items.append( (common_filename, idx) )
        node = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, node)
        return node.children

    def run(self):
        self.is_vectorgraphic = None 
        self.filename = None

        self._parse_content()
        new_content = self._create_content()
        new_nodes = self._parse_content_into_nodes(new_content)
        return new_nodes


def setup(app):

    app.add_directive("figure_fairplus", FigureFairplus)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


def _make_string_red(string):
    escape_character_to_make_a_string_red_start = "\033[91m"
    escape_character_to_make_a_string_red_end   = "\033[0m"
    return escape_character_to_make_a_string_red_start + string + escape_character_to_make_a_string_red_end
