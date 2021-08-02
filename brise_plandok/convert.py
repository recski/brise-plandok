"""
converter between plandok formats
JSON: the single JSON format produced by plandok.py and get_attributes.py
CSV_ATTR: annotation output (from excel)
CSV_FULL: sample from Bjoern, in csv, with all features

JSON is used as the internal format for conversion
"""
import argparse
import csv
import json
import logging
import sys
import os
import re
import brise_plandok.annotation
from brise_plandok.annotation.annotate import Annotate
from brise_plandok.annotation.attributes import ATTR_TO_CAT, ATTRS_BY_CAT
from brise_plandok.annotation.agreement import gen_sens_from_file


class Converter():
    input_formats = {"JSON", "CSV_ATTR", "CSV_FULL", "XLSX"}
    output_formats = {"JSON", "TXT", "XLSX"}  # , "CSV_ATTR", "CSV_FULL"}

    @staticmethod
    def check_attribute(curr_sen):
        for attribute in curr_sen["attributes"]:
            if attribute["name"] not in ATTR_TO_CAT:
                logging.warning(
                    f'Sen ID: {curr_sen["sen_id"]}, Attribute: {attribute["name"]} not in the Attribute list')

    @staticmethod
    def build_json(
            sen, attributes=None, sen_id=None, section_id=None,
            section_num=None, doc_id=None, modality=None):
        if isinstance(sen, dict):
            sentence = sen
        elif isinstance(sen, str):
            sentence = {
                "sen_id": sen_id, "text": sen, "attributes": attributes,
                "modality": [] if modality is None else modality}
        else:
            assert False

        return {
            "id": doc_id,
            "text": None,
            "sections": [{
                "id": section_id,
                "text": None,
                'num': section_num,
                "sens": [sentence]
            }]
        }

    @staticmethod
    def attrs_from_names(attrs):
        return [{"name": attr, "value": None, "type": None} for attr in attrs]

    @staticmethod
    def convert_to_logical_form(extracted_attributes):
        modality = extracted_attributes["modality"]
        attributes = extracted_attributes["attributes"]

        def normalize_attribute(attribute):
            numbers = re.compile(
                r"^(?P<number>\d+((,|\.)\d+)?)(?P<unit>m|m2|cm|cm2)$")

            if attribute and isinstance(attribute, str):
                if "Grad" in attribute:
                    attribute = attribute.split("Grad")[0]

                match = numbers.search(attribute)
                if match:
                    d = match.groupdict()
                    matched_number = d["number"]
                    unit = None
                    if "unit" in d:
                        unit = d["unit"]
                    number = matched_number.replace(",", ".")

                    multiply = {"m": 100, "m2": 10000, "cm": 1, "cm2": 1}

                    if unit:
                        number = int(float(number) * multiply[unit])
                    else:
                        number = int(float(number))

                    return str(number)
                else:
                    return attribute[0].lower() + attribute[1:]
            else:
                return attribute

        def normalize_attributes(attribute):
            return {"name": normalize_attribute(attribute["name"]),
                    "value": normalize_attribute(attribute["value"]),
                    "type": attribute["type"]}

        contents = [normalize_attributes(attribute) for attribute in attributes if attribute["type"] == "content"]  # noqa
        conditions = [normalize_attributes(attribute) for attribute in attributes if attribute["type"] == "condition"]  # noqa
        content_exceptions = [normalize_attributes(attribute) for attribute in attributes if attribute["type"] == "contentException"]  # noqa
        condition_exceptions = [normalize_attributes(attribute) for attribute in attributes if attribute["type"] == "conditionException"]  # noqa

        contents_string = []
        for content in contents:
            if content["value"] == True or content["value"] == None:
                contents_string.append(content["name"])
            elif content["value"] == False:
                contents_string.append(f'neg {content["name"]}')
            else:
                contents_string.append(
                    f'{content["name"]}({content["value"]})')
        contents_string = " and ".join(contents_string)

        conditions_string = []
        for condition in conditions:
            if condition["value"] == True or condition["value"] == None:
                conditions_string.append(condition["name"])
            elif condition["value"] == False:
                conditions_string.append(f'neg {condition["name"]}')
            else:
                conditions_string.append(
                    f'{condition["name"]}({condition["value"]})')
        conditions_string = " and ".join(conditions_string)

        content_exceptions_string = []
        for content_exception in content_exceptions:
            if content_exception["value"] == True or content_exception["value"] == None:
                content_exceptions_string.append(content_exception["name"])
            elif content_exception["value"] == False:
                content_exceptions_string.append(
                    f'neg {content_exception["name"]}')
            else:
                content_exceptions_string.append(
                    f'{content_exception["name"]}({content_exception["value"]})')
        content_exceptions_string = " or ".join(content_exceptions_string)

        condition_exceptions_string = []
        for condition_exception in condition_exceptions:
            if condition_exception["value"] == True or condition_exception["value"] == None:
                condition_exceptions_string.append(condition_exception["name"])
            elif condition_exception["value"] == False:
                condition_exceptions_string.append(
                    f'neg {condition_exception["name"]}')
            else:
                condition_exceptions_string.append(
                    f'{condition_exception["name"]}({condition_exception["value"]})')
        condition_exceptions_string = " or ".join(condition_exceptions_string)

        logical_form = ""
        prover_form = ""

        if modality == "obligation" or modality == "permission":
            if contents:
                logical_form += contents_string
            if content_exceptions:
                logical_form += f' or {content_exceptions_string}'
            if conditions:
                logical_form += f', {conditions_string}'

            logical_form = f'obl({logical_form})'
            prover_form = logical_form

            if condition_exceptions:
                exception_logical_form = ""
                if contents:
                    exception_logical_form += contents_string
                if content_exceptions:
                    exception_logical_form += f' or {content_exceptions_string}'

                exception_logical_form = f'neg({exception_logical_form})'
                exception_logical_form += f', {condition_exceptions_string}'

                prover_form = f'{logical_form} and per({exception_logical_form})'
                logical_form = f'{logical_form}, per({exception_logical_form})'

        elif modality == "prohibition":
            if contents:
                logical_form += contents_string
            if content_exceptions:
                logical_form += f' and neg {content_exceptions_string}'
            if conditions:
                logical_form += f', {conditions_string}'

            logical_form = f'for({logical_form})'
            prover_form = logical_form

            if condition_exceptions:
                exception_logical_form = ""
                if contents:
                    exception_logical_form += contents_string
                if content_exceptions:
                    exception_logical_form += f' and neg {content_exceptions_string}'

                if condition_exception:
                    exception_logical_form += f', {condition_exceptions_string}'

                prover_form = f'{logical_form} and per({exception_logical_form})'
                logical_form = f'{logical_form}, per({exception_logical_form})'

        return logical_form, prover_form

    def __init__(self, args):
        assert args.input_format in Converter.input_formats
        assert args.output_format in Converter.output_formats
        self.input_format = args.input_format
        self.output_format = args.output_format
        self.output_file = args.output_file

    def postprocess_full(self, sen):
        if len(sen['modality']) > 1:
            logging.warning(
                f'multiple modalities given for sentence {sen["sen_id"]}')

        sen['modality'] = sorted(sen['modality'])
        return Converter.build_json(sen)

    def read_csv_full(self, stream):
        yield from (
            self.postprocess_full(sen) for sen in self._read_csv_full(stream))

    def _read_csv_full(self, stream):
        curr_sen = None
        for i, row in enumerate(
                csv.reader(stream, delimiter=";", quotechar='"')):
            if i == 0:
                continue
            fields = [s if s not in ('N/A', '') else None for s in row[1:7]]
            if fields[0] is None:
                assert fields[1] is None
            elif curr_sen and fields[0] == curr_sen['sen_id']:
                # sometimes the id and text are repeated
                pass
            else:
                if curr_sen:
                    Converter.check_attribute(curr_sen)
                    yield curr_sen
                sen_id, text = fields[:2]
                curr_sen = {
                    "sen_id": sen_id, "text": text,
                    'modality': set(), "attributes": []}

            attr, cat, note, value = fields[2:]
            if not attr:
                assert not cat and not value
                continue
            if cat == 'modal':
                curr_sen['modality'].add(attr)
            else:
                curr_sen['attributes'].append({
                    "type": cat,
                    "name": attr,
                    "value": value})
        if curr_sen:
            Converter.check_attribute(curr_sen)
            yield curr_sen

    def read_csv_attr(self, stream):
        for i, row in enumerate(
                csv.reader(stream, delimiter=",", quotechar='"')):
            if i == 0:
                has_id = row[0] == 'Sentence_ID'
            if i < 2:
                continue

            sen_id, sen, rest = (
                (row[0], row[1], row[2:])
                if has_id else (f'{i}', row[0], row[1:]))

            attrs = [
                field for j, field in enumerate(rest)
                if field and j in (1, 3, 5, 7)]

            attributes = Converter.attrs_from_names(attrs)
            logging.warning(attributes)
            yield Converter.build_json(
                sen, attributes=attributes, sen_id=sen_id, modality=None)

    def read_xlsx(self, stream):
        sens = [Converter.build_json(line["text"], attributes=line["attributes"], sen_id=line["id"], modality=None)[
            "sections"][0]["sens"][0] for line in gen_sens_from_file(stream)]

        for sen in sens:
            atts = []
            for attribute in sen["attributes"]:
                atts.append({
                    "type": None,
                    "name": attribute,
                    "value": None})
            sen["attributes"] = atts

        doc = {
            "id": None,
            "text": None,
            "sections": [{
                "id": None,
                "text": None,
                'num': None,
                "sens": sens
            }]
        }

        yield doc

    def read_json(self, stream):
        for line in stream:
            yield json.loads(line)

    def read(self, stream):
        if self.input_format == 'JSON':
            yield from self.read_json(stream)
        elif self.input_format == 'CSV_ATTR':
            yield from self.read_csv_attr(stream)
        elif self.input_format == 'CSV_FULL':
            yield from self.read_csv_full(stream)
        elif self.input_format == "XLSX":
            yield from self.read_xlsx(stream)
        else:
            assert False

    def write_json(self, doc, stream):
        stream.write(json.dumps(doc))
        stream.write('\n')

    def write_xlsx(self, doc, file):
        annotate = Annotate()
        dataset = []
        for section in doc["sections"]:
            for sen in section["sens"]:
                attrs_text = ",".join(
                    attr['name'] for attr in sen['attributes'])
                dataset.append((sen["sen_id"], sen["text"], attrs_text))
        annotate.parse(dataset, os.path.join(os.path.dirname(
            brise_plandok.annotation.__file__), "BRISE.xlsx"), file)

    def write_txt(self, doc, stream):
        for section in doc["sections"]:
            for sen in section["sens"]:
                attrs_text = ",".join(
                    attr['name'] for attr in sen['attributes'])
                line = '\t'.join([sen['sen_id'], sen['text'], attrs_text])
                stream.write(f"{line}\n")

    def write(self, doc, stream):
        if self.output_format == 'JSON':
            self.write_json(doc, stream)
        elif self.output_format == 'TXT':
            self.write_txt(doc, stream)
        elif self.output_format == "XLSX":
            self.write_xlsx(doc, stream)
        else:
            assert False

    def convert(self, input_stream, output_stream):
        for doc in self.read(input_stream):
            self.write(doc, output_stream)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input-format", type=str)
    parser.add_argument("-o", "--output-format", type=str)
    parser.add_argument("-if", "--input-file", type=str, default=None)
    parser.add_argument("-of", "--output-file", type=str, default=None)
    parser.set_defaults(input_format="JSON", output_format="JSON")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    converter = Converter(args)

    if args.input_format == "XLSX":
        assert args.input_file
    if args.output_format == "XLSX":
        assert args.output_file

    input_stream = args.input_file if args.input_file != None else sys.stdin
    output_stream = args.output_file if args.output_file != None else sys.stdout

    converter.convert(input_stream, output_stream)


if __name__ == "__main__":
    main()
