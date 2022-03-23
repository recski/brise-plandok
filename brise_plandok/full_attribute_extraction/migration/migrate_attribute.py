import argparse
import logging

from xpotato.dataset.dataset import Dataset
from xpotato.graph_extractor.extract import FeatureEvaluator

from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import AttributeFields, AttributeTypes, SenToAttrFields
from brise_plandok.full_attribute_extraction.attribute.potato.utils import load_features
from brise_plandok.full_attribute_extraction.type.extract_types import match_types
from brise_plandok.full_attribute_extraction.value.extract_values import match_values
from brise_plandok.utils import update_gold_docs

DUMMY_LABEL = "dummy"
GRAPH_FORMAT = "fourlang"


def migrate_attribute(gold_folder, input_attribute, output_attributes, values):
    evaluator = FeatureEvaluator()
    sen_to_gold_attrs = SenToAttrMap(
        gold_dir=gold_folder,
        fuzzy=False,
        full=True,
        attributes=[input_attribute],
        values_map={input_attribute: values},
    )
    sens_to_update = len(sen_to_gold_attrs.sen_to_attr.keys())
    print(f"Number of different texts to update: {sens_to_update}")
    predicted = _predict_output_attributes(evaluator, output_attributes, sen_to_gold_attrs)
    for text, entry in sen_to_gold_attrs.sen_to_attr.items():
        print(f"================================================")
        print(f"{sens_to_update} to go")
        old_attributes = entry[SenToAttrFields.ATTR]

        if [input_attribute] == output_attributes:
            predicted_attributes = [input_attribute]
        else:
            predicted_attributes = predicted.loc[predicted["Sentence"] == text][
                "Predicted label"
            ].to_list()[0]
        predicted_full_attributes = _predict_full_attributes(predicted_attributes, text)

        _check_suggestions(
            old_attributes, predicted_full_attributes, text, output_attributes, input_attribute
        )

        if input_attribute not in output_attributes:
            del old_attributes[input_attribute]

        print(f"\nNew attributes:\n{old_attributes}\n")
        print(f"Sentences to update: {entry[SenToAttrFields.SENS]}")
        input()
        update_gold_docs(
            gold_attr_candidate=old_attributes,
            gold_mod_candidate=entry[SenToAttrFields.MOD],
            current_gold_sens=entry[SenToAttrFields.SENS],
            gold_folder=gold_folder,
        )
        sens_to_update -= 1


def _check_suggestions(
    old_attributes,
    predicted_full_attributes,
    text,
    output_attributes,
    input_attribute,
):
    print(f"================================================\n\nText:\n{text}")
    print(f"\nOld attributes:\n\n{old_attributes}\n\n{old_attributes[input_attribute]}")
    print(f"\nMigrated attributes: {output_attributes}\n")
    print(f"{predicted_full_attributes}")
    take = input("\nTake it? (Enter=yes, else no)")
    if take == "":
        for migrated_attr, full_migrated_attr in predicted_full_attributes.items():
            old_attributes[migrated_attr] = full_migrated_attr
    else:
        while True:
            name_input = input(f"Name: ")
            if name_input == "-":
                break
            value_input = input(f"Value: ")
            type_input = _read_type()
            attr_input = {
                AttributeFields.NAME: name_input,
                AttributeFields.VALUE: [value_input],
                AttributeFields.TYPE: [type_input],
            }
            old_attributes[name_input] = attr_input
            done = input(f"{attr_input}\nDone? (Enter=yes, else no)")
            if done == "":
                break


def _read_type():
    while True:
        type_input_from_console = input(
            f"Type: - ( 0 : condition, 1 : content, 2 : conditionException, 3 : contentException )"
        )
        if type_input_from_console == "0":
            type_input = AttributeTypes.CONDITION
            break
        if type_input_from_console == "1":
            type_input = AttributeTypes.CONTENT
            break
        if type_input_from_console == "2":
            type_input = AttributeTypes.CONDITION_EXCEPTION
            break
        if type_input_from_console == "3":
            type_input = AttributeTypes.CONTENT_EXCEPTION
            break
    return type_input


def _predict_full_attributes(predicted_attributes, text):
    predicted_full_attributes = {}
    for new_attr in predicted_attributes:
        value = list(set([value for value in match_values(new_attr, text)]))
        attr_type = match_types(new_attr, text)
        predicted_full_attributes[new_attr] = {
            AttributeFields.NAME: new_attr,
            AttributeFields.VALUE: value,
            AttributeFields.TYPE: [attr_type],
        }
    return predicted_full_attributes


def _predict_output_attributes(evaluator, output_attributes, sen_to_gold_attrs):
    sentences = []
    for text in sen_to_gold_attrs.sen_to_attr.keys():
        sentences.append((text, DUMMY_LABEL))
    dataset = Dataset(sentences, label_vocab={"NO": 0, DUMMY_LABEL: 1}, lang="de")
    dataset.set_graphs(dataset.parse_graphs(graph_format=GRAPH_FORMAT))
    df = dataset.to_dataframe()
    rules_to_match = load_features(attributes=output_attributes)
    return evaluator.match_features(df, features=rules_to_match, multi=True)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    parser.add_argument("-i", "--input-attribute")
    parser.add_argument("-o", "--output-attributes", type=str, nargs="+")
    parser.add_argument("-v", "--values", type=str, nargs="+", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    migrate_attribute(args.gold_dir, args.input_attribute, args.output_attributes, args.values)
