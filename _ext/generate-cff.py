from global_variables_fairplus import CONTROLLED_AUTHOR_LIST
import yaml
import os
import logging

cff = {
            "cff-version": "1.2.0",
            "message": "If you use this resource, please cite it using these metadata.",
            "title": "The FAIR Cookbook",
            "abstract": "Practical Guidance on how to make data FAIR and move through data maturity levels.",
            "authors": [{}],
            "version": "0.1.0",
            "date-released": "2022-04-30",
            "identifiers": [{"type": "doi",
                             "value": "10.0000.1234/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._[]()\\:;",
                             "description": "A pseudo-DOI testing all allowed characters."}],
            "license": "CC-BY-4.0",
            "license-url": "https://creativecommons.org/licenses/by/4.0/",
            "repository-code": "https://github.com/FAIRplus/the-fair-cookbook/",
            "url": "https://faircookbook.elixir-europe.org/content/home.html"
}


authors_list = []

logger = logging.getLogger(__name__)
logger.info('---CFF Citation generation:-----')

for key in CONTROLLED_AUTHOR_LIST.keys():
    alt_author = {}
    results = CONTROLLED_AUTHOR_LIST[key]["name"].split(" ", 1)

    if CONTROLLED_AUTHOR_LIST[key]["orcid"]:
        alt_author["family-names"] = results[1]
        alt_author["given-names"] = results[0]
        alt_author["orcid"] = "https://orcid.org/" + CONTROLLED_AUTHOR_LIST[key]["orcid"]
        alt_author["affiliation"] = CONTROLLED_AUTHOR_LIST[key]["affiliation"]

    else:
        alt_author["family-names"] = results[1]
        alt_author["given-names"] = results[0]
        alt_author["affiliation"] = CONTROLLED_AUTHOR_LIST[key]["affiliation"]

    authors_list.append(alt_author)

cff["authors"] = authors_list

try:
    with open(os.path.join("../", "CITATION.cff"), "w") as alt_cff:
        yaml.dump(cff, alt_cff, sort_keys=False)
except IOError as ioe:
    logging.error(ioe)