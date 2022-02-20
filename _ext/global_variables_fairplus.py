
## these are global variables (= data, or even metadata!) used within the custom directives


CONTROLLED_VOCABULARY_RECIPE_TYPE = {
    "background_information"    : "Background information",
    "inventory"                 : "Inventory",
    "survey_review"             : "Survey / Review",
    "guidance"                  : "Guidance",
    "technical_guidance"        : "Technical Guidance",
    "hands_on"                  : "Hands-on",
    "applied_example"           : "Experience Report / Applied Example",
    "perspective"               : "Perspective"

}

CONTROLLED_VOCABULARY_INTENDED_AUDIENCE = {
    "funder"                    : "Funder",
    "procurement_officer"       : "Procurement Officer",
    "principal_investigator"    : "Principal Investigator",
    "data_curator"              : "Data Curator",
    "data_engineer"             : "Data Engineer",
    "data_manager"              : "Data Manager",
    "data_scientist"            : "Data Scientist",
    "chemoinformatician"        : "Chemoinformatician",
    "bioinformatician"          : "Bioinformatician",
    "software_engineer"         : "Software Engineer",
    "software_developer"        : "Software Developer",
    "system_administrator"      : "System Administrator",
    "terminology_manager"       : "Terminology Manager",
    "ontologist"                : "Ontologist",
    "data_producer"             : "Data Producer",
    "data_consumer"             : "Data Consumer",
    "everyone"                  : "Everyone",
}

CONTROLLED_VOCABULARY_DIFFICULTY_LEVEL = {
    "1" : "very easy",
    "2" : "easy",
    "3" : "medium",
    "4" : "hard",
    "5" : "very hard",
}

CONTROLLED_VOCABULARY_MATURITY_LEVEL = {
    "1" : "level 0",
    "2" : "level 1",
    "3" : "level 2",
    "4" : "level 3",
    "5" : "level 4",
}

CONTROLLED_VOCABULARY_EXECUTABLE_CODE = {
    "yeah" : "Yes",
    "nope" : "No",
}

LINK_TO_THE_FAIRPLUS_LOGO = "https://fairplus.github.io/the-fair-cookbook/_static/images/fairplus-mini.png"


CONTROLLED_LIST_OF_ELIXIR_NODES = {
    "BE"        : "ELIXIR-BE.svg",
    "CH"        : "ELIXIR-CH.svg",
    "CZ"        : "ELIXIR-CZ.svg",
    "DE"        : "ELIXIR-DE.svg",
    "DK"        : "ELIXIR-DK.svg",
    "EE"        : "ELIXIR-EE.svg",
    "ES"        : "ELIXIR-ES.svg",
    "FI"        : "ELIXIR-FI.svg",
    "FR"        : "ELIXIR-FR.svg",
    "GR"        : "ELIXIR-GR.svg",
    "HU"        : "ELIXIR-HU.svg",
    "IE"        : "ELIXIR-IE.svg",
    "IL"        : "ELIXIR-IL.svg",
    "IT"        : "ELIXIR-IT.svg",
    "LU"        : "ELIXIR-LU.svg",
    "NL"        : "ELIXIR-NL.svg",
    "NO"        : "ELIXIR-NO.svg",
    "PT"        : "ELIXIR-PT.svg",
    "SE"        : "ELIXIR-SE.svg",
    "SI"        : "ELIXIR-SI.svg",
    "UK"        : "ELIXIR-UK.svg",
    "general"   : "ELIXIR.png",
    "embl"      : "embl.png",
}

