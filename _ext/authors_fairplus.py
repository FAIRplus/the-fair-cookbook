from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import sphinx.errors
from sphinx.util import logging


from global_variables_fairplus import CONTROLLED_AUTHOR_LIST, CONTROLLED_LIST_OF_ELIXIR_NODES

logger = logging.getLogger(__name__)
logger.info('Hello, this is "authors_fairplus" extension!')


class AuthorsFairplus(Directive):
    """
    This directive is supposed to work like this:

    ````{authors}
    author_name1: contribution1, contribution2
    author_name2: contribution1, contribution3
    ````

    Failure to stick to this format will raise an Exception. 
    """

    has_content = True
    final_argument_whitespace = False ## actually, this allows ANY argument to contain whitespace.
    option_spec = {}

    def _parse_content(self):

        for line in self.content:
            if line.strip() == "":
                continue

            if line.count(":") != 1:
                raise sphinx.errors.ExtensionError(_make_string_red(
                    f"The author line must contain exactly one colon (':'), but you gave: '{line}'"
                ))

            author, contribution_list = line.split(":")
            author = author.strip()
            contributions = list([ c.strip() for c in contribution_list.split(",") if c.strip() != "" ])

            if contributions == []:
                raise sphinx.errors.ExtensionError(_make_string_red(
                    f"You have to enter the specific contributions for all authors, but you gave: '{line}'"
                ))

            #logger.info([author, contributions])

            if author in self.author_dict:
                raise sphinx.errors.ExtensionError(_make_string_red(
                     f"You have entered the author '{author}' at least twice, but authors have to be unique"
                ))

            self.author_dict.update( { author: contributions } )


        for author in self.author_dict:
            if not author in CONTROLLED_AUTHOR_LIST:
                raise sphinx.errors.ExtensionError(_make_string_red(
                    f"The author '{author}' is not registered in the CONTROLLED_AUTHOR_LIST. You can add the author in _ext/global_variables_fairplus.py if you want."
                ))

        return 

    def _create_content(self):
        content = []

        content.extend([
            '| Name | ORCID | Affiliation | Type | ELIXIR Node | Contribution |',
            '|------|-------|-------------|------|-------------|--------------|',
        ])

        for author in self.author_dict:
        
            github_handle        = CONTROLLED_AUTHOR_LIST[author]["github_handle"]
            name                 = CONTROLLED_AUTHOR_LIST[author]["name"]
            orcid                = CONTROLLED_AUTHOR_LIST[author]["orcid"]
            affiliation          = CONTROLLED_AUTHOR_LIST[author]["affiliation"]
            type_of_affiliation  = CONTROLLED_AUTHOR_LIST[author]["type_of_affiliation"]
            elixir_node          = CONTROLLED_AUTHOR_LIST[author]["elixir_node"]
            

            if github_handle != "":
                github_link_start = f'<a target="_blank" href="https://github.com/{github_handle}">'
                github_link_end   = '</a>'
                github_image_block = f'<img class="avatar-style" src="https://avatars.githubusercontent.com/{github_handle}"></img>'
            else:
                github_link_start = ""
                github_link_end   = ""
                github_image_block = f'<img class="avatar-style" src="https://avatars.githubusercontent.com/NONE"></img>'

            github_and_name_block = f'<div class="firstCol">{github_link_start}{github_image_block}<div class="d-block">{name}</div>{github_link_end}</div>'


            if orcid != "":
                orcid_block = f'<a target="_blank" href="https://orcid.org/{orcid}"><i class="fab fa-orcid fa-2x text--orange"></i></a>'
            else:
                orcid_block = ""


            if type_of_affiliation == "academia":
                type_block = '<i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i>'
            elif type_of_affiliation == "efpia":
                type_block = '<i class="fas fa-industry fa-1x text--purple-light" alt="EFPIA"></i>'
            elif type_of_affiliation == "sme":
                type_block = '<i class="fas fa-project-diagram fa-1x" style="color:#300861;" alt="SME"></i>'
            else:
                raise sphinx.errors.ExtensionError(_make_string_red(f"Unexpected type of affiliation for author '{author}'."))


            if elixir_node != "":
                assert elixir_node in CONTROLLED_LIST_OF_ELIXIR_NODES, \
                    sphinx.errors.ExtensionError(_make_string_red(f"The elixir_node of '{author}' is not registered in the CONTROLLED_LIST_OF_ELIXIR_NODES."))

                elixir_block = f'<img class="elixir-style" src="../../../_static/images/logo/Elixir/{CONTROLLED_LIST_OF_ELIXIR_NODES[elixir_node]}" ></img>' #
            else:
                elixir_block = ""


            contribution_list = self.author_dict[author]
            contribution_block = ", ".join(contribution_list)


            content.extend([
                f'| {github_and_name_block} | {orcid_block} | {affiliation} | {type_block} | {elixir_block} | {contribution_block} |'
            ])
        return content


    def run(self):

        self.author_dict = {}

        self._parse_content()

        new_content = self._create_content()

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


def setup(app):

    app.add_directive("authors_fairplus", AuthorsFairplus)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


def _make_string_red(string):
    escape_character_to_make_a_string_red_start = "\033[91m"
    escape_character_to_make_a_string_red_end   = "\033[0m"
    return escape_character_to_make_a_string_red_start + string + escape_character_to_make_a_string_red_end
