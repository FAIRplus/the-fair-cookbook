from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from json import dumps
import sphinx.errors
import sphinx_panels.panels
from sphinx.util import logging

from global_variables_fairplus import LINK_TO_THE_FAIRPLUS_LOGO, CONTROLLED_VOCABULARY_EXECUTABLE_CODE, CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL, CONTROLLED_VOCABULARY_INTENDED_AUDIENCE, CONTROLLED_VOCABULARY_MATURITY_LEVEL, CONTROLLED_VOCABULARY_MATURITY_INDICATOR, CONTROLLED_VOCABULARY_RECIPE_TYPE 

logger = logging.getLogger(__name__)
logger.info('Hello, this is "panels_fairplus" extension!')


class PanelFairplus(Directive):
    has_content = False
    final_argument_whitespace = True ## actually, this allows ANY argument to contain whitespace.
    option_spec = {
        "identifier_text"       : directives.unchanged_required,
        "identifier_link"       : directives.unchanged_required,
        "difficulty_level"      : directives.unchanged_required,
        "reading_time_minutes"  : directives.unchanged_required,
        "recipe_type"           : directives.unchanged_required,
        "has_executable_code"   : directives.unchanged_required,
        "intended_audience"     : directives.unchanged_required,
        "maturity_level"        : directives.unchanged_required,
        "maturity_indicator"    : directives.unchanged_required,
        "recipe_name": directives.unchanged_required
    }

    def _clean_options(self):

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
        assert  self.options["difficulty_level"]  in CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL or \
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



        # maturity_level
        assert      self.options["maturity_level"]  in CONTROLLED_VOCABULARY_MATURITY_LEVEL or \
                str(self.options["maturity_level"]) in CONTROLLED_VOCABULARY_MATURITY_LEVEL , \
            sphinx.errors.ExtensionError(
                _make_string_red(
                    f"The value of maturity_level has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_MATURITY_LEVEL))} ."
                    ))
        self.options["maturity_level"] = str(self.options["maturity_level"])


        # maturity_indicators
        list_of_maturity_indicators = []
        for split_element in self.options["maturity_indicator"].split(","):
            stripped = split_element.strip()
            if stripped == "": continue
            list_of_maturity_indicators.append( stripped )

            assert stripped in CONTROLLED_VOCABULARY_MATURITY_INDICATOR, \
            sphinx.errors.ExtensionError(
                _make_string_red(
                    f"The value of maturity_indicators has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_MATURITY_INDICATOR))} ."
                    ))

        # assert len(list_of_maturity_indicators) > 0, \
        #     sphinx.errors.ExtensionError(_make_string_red(
        #         f"The value of intended_audience has to contain at least one element."
        #         ))

        self.options["maturity_indicator"] = list_of_maturity_indicators

        # has_executable_code
        assert self.options["has_executable_code"] in CONTROLLED_VOCABULARY_EXECUTABLE_CODE, \
            sphinx.errors.ExtensionError(_make_string_red(
                f"The value of has_executable_code has to be out of the following controlled vocabulary: {', '.join(list(CONTROLLED_VOCABULARY_EXECUTABLE_CODE))} ."
                ))
            ## no joke, because "True" and "yes" are evaluated by YAML to be "", we need "yeah" and "nope"...

        assert ':' not in self.options["recipe_name"], \
            sphinx.errors.ExtensionError(
                _make_string_red("The colon (i.e. the character ':') is not allowed in recipe_name: %s" % (self.options["recipe_name"])))

    def _create_content(self):
        content = []
        content.extend([
            '<br/>',
            '',

            f'{self.get_ld()}',
            '<div class="card recipe d-flex">',
                '<div class="card-header purple-dark text--white">',
                    '<div class="overview">',
                        '<div class="overviewLabel">Recipe Overview</div>',
                        '<div class="overviewContent">',
                            '<div class="item"><div class="itemContainer">',
                                '<i class="itemIcon fa fa-clock fa-2x text--white"></i>',
                                '<div class="itemContent">',
                                    '<div class="label"> Reading Time </div>',
                                    f'{self.options["reading_time_minutes"]} minutes',
                               '</div>',
                            '</div></div>',
                            '<div class="item"><div class="itemContainer">',
                                '<i class="itemIcon fa fa-play-circle fa-2x text--white"></i>',
                                '<div class="itemContent">',
                                    '<div class="label"> Executable Code </div>',
                                    f'{ CONTROLLED_VOCABULARY_EXECUTABLE_CODE[self.options["has_executable_code"]] }',
                                '</div>',
                            '</div></div>',
                            '<div class="item" style="margin-bottom:10px"><div class="itemContainer">',
                                '<i class="itemIcon fa fa-fire fa-2x text--white" style="margin-left:4px;margin-right: 5px;"></i>',
                                '<div class="itemContent">',
                                    '<div class="label" style="position:relative; left:-6px">Difficulty</div>',
                                    *['<i class="fa fa-fire"></i>'] * self.options["difficulty_level"],
                                    *['<i class="fa fa-fire" style="color:grey"></i>'] * (5 - self.options["difficulty_level"]),
                                '</div>',
                            '</div></div>',
                        '</div>'
                    '</div>',
                '</div>',
                '<div class="card-body text--purple-dark">',
                    '<div class="title">',
                        f'<div style="flex-grow:1; margin-right:5px">{self.options["recipe_name"]}</div>',
                        f'<img src="{LINK_TO_THE_FAIRPLUS_LOGO}" alt="FAIRPlus logo"> </img>',
                    '</div>',
                    '<div class="section">',
                        '<i class="sectionIcon fa fa-laptop fa-2x"></i>'
                        '<div class="sectionContent">',
                            '<div class="label">Recipe Type</div>',
                            f'<div class="sectionValue">{ CONTROLLED_VOCABULARY_RECIPE_TYPE[self.options["recipe_type"]] }</div>',
                        '</div>',
                    '</div>',
                    '<div class="section" style="flex-grow: 1;">',
                        '<i class="sectionIcon fa fa-users fa-2x"></i>'
                        '<div class="sectionContent">',
                            '<div class="label">Audience</div>',
                            f'<div class="sectionValue">{self.get_audience()}</div>',
                        '</div>',
                    '</div>',
                    '<div class="section" style="flex-grow: 1;">',
                        f'<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="signal" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 600" class="bars {self.get_maturity()}">',
                          '<path class="bar5" d="M216 288h-48c-8.84 0-16 7.16-16 16v192c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V304c0-8.84-7.16-16-16-16zM88 384H40c-8.84 0-16 7.16-16 16v96c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16v-96c0-8.84-7.16-16-16-16zm256-192h-48c-8.84 0-16 7.16-16 16v288c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V208c0-8.84-7.16-16-16-16zm128-96h-48c-8.84 0-16 7.16-16 16v384c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V112c0-8.84-7.16-16-16-16zM600 0h-48c-8.84 0-16 7.16-16 16v480c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V16c0-8.84-7.16-16-16-16z"/>',
                          '<path class="bar4" d="M216 288h-48c-8.84 0-16 7.16-16 16v192c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V304c0-8.84-7.16-16-16-16zM88 384H40c-8.84 0-16 7.16-16 16v96c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16v-96c0-8.84-7.16-16-16-16zm256-192h-48c-8.84 0-16 7.16-16 16v288c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V208c0-8.84-7.16-16-16-16zm128-96h-48c-8.84 0-16 7.16-16 16v384c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V112c0-8.84-7.16-16-16-16zM600" />',  
                          '<path class="bar3" d="M216 288h-48c-8.84 0-16 7.16-16 16v192c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V304c0-8.84-7.16-16-16-16zM88 384H40c-8.84 0-16 7.16-16 16v96c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16v-96c0-8.84-7.16-16-16-16zm256-192h-48c-8.84 0-16 7.16-16 16v288c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V208c0-8.84-7.16-16-16-16zm128-96h-48c-8.84" />',
                          '<path class="bar1" d="M216 288h-48c-8.84 0-16 7.16-16 16v192c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V304c0-8.84-7.16-16-16-16zM88 384H40c-8.84 0-16 7.16-16 16v96c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16v-96c0-8.84-7.16-16-16-16zm256-192h-48c-8.84"/>',
                          '<path class="bar2" d="M216 288h-48c-8.84 0-16 7.16-16 16v192c0 8.84 7.16 16 16 16h48c8.84 0 16-7.16 16-16V304c0-8.84-7.16-16-16-16zM88 384H40c-8.84"/>',     
                        '</svg>',
                        '<div class="sectionContent">',
                          '<div class="label">Maturity Level & Indicator</div>',
                          f'<div class="sectionValue">{self.get_indicators()}</div>',
            '<div class="tooltip">hover me',
            '<span class="tooltiptext">Tooltip text</span></div>',
                        '</div>',
                    '</div>'
                    '<div class="card-footer text--orange sphinx-bs.badge.badge-primary"> Cite me with ',
                        f'<a href="{self.options["identifier_link"]}" class="text--purple-dark">{self.options["identifier_text"]}',
                    '</a></div>',

                '</div>',
            '</div>',
            '',

            ''
        ])
        return content

    def get_audience(self):
        """
        Gets the list of audience targets properly formatted as a string
        :return str: a string properly formatted containing the list of audience targets
        """
        audience = []
        for target in self.options["intended_audience"]:
            term, curie = CONTROLLED_VOCABULARY_INTENDED_AUDIENCE[target].split("|")
            if curie == "NA":
                audience_tag = term
            else:
                audience_tag = "<a href=\"http://purl.obolibrary.org/obo/" + curie + "\">" + term + "</a>"

            audience.append(audience_tag)
        # return ", ".join(["<a href=\"http://purl.obolibrary.org/obo/" +  + "</a>"
        #                   for target in self.options["intended_audience"]])
        return ", ".join(audience)

    def get_maturity(self):
        """
        Gets the list of improved maturity indicators
        :return str: a string properly formatted containing the list of audience targets
        """
        return ", ".join([CONTROLLED_VOCABULARY_MATURITY_LEVEL[target]
                          for target in self.options["maturity_level"]])

    def get_indicators(self):
        """
        Gets the list of improved maturity indicators
        :return str: a string properly formatted containing the list of audience targets
        """
        indicators = '<v-chip-group>'
        base_url = "https://github.com/FAIRplus/Data-Maturity/blob/indicator-definitions/docs/_indicators/"
        for indicator in self.options['maturity_indicator']:
            label = CONTROLLED_VOCABULARY_MATURITY_INDICATOR[indicator].replace('[', '').replace(']', '')
            href = base_url + label
            indicators += ('<v-chip href="{}" class="secondary white--text" target="_blank" label>'
                           '{}</v-chip>').format(href, label)
        indicators += '</v-chip-group>'
        return indicators

    def get_ld(self):
        """
        Parses the class attributes to build the corresponding JSON-LD markup.
        :return: a json-ld representation of the recipe
        """
        json_ld = {
            "@context": {
                "bs": "https://bioschema.org/",
                "dc": "http://purl.org/dc/terms/",
                "owl": "http://www.w3.org/2002/07/owl#",
                "sdo": "https://schema.org/",
            },
            "@type": ["sdo:HowTo", "sdo:LearningResource"],
            "@id": self.options["identifier_link"],
            "sdo:name": self.options["recipe_name"],
            "sdo:description": self.options["recipe_name"],
            "sdo:keywords": [],
            "dc:conformsTo": {
                "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE",
                "@type": "CreativeWork"
            },
            "sdo:inLanguage": ["en-GB"],
            "sdo:audience": [CONTROLLED_VOCABULARY_INTENDED_AUDIENCE[target]
                             for target in self.options["intended_audience"]],
            "sdo:isPartOf": [
                {
                    "@type": "CreativeWork",
                    "@id": "https://fairplus.github.io/the-fair-cookbook/",
                    "sdo:url": "https://fairplus.github.io/the-fair-cookbook/",
                    "sdo:name": "The FAIR Cookbook"
                }
            ],
            "sdo:learningResourceType": CONTROLLED_VOCABULARY_RECIPE_TYPE[self.options["recipe_type"]],
            "sdo:identifier": {
                "@type": "PropertyValue",
                "@id": "",
                "sdo:name": self.options["identifier_text"],
                "dso:url": self.options["identifier_link"],
                "owl:sameAs": "https://identifiers.org/fcb:%s" % str(self.options["identifier_text"])
            },
            "sdo:license": {
                "@type": "CreativeWork",
                "@id": "https://creativecommons.org/licenses/by/4.0/",
                "sdo:url": "https://creativecommons.org/licenses/by/4.0/",
                "sdo:name": "CC-BY-4.0"
            },
            "sdo:timeRequired": "PT0H%sM0S" % str(self.options["reading_time_minutes"]),
            "sdo:totalTime": "PT0H%sM0S" % str(self.options["reading_time_minutes"]),
            "sdo:step": [{
                "@type": "sdo:HowToSection",
                "sdo:position": "1",
                "sdo:name": "Overview",
                "sdo:url": self.options["identifier_link"] + "#main-objectives",
                "sdo:itemListElement": [{"@type": "sdo:HowToStep",
                                         "sdo:position": "1",
                                         "sdo:name": "",
                                         "sdo:itemListElement": [{"@type": "sdo:HowToDirection",
                                                                  "sdo:position": "1",
                                                                  "sdo:name": "step-by-step section",
                                                                  "sdo:text": "Follow the step-by-step section.",
                                                                  "sdo:url": self.options["identifier_link"]
                                                                             + "#main-objectives",},
                                                                 {"@type": "sdo:HowToTip",
                                                                  "sdo:position": "2",
                                                                  "sdo:name": "Reporting an issue",
                                                                  "sdo:text": "Use our GitHub issue tracker to report any error. Thanks!",
                                                                  "sdo:url": "https://github.com/FAIRplus/the-fair-cookbook/issues/new/choose"}]
                                         }
                                        ]},
                {
                    "@type": "sdo:HowToSection",
                    "sdo:position": "2",
                    "sdo:name": "Conclusion",
                    "sdo:url": self.options["identifier_link"] + "#conclusion",
                    "sdo:itemListElement": [{"@type": "sdo:HowToStep",
                                             "sdo:position": "1",
                                             "sdo:name": "",
                                             "sdo:itemListElement": [{"@type": "sdo:HowToDirection",
                                                                      "sdo:position": "1",
                                                                      "sdo:name": "conclusion section",
                                                                      "sdo:text": "What to read next?",
                                                                      "sdo:url": self.options["identifier_link"]
                                                                                 + "#conclusion"},
                                                                     {"@type": "sdo:HowToTip",
                                                                      "sdo:position": "2",
                                                                      "sdo:name": "Reporting an issue",
                                                                      "sdo:text": "Use our GitHub issue tracker to report any error. Thanks!",
                                                                      "sdo:url": "https://github.com/FAIRplus/the-fair-cookbook/issues/new/choose"}]}]}
            ]
        }
        return '<script type="application/ld+json"> %s </script>' % dumps(json_ld)

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


escape_character_to_make_a_string_red_start = "\033[91m"
escape_character_to_make_a_string_red_end   = "\033[0m"


def _make_string_red(string):
    return escape_character_to_make_a_string_red_start + string + escape_character_to_make_a_string_red_end
