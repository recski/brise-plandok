import json
import os
import re
import sys
# from itertools import chain

from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline
from tuw_nlp.text.utils import normalize_whitespace
from tqdm import tqdm


SEC_NUM_PATT = re.compile(
    r'^(?P<secnum>(?:II*\.|[1-9][0-9]?(\.[1-9][0-9]?)*[.\s]+)+)(?P<rest>$|[^0-9])')  # noqa

PAGE_NO_PATT = re.compile(r'^-[0-9][0-9]*-$')


class PlanDok():

    @staticmethod
    def from_file(fn):
        with open(fn) as f:
            txt = f.read()
            doc_id = os.path.basename(fn).replace('.txt', '')
            return PlanDok.from_txt(txt, doc_id)

    @staticmethod
    def from_txt(txt, doc_id):
        d = PlanDok(doc_id)
        d.txt = txt
        sections = d.get_sections(txt)
        d.sections = sections
        return d

    @staticmethod
    def from_dict(data):
        d = PlanDok(data['id'])
        d.sections = data['sections']
        return d

    def __init__(self, doc_id):
        self.id = doc_id
        self.sections = []
        self.tokenizer = None

    def to_dict(self):
        return {
            "id": self.id,
            "txt": self.txt,
            "sections": self.sections}

    def gen_tsv(self):
        for section in self.sections:
            for sen in section['sens']:
                yield f"{sen['sen_id']}\t{sen['text']}"

    def to_tsv(self):
        return "\n".join(sen for sen in self.gen_tsv())

    def get_sections(self, txt):
        sections = []
        curr_section = 'header'
        curr_text = ['']
        for raw_line in txt.split('\n'):
            line = raw_line.strip()
            if not line or PAGE_NO_PATT.match(line):
                if not line:
                    curr_text.append('')
                continue
            match = SEC_NUM_PATT.match(line)
            if match is None:
                if curr_text[-1].endswith('-'):
                    # sys.stderr.write(
                    #     curr_text[-1].split()[-1]+'\t'+line.split()[0]+'\n')
                    curr_text[-1] = curr_text[-1][:-1] + f'{line}'
                else:
                    curr_text[-1] += f' {line}'
            else:
                # sys.stderr.write('{0}\t{1}\n'.format(line, match.groups()))
                sections.append([curr_section, curr_text])
                curr_section = match.group('secnum').strip().replace(' ', '_')
                rest = SEC_NUM_PATT.sub(r'\g<rest>', line).strip()
                curr_text = [rest] if rest else ['']

        sections.append([curr_section, curr_text])

        sections = [
            {"id": i, "num": num, "text": " ".join([
                par for par in [
                    normalize_whitespace(sen) for sen in sec] if par])}
            for i, (num, sec) in enumerate(sections)]

        return sections

    def analyze(self, nlp):
        for section in self.sections:
            section['sens'] = []
            if section['text'] == "":
                continue
            # for i, sen in enumerate(chain(
            #         *(tokenizer.tokenize(par) for par in section['text']))):
            for i, sen in enumerate(
                    nlp(section['text']).sentences):
                section['sens'].append({
                    "sen_id": f"{self.id}_{section['id']}_{i}",
                    "text": sen.text,
                    "attributes": [],
                    "tokens": sen.to_dict()})


def main():
    with CachedStanzaPipeline(
            CustomStanzaPipeline(), 'cache/nlp_cache.json') as nlp:
        for fn in tqdm(sys.argv[1:]):
            doc = PlanDok.from_file(fn)
            doc.analyze(nlp)
            print(json.dumps(doc.to_dict()))


if __name__ == "__main__":
    main()
