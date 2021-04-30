from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import sphinx_panels.panels
import sphinx.errors


CONTROLLED_VOCABULARY_RECIPE_TYPE = {
    "background_information"    : "Background information",
    "survey_review"             : "Survey / Review",
    "guidance"                  : "Guidance",    
    "technical_guidance"        : "Technical Guidance",
    "handson"                   : "Hands-on",
}

CONTROLLED_VOCABULARY_INTENDED_AUDIENCE = {
    "funder"                    : "Funder",
    "procurement_officer"       : "Procurement Officer",
    "principal_investigator"    : "Principal Investigator",
    "data_curator"              : "Data Curator",
    "data_manager"              : "Data Manager",
    "data_scientist"            : "Data Scientist",
    "chemoinformatician"        : "Chemoinformatician",
    "bioinformatician"          : "Bioinformatician",
    "software_engineer"         : "Software Engineer",
    "system_administrator"      : "System Administrator",
    "terminology_manager"       : "Terminology Manager",
    "ontologist"                : "Ontologist",
}

CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL = {
    "1" : "very easy",
    "2" : "easy",
    "3" : "medium",
    "4" : "hard",
    "5" : "very hard",
}

CONTROLLED_VOCABULARY_EXECUTABLE_CODE = {
    "yeah" : "Yes",
    "nope" : "No",
}

make_red_start = "\033[91m"
make_red_end   = "\033[0m"
def _make_string_red(string):
    return make_red_start + string + make_red_end


