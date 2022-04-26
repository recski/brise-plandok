import argparse
import json
import logging
import os
import sys
from contextlib import contextmanager

from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline

from brise_plandok.constants import SenFields


class Extractor:
    def __init__(self, nlp, cache_dir="cache"):
        self.nlp = nlp
        self.cache_dir = cache_dir

    def parse(self, text):
        return self.nlp(text)

    def run_on_parsed_sections(self, sections):
        raise NotImplementedError

    def run_on_sections(self, sections):
        """The function parses each section in the json file, first running dependency parsing on each document.
        After parsing the sentences with stanza, we run the IRTG parsers
        """
        for section in sections:
            for sen in section["sens"]:
                if "tokens" not in sen:
                    sen["tokens"] = self.parse(sen["text"]).sentences[0].to_dict()

        results = self.run_on_parsed_sections(sections)

        for section in sections:
            for sen in section["sens"]:
                # both types of return values should have all data
                if SenFields.ID in sen:
                    sen_id = sen[SenFields.ID]
                else:
                    sen_id = sen["sen_id"]
                sen.update(results[sen_id])
                results[sen_id].update(sen)

        return sections, results

    def process_json(self, stream):
        """Runs the extraction pipeline on the input stream

        Args:
            stream (json): The json file We want to run our pipeline on, each line contains
            a document and the documents consist of sections. Each section contains multiple sentences

        Yields:
            json: The json file annotated by our rule extraction system
        """
        for line in stream:
            doc = json.loads(line.strip())
            doc_id = doc["id"]
            logging.debug(doc_id)

            doc["sections"], _ = self.run_on_sections(doc["sections"])

            yield doc


@contextmanager
def get_extractor(args):
    """Returns an Extractor class initialized as a ContextManager.
    This helps dealing with errors as it saves the cache even if an error occurs.
    We initialize Rule or AttributeExtractor based on its arguments.

    Args:
        args: determines whether we use the old or the new version of the Extractor.

    Yields:
        AttributeExtractor or RuleExtractor with the initialized CachedStanzaPipeline
    """
    nlp_pipeline = CustomStanzaPipeline(processors="tokenize,mwt,pos,lemma,depparse")
    nlp_cache = os.path.join(args.cache_dir, "nlp_cache.json")
    with CachedStanzaPipeline(nlp_pipeline, nlp_cache) as nlp:
        if args.rule_ext:
            from brise_plandok.rule_extractor import RuleExtractor

            logging.warning("initializing old rule extractor (RuleExtractor)")
            yield RuleExtractor(nlp, cache_dir=args.cache_dir)
        else:
            from brise_plandok.attr_extractor import AttributeExtractor

            logging.warning("initializing new attribute extractor (AttributeExtractor)")
            yield AttributeExtractor(nlp, cache_dir=args.cache_dir)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-cd", "--cache-dir", default="cache", type=str)
    parser.add_argument("-r", "--rule-ext", default=False, action="store_true")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " + "%(module)s (%(lineno)s) - %(levelname)s - %(message)s",
    )
    args = get_args()

    with get_extractor(args) as extractor:
        for doc in extractor.process_json(sys.stdin):
            print(json.dumps(doc))


if __name__ == "__main__":
    main()