## for NULL values (= not existent, e.g. github_handle, orcid, elixir_node), set to ""
## allowed values for type_of_affiliation: "academia", "efpia", "sme".
CONTROLLED_AUTHOR_LIST = {
"Alasdair"          : { "github_handle" : "AlasdairGray",     "name" : "Alasdair J G Gray",          "orcid" : "0000-0002-5711-4872",        "affiliation" : "Heriot Watt University",                          "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Alejandra"         : { "github_handle" : "",                 "name" : "Alejandra Delfin Rossaro",   "orcid" : "0000-0002-5423-4203",        "affiliation" : "Universite Paul Sabatier",                        "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"AndreaSplendiani"  : { "github_handle" : "sgtp",             "name" : "Andrea Splendiani",          "orcid" : "0000-0002-3201-9617",        "affiliation" : "Novartis AG",                                     "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"AndreaZaliani"     : { "github_handle" : "agiani99",         "name" : "Andrea Zaliani",             "orcid" : "0000-0002-1740-8390",        "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Andreas"           : { "github_handle" : "",                 "name" : "Andreas Pippow",             "orcid" : "0000-0003-1301-2580",        "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Anne"              : { "github_handle" : "",                 "name" : "Anne Cambon-Thomsen",        "orcid" : "0000-0001-8793-3644",        "affiliation" : "Universite Paul Sabatier",                        "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Ashni"             : { "github_handle" : "",                 "name" : "Ashni Sedani",               "orcid" : "0000-0002-2424-3483",        "affiliation" : "GSK",                                             "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Carole"            : { "github_handle" : "carolegoble",      "name" : "Carole Goble",               "orcid" : "0000-0003-1219-2137",        "affiliation" : "University of Manchester",                        "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Chris"             : { "github_handle" : "Chris-Evelo",      "name" : "Chris Evelo",                "orcid" : "0000-0002-5301-3142",        "affiliation" : "Maastricht University",                           "type_of_affiliation" : "academia",         "elixir_node" : "NL"        }, 
"Chuang"            : { "github_handle" : "",                 "name" : "Chuang Kee Ong",             "orcid" : "",                           "affiliation" : "Astra-Zeneca",                                    "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Colin"             : { "github_handle" : "",                 "name" : "Colin Wood",                 "orcid" : "",                           "affiliation" : "Astra-Zeneca",                                    "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Daniel"            : { "github_handle" : "u8sand",           "name" : "Daniel J. B. Clarke",        "orcid" : "0000-0003-3471-7416",        "affiliation" : "Icahn School of Medicine at Mount Sinai",         "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Danielle"          : { "github_handle" : "daniwelter",       "name" : "Danielle Welter",            "orcid" : "0000-0003-1058-2668",        "affiliation" : "University of Luxembourg",                        "type_of_affiliation" : "academia",         "elixir_node" : "LU"        }, 
"David"             : { "github_handle" : "",                 "name" : "David Henderson",            "orcid" : "0000-0002-6433-200X",        "affiliation" : "Bayer AG",                                        "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Dominique"         : { "github_handle" : "terazus",          "name" : "Dominique Batista",          "orcid" : "0000-0002-2109-489X",        "affiliation" : "University of Oxford",                            "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Dorothy"           : { "github_handle" : "",                 "name" : "Dorothy Reilly",             "orcid" : "",                           "affiliation" : "Novartis AG",                                     "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Ebtisam"           : { "github_handle" : "mfby4ea3",         "name" : "Ebtisam Alharbi",            "orcid" : "",                           "affiliation" : "University of Manchester",                        "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Eelke"             : { "github_handle" : "eelkevanderhorst", "name" : "Eelke van der Horst",        "orcid" : "0000-0002-8777-5612",        "affiliation" : "The Hyve",                                        "type_of_affiliation" : "sme",              "elixir_node" : ""          }, 
"Egon"              : { "github_handle" : "egonw",            "name" : "Egon Willighagen",           "orcid" : "0000-0001-7542-0286",        "affiliation" : "Maastricht University",                           "type_of_affiliation" : "academia",         "elixir_node" : "NL"        }, 
"Emiliano"          : { "github_handle" : "ereynrs",          "name" : "Emiliano Reynares",          "orcid" : "0000-0002-5109-3716",        "affiliation" : "Boehringer-Ingelheim AG",                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Emma"              : { "github_handle" : "",                 "name" : "Emma Vos",                   "orcid" : "0000-0002-8589-0609",        "affiliation" : "The Hyve",                                        "type_of_affiliation" : "sme",              "elixir_node" : ""          }, 
"Eva"               : { "github_handle" : "evaMart",          "name" : "Eva Marin del Pico",         "orcid" : "0000-0001-8324-2897",        "affiliation" : "Barcelona Supercomputing Centre",                 "type_of_affiliation" : "academia",         "elixir_node" : "ES"        }, 
"Francesco"         : { "github_handle" : "fra82",            "name" : "Francesco Ronzano",          "orcid" : "0000-0001-5037-9061",        "affiliation" : "IMIM",                                            "type_of_affiliation" : "academia",         "elixir_node" : "ES"        }, 
"Franziska"         : { "github_handle" : "",                 "name" : "Franziska Kroh",             "orcid" : "",                           "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Fuqi"              : { "github_handle" : "fuqix",            "name" : "Fuqi Xu",                    "orcid" : "0000-0002-5923-3859",        "affiliation" : "EMBL-EBI",                                        "type_of_affiliation" : "academia",         "elixir_node" : "embl"      }, 
"Gabriel"           : { "github_handle" : "denoa1",           "name" : "Gabriel Backianathan",       "orcid" : "",                           "affiliation" : "Novartis AG",                                     "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"George"            : { "github_handle" : "",                 "name" : "George Papadotas",           "orcid" : "",                           "affiliation" : "GSK",                                             "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Gesa"              : { "github_handle" : "",                 "name" : "Gesa Witt",                  "orcid" : "0000-0003-2344-706X",        "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Hannah"            : { "github_handle" : "HEHurst",          "name" : "Hannah Hurst",               "orcid" : "",                           "affiliation" : "EMBL-EBI",                                        "type_of_affiliation" : "academia",         "elixir_node" : "embl"      }, 
"Herman"            : { "github_handle" : "",                 "name" : "Herman Van Vlijmen",         "orcid" : "0000-0002-1915-3141",        "affiliation" : "Janssen",                                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Ibrahim"           : { "github_handle" : "iemam",            "name" : "Ibrahim Emam",               "orcid" : "0000-0002-7561-2787",        "affiliation" : "Imperial College London",                         "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Jean"              : { "github_handle" : "",                 "name" : "Jean-Marc Neefs",            "orcid" : "",                           "affiliation" : "Janssen",                                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Jolanda"           : { "github_handle" : "JolandaS",         "name" : "Jolanda Strubel",            "orcid" : "0000-0001-6675-4639",        "affiliation" : "The Hyve",                                        "type_of_affiliation" : "sme",              "elixir_node" : ""          }, 
"Karsten"           : { "github_handle" : "",                 "name" : "Karsten Quast",              "orcid" : "",                           "affiliation" : "Boehringer-Ingelheim AG",                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Kees"              : { "github_handle" : "keesvanbochove",   "name" : "Kees van Bochove",           "orcid" : "0000-0002-8589-0609",        "affiliation" : "The Hyve",                                        "type_of_affiliation" : "sme",              "elixir_node" : ""          }, 
"Kurt"              : { "github_handle" : "kdauth",           "name" : "Kurt Dauth",                 "orcid" : "",                           "affiliation" : "Boehringer-Ingelheim AG",                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Laura"             : { "github_handle" : "",                 "name" : "Laura Furlong",              "orcid" : "0000-0002-9383-528X",        "affiliation" : "IMIM",                                            "type_of_affiliation" : "academia",         "elixir_node" : "ES"        }, 
"Leyla"             : { "github_handle" : "ljgarcia",         "name" : "Leyla Garcia",               "orcid" : "0000-0003-3986-0510",        "affiliation" : "ZB MED Information Centre for life sciences",     "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Lucas"             : { "github_handle" : "lucas-ubm",        "name" : "Lucas Giovanni",             "orcid" : "0000-0001-6518-9535",        "affiliation" : "Maastricht University",                           "type_of_affiliation" : "academia",         "elixir_node" : "NL"        }, 
"Manfred"           : { "github_handle" : "",                 "name" : "Manfred Kohler",             "orcid" : "",                           "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Manuela"           : { "github_handle" : "",                 "name" : "Manuela Pruess",             "orcid" : "0000-0002-6857-5543",        "affiliation" : "SIB",                                             "type_of_affiliation" : "academia",         "elixir_node" : "CH"        }, 
"Mark"              : { "github_handle" : "",                 "name" : "Mark Ibberson",              "orcid" : "0000-0003-3152-5670",        "affiliation" : "SIB",                                             "type_of_affiliation" : "academia",         "elixir_node" : "CH"        }, 
"Melanie"           : { "github_handle" : "mcourtot",         "name" : "Melanie Courtot",            "orcid" : "0000-0002-9551-6370",        "affiliation" : "EMBL-EBI",                                        "type_of_affiliation" : "academia",         "elixir_node" : "embl"      }, 
"Mike"              : { "github_handle" : "mikedarcy",        "name" : "Mike d'Arcy",                "orcid" : "0000-0003-2280-917X",        "affiliation" : "University of Southern California",               "type_of_affiliation" : "academia",         "elixir_node" : "embl"      }, 
"NickJuty"          : { "github_handle" : "nsjuty",           "name" : "Nick Juty",                  "orcid" : "0000-0002-2036-8350",        "affiliation" : "University of Manchester",                        "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"NickLynch"         : { "github_handle" : "nicklynch",        "name" : "Nick Lynch",                 "orcid" : "0000-0002-8997-5298",        "affiliation" : "OpenPhacts",                                      "type_of_affiliation" : "sme",              "elixir_node" : ""          }, 
"Ola"               : { "github_handle" : "",                 "name" : "Ola Engkvist",               "orcid" : "0000-0003-4970-6461",        "affiliation" : "Astra-Zeneca",                                    "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Oya"               : { "github_handle" : "oyadenizbeyan",    "name" : "Oya Deniz Beyan",            "orcid" : "0000-0001-7611-3501",        "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Paul"              : { "github_handle" : "",                 "name" : "Paul Peeters",               "orcid" : "0000-0001-9915-2933",        "affiliation" : "Janssen",                                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Peter"             : { "github_handle" : "PeterWoollard",    "name" : "Peter Woollard",             "orcid" : "0000-0002-7654-6902",        "affiliation" : "GSK",                                             "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Petros"            : { "github_handle" : "petrospaps",       "name" : "Petros Papadopoulos",        "orcid" : "0000-0002-8110-7576",        "affiliation" : "Heriot Watt University",                          "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Philip"            : { "github_handle" : "",                 "name" : "Philip Gribbon",             "orcid" : "0000-0001-7655-2459",        "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Philippe"          : { "github_handle" : "proccaserra",      "name" : "Philippe Rocca-Serra",       "orcid" : "0000-0001-9853-5668",        "affiliation" : "University of Oxford",                            "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Ratnesh"           : { "github_handle" : "",                 "name" : "Ratnesh Sahay",              "orcid" : "",                           "affiliation" : "Astra-Zeneca",                                    "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Robert"            : { "github_handle" : "robertgiessmann",  "name" : "Robert Giessmann",           "orcid" : "0000-0002-0254-1500",        "affiliation" : "Bayer AG",                                        "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Rudi"              : { "github_handle" : "rverbeec",         "name" : "Rudi Verbeeck",              "orcid" : "0000-0001-5445-6095",        "affiliation" : "Janssen",                                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Salvador"          : { "github_handle" : "scapella",         "name" : "Salvador Capella Gutierrez", "orcid" : "0000-0002-0309-604X",        "affiliation" : "Barcelona Supercomputing Centre",                 "type_of_affiliation" : "academia",         "elixir_node" : "ES"        }, 
"Scott"             : { "github_handle" : "",                 "name" : "Scott Lusher",               "orcid" : "",                           "affiliation" : "Janssen",                                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Sukhi"             : { "github_handle" : "",                 "name" : "Sukhi Singh",                "orcid" : "0000-0001-8324-2897",        "affiliation" : "The Hyve",                                        "type_of_affiliation" : "sme",              "elixir_node" : ""          }, 
"Susanna"           : { "github_handle" : "susannasansone",   "name" : "Susanna-Assunta Sansone",    "orcid" : "0000-0001-5306-5690",        "affiliation" : "University of Oxford",                            "type_of_affiliation" : "academia",         "elixir_node" : "UK"        }, 
"Tom"               : { "github_handle" : "",                 "name" : "Tom Plasterer",              "orcid" : "",                           "affiliation" : "Astra-Zeneca",                                    "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Tony"              : { "github_handle" : "tburdett",         "name" : "Tony Burdett",               "orcid" : "0000-0002-2513-5396",        "affiliation" : "EMBL-EBI",                                        "type_of_affiliation" : "academia",         "elixir_node" : "embl"      }, 
"Ulrich"            : { "github_handle" : "ulo",              "name" : "Ulrich Goldmann",            "orcid" : "0000-0003-1120-6912",        "affiliation" : "CEMM",                                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Valentin"          : { "github_handle" : "neoflex",          "name" : "Valentin Grouès",            "orcid" : "0000-0001-6501-0806",        "affiliation" : "University of Luxembourg",                        "type_of_affiliation" : "academia",         "elixir_node" : "LU"        }, 
"Vassilios"         : { "github_handle" : "vioannid",         "name" : "Vassilios Ioannidis",        "orcid" : "0000-0002-4209-2578",        "affiliation" : "SIB",                                             "type_of_affiliation" : "academia",         "elixir_node" : "CH"        }, 
"Venkata"           : { "github_handle" : "satagopam7",       "name" : "Venkata P. Satagopam",       "orcid" : "0000-0002-6532-5880",        "affiliation" : "University of Luxembourg",                        "type_of_affiliation" : "academia",         "elixir_node" : "LU"        }, 
"Vitaly"            : { "github_handle" : "sedlyarov",        "name" : "Vitaly Sedlyarov",           "orcid" : "0000-0002-9872-3535",        "affiliation" : "Boehringer-Ingelheim AG",                         "type_of_affiliation" : "efpia",            "elixir_node" : ""          }, 
"Wei"               : { "github_handle" : "weiguUL",          "name" : "Wei Gu",                     "orcid" : "0000-0003-3951-6680",        "affiliation" : "University of Luxembourg",                        "type_of_affiliation" : "academia",         "elixir_node" : "LU"        }, 
"Yojana"            : { "github_handle" : "YojanaGadiya",     "name" : "Yojana Gaidya",              "orcid" : "0000-0002-7683-0452",        "affiliation" : "Fraunhofer Institute",                            "type_of_affiliation" : "academia",         "elixir_node" : ""          }, 
"Zachary"           : { "github_handle" : "zjwarnes",         "name" : "Zachary Warnes",             "orcid" : "0000-0002-7777-6013",        "affiliation" : "Maastricht University",                           "type_of_affiliation" : "academia",         "elixir_node" : "NL"        }, 
}


CONTROLLED_LICENSE_LIST = {
    "CC-BY-4.0": """This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
""", 
    "CC0-1.0": """This page is released under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

<a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en"><img src="[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/deed.en)" height="20"/></a>
"""

}