class PanelFairplus(Directive):
    has_content = True
    final_argument_whitespace = True ## actually, this allows ANY argument to contain whitespace.
    option_spec = {
        "identifier_text"       : directives.unchanged_required,
        "identifier_link"       : directives.unchanged_required,
        "difficulty_level"      : directives.unchanged_required,
        "reading_time_minutes"  : directives.unchanged_required,
        "recipe_type"           : directives.unchanged_required,
        "has_executable_code"   : directives.unchanged_required,
        "intended_audience"     : directives.unchanged_required,
    }

    def _clean_options(self):
        print("")
        print(self.options)
        
        # are the options existent and non-empty?
        for option_name in self.option_spec: 
            assert option_name in self.options, \
                sphinx.errors.ExtensionError(_make_string_red(
                    f"You did not provide the required option {option_name}."
                    ))

            assert self.options[option_name] != "", \
                sphinx.errors.ExtensionError(_make_string_red(
                    f"The value of {option_name} has to be non-empty."
                    ))
        
        # identifier_text
        pass
        

        # identifier_link
        assert self.options["identifier_link"].startswith("http://") or self.options["identifier_link"].startswith("https://"), \
            sphinx.errors.ExtensionError(_make_string_red(
                f"The value of identifier_link has to start with http:// or https://."
                ))


        # difficulty_level
        assert      self.options["difficulty_level"]  in CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL or \
                str(self.options["difficulty_level"]) in CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL , \
            sphinx.errors.ExtensionError(
                _make_string_red(
                    f"The value of difficulty_level has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL))} ."
                    ))
        self.options["difficulty_level"] = int(self.options["difficulty_level"])


        # recipe_type
        assert self.options["recipe_type"] in CONTROLLED_VOCABULARY_RECIPE_TYPE, \
            sphinx.errors.ExtensionError(
                _make_string_red(
                    f"The value of recipe_type has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_RECIPE_TYPE))} ."
                    ))


        # reading_time_minutes
        try:
            self.options["reading_time_minutes"] = int(self.options["reading_time_minutes"])
        except ValueError:
            raise \
                sphinx.errors.ExtensionError(_make_string_red(
                    f"The value of reading_time_minutes has to be an integer number."
                    ))

        assert self.options["reading_time_minutes"] > 0, \
            sphinx.errors.ExtensionError(_make_string_red(
                f"The value of reading_time_minutes has to be a positive number."
                ))


        # intended_audience
        list_of_intended_audiences = []
        for split_element in self.options["intended_audience"].split(","):
            stripped = split_element.strip()
            if stripped == "": continue
            list_of_intended_audiences.append( stripped )

            assert stripped in CONTROLLED_VOCABULARY_INTENDED_AUDIENCE, \
            sphinx.errors.ExtensionError(
                _make_string_red(
                    f"The value of intended_audience has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_INTENDED_AUDIENCE))} ."
                    ))

        assert len(list_of_intended_audiences) > 0, \
            sphinx.errors.ExtensionError(_make_string_red(
                f"The value of intended_audience has to contain at least one element."
                ))

        self.options["intended_audience"] = list_of_intended_audiences

        
        # has_executable_code
        assert self.options["has_executable_code"] in CONTROLLED_VOCABULARY_EXECUTABLE_CODE, \
            sphinx.errors.ExtensionError(_make_string_red(
                f"The value of has_executable_code has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_EXECUTABLE_CODE))} ."
                ))
            ## no joke, because "True" and "yes" are evaluated by YAML to be "", we need "yeah" and "nope"... 

        print(self.options)


    def _create_content(self):
        content = []


        content.extend(
            [
            '<br/>',
            '',
            '----',
            '',
            '````{panels}',
            ':container: container-lg pb-3',
            ':column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1',
            ':card: rounded',
            '',
            '<i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>',
            '^^^',
            '<h4><b>Identifier</b></h4>',
            f'<i class="fa fa-map-signs fa-lg" style="color:#7e0038;"></i> <a href="{self.options["identifier_link"]}">{self.options["identifier_text"]}</a> ',
            '',
            '---',
            '<i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>',
            '^^^',
            '<h4><b>Difficulty level</b></h4>',
            *['<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>'] * self.options["difficulty_level"],
            *['<i class="fa fa-fire fa-lg" style="color:lightgrey;"></i>'] * (5 - self.options["difficulty_level"]),
            '',
            '---',
            '<i class="fas fa-clock fa-2x" style="color:#7e0038;"></i>',
            '^^^',
            '<h4><b>Reading Time</b></h4>',
            f'<i class="fa fa-clock fa-lg" style="color:#7e0038;"></i> {self.options["reading_time_minutes"]} minutes',
            '<h4><b>Recipe Type</b></h4>',
            f'<i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> { CONTROLLED_VOCABULARY_RECIPE_TYPE[self.options["recipe_type"]] }',
            '<h4><b>Executable Code</b></h4>',
            f'<i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> { CONTROLLED_VOCABULARY_EXECUTABLE_CODE[self.options["has_executable_code"]] }',
            '',
            '---',
            '<i class="fa fa-users fa-2x" style="color:#7e0038;"></i>',
            '^^^',
            '<h4><b>Intended Audience</b></h4>',
            '<p><i class="fa fa-money-bill fa-lg" style="color:#7e0038;"></i> Funder</p>'                                if "funder" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Procurement Officer  </p>'                 if "procurement_officer" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i>    Principal Investigator</p>'                if "principal_investigator" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Data Curator  </p>'                        if "data_curator" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-database fa-lg" style="color:#7e0038;"></i>   Data Manager</p>'                          if "data_manager" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i>     Data Scientist</p>'                        if "data_scientist" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Chemoinformatician  </p>'                  if "chemoinformatician" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Bioinformatician  </p>'                    if "bioinformatician" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Software Engineer  </p>'                   if "software_engineer" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       System Administrator  </p>'                if "system_administrator" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Terminology Manager  </p>'                 if "terminology_manager" in self.options["intended_audience"] else "",
            '<p><i class="fa fa-user fa-lg" style="color:#7e0038;"></i>       Ontologist  </p>'                          if "ontologist" in self.options["intended_audience"] else "",
            '````',
            '',
            '----',
            ''
        ])
        return content

    def run(self):

        self._clean_options()

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
    app.setup_extension("sphinx_panels")

    app.add_directive("panels_fairplus", PanelFairplus)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
    
