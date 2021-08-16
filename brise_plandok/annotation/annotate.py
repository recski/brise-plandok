# Python program to read an excel file

# import openpyxl module
import openpyxl
import argparse
import logging
from openpyxl.comments import Comment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Alignment, Font, PatternFill
from collections import defaultdict
from brise_plandok.annotation.attributes import ATTR_TO_CAT, ATTRS_BY_CAT

class Annotate:

    def parse(self, dataset, template, save):
        sentences = []
        labels = []
        sentence_ids = []

        logging.info('started the creation of the excel sheet')
        normalize_lab = {"PlanzeichenBBID": "Planzeichen", "VerkehrsflaecheID": "Verkehrsflaeche_ID",
                         "BauweiseID": "Bauweise_ID", "WidmungID": "WidmungUndZweckbestimmung", "BauklasseID": "Bauklasse", "TechnischeUndBelichtungsAufbautenZulaessig": "AufbautenZulaessig"}
        for line in dataset:
            sentence_ids.append(line[0])
            sentences.append(line[1])
            label = ",".join(
                [normalize_lab[l] if l in normalize_lab else l for l in line[2].split(",")])
            labels.append(label)

        # Give the location of the file
        path = template

        # To open the workbook
        # workbook object is created
        wb_obj = openpyxl.load_workbook(path)

        # Get workbook active sheet object
        # from the active attribute
        sheet_obj = wb_obj.active

        # Read in the attributes
        attribute_to_attribute_class = defaultdict(str)
        sheet_obj_labels = wb_obj["Label"]
        for i in range(ord('F'), ord('T') + 1):
            attrs = []
            for col in sheet_obj_labels[chr(i)]:
                if col.value:
                    attrs.append(col.value)
            for attr in attrs[1:]:
                attribute_to_attribute_class[attr] = attrs[0]

        sheet_obj.insert_rows(idx=3, amount=len(sentences))

        data_val = DataValidation(type="list", formula1='=Attribute')
        sheet_obj.add_data_validation(data_val)

        for i, _ in enumerate(sentences):
            label = labels[i]
            excel_row_id = i + 3

            sentence_id = "A" + str(excel_row_id)
            sentence = "B" + str(excel_row_id)

            attribute_C = "C" + str(excel_row_id)
            attribute_class_D = "D" + str(excel_row_id)

            attribute_E = "E" + str(excel_row_id)
            attribute_class_F = "F" + str(excel_row_id)

            attribute_G = "G" + str(excel_row_id)
            attribute_class_H = "H" + str(excel_row_id)

            attribute_I = "I" + str(excel_row_id)
            attribute_class_J = "J" + str(excel_row_id)

            attribute_K = "K" + str(excel_row_id)
            attribute_class_L = "L" + str(excel_row_id)

            sheet_obj[sentence] = sentences[i]
            sheet_obj[sentence_id] = sentence_ids[i]
            sheet_obj[sentence].alignment = Alignment(wrapText=True)
            sheet_obj[sentence_id].alignment = Alignment(wrapText=True)

            if sentence_ids[i].split("_")[-2] == "0":
                for j in range(ord('C'), ord('P') + 1):
                    cell_id = chr(j)+str(excel_row_id)
                    sheet_obj[cell_id] = "DON'T ANNOTATE THIS SENTENCE"
                    sheet_obj[cell_id].fill = PatternFill(
                        fgColor="878787", fill_type="solid")
                    sheet_obj[cell_id].alignment = Alignment(wrapText=True, horizontal="center", vertical="center")
                    sheet_obj[cell_id].font = Font(bold=True)
            else:
                data_val.add(sheet_obj[attribute_C])
                data_val.add(sheet_obj[attribute_E])
                data_val.add(sheet_obj[attribute_G])
                data_val.add(sheet_obj[attribute_I])
                data_val.add(sheet_obj[attribute_K])

                data_val_subclass_C = DataValidation(
                    type="list", formula1='==INDIRECT($C${0})'.format(str(excel_row_id)))
                sheet_obj.add_data_validation(data_val_subclass_C)
                data_val_subclass_C.add(sheet_obj[attribute_class_D])

                data_val_subclass_E = DataValidation(
                    type="list", formula1='==INDIRECT($E${0})'.format(str(excel_row_id)))
                sheet_obj.add_data_validation(data_val_subclass_E)
                data_val_subclass_E.add(sheet_obj[attribute_class_F])

                data_val_subclass_G = DataValidation(
                    type="list", formula1='==INDIRECT($G${0})'.format(str(excel_row_id)))
                sheet_obj.add_data_validation(data_val_subclass_G)
                data_val_subclass_G.add(sheet_obj[attribute_class_H])

                data_val_subclass_I = DataValidation(
                    type="list", formula1='==INDIRECT($I${0})'.format(str(excel_row_id)))
                sheet_obj.add_data_validation(data_val_subclass_I)
                data_val_subclass_I.add(sheet_obj[attribute_class_J])

                data_val_subclass_K = DataValidation(
                    type="list", formula1='==INDIRECT($K${0})'.format(str(excel_row_id)))
                sheet_obj.add_data_validation(data_val_subclass_K)
                data_val_subclass_K.add(sheet_obj[attribute_class_L])

                label_splited = label.strip().split(',')

                label_splited = list(set(label_splited))

                cleaned_labels = label_splited.copy()
                for l in label_splited:
                    if l and l not in ATTR_TO_CAT:
                        logging.warning(
                            f"{l} attribute not in the attribute list, will be skipped!")
                        cleaned_labels.remove(l)

                label_splited = cleaned_labels

                if len(label_splited) > 0 and label_splited[0]:
                    sheet_obj[attribute_C] = attribute_to_attribute_class[label_splited[0]]
                    sheet_obj[attribute_class_D] = label_splited[0]
                    sheet_obj[attribute_C].alignment = Alignment(wrapText=True)
                    sheet_obj[attribute_class_D].alignment = Alignment(
                        wrapText=True)

                if len(label_splited) > 1:
                    sheet_obj[attribute_E] = attribute_to_attribute_class[label_splited[1]]
                    sheet_obj[attribute_class_F] = label_splited[1]
                    sheet_obj[attribute_E].alignment = Alignment(wrapText=True)
                    sheet_obj[attribute_class_F].alignment = Alignment(
                        wrapText=True)

                if len(label_splited) > 2:
                    sheet_obj[attribute_G] = attribute_to_attribute_class[label_splited[2]]
                    sheet_obj[attribute_class_H] = label_splited[2]
                    sheet_obj[attribute_G].alignment = Alignment(wrapText=True)
                    sheet_obj[attribute_class_H].alignment = Alignment(
                        wrapText=True)

                if len(label_splited) > 3:
                    sheet_obj[attribute_I] = attribute_to_attribute_class[label_splited[3]]
                    sheet_obj[attribute_class_J] = label_splited[3]
                    sheet_obj[attribute_I].alignment = Alignment(wrapText=True)
                    sheet_obj[attribute_class_J].alignment = Alignment(
                        wrapText=True)

                if len(label_splited) > 4:
                    sheet_obj[attribute_K] = attribute_to_attribute_class[label_splited[4]]
                    sheet_obj[attribute_class_L] = label_splited[4]
                    sheet_obj[attribute_K].alignment = Alignment(wrapText=True)
                    sheet_obj[attribute_class_L].alignment = Alignment(
                        wrapText=True)

        wb_obj.save(save)


def main():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s : " +
        "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    annotate = Annotate()
    parser = argparse.ArgumentParser(
        description='Create excel files for annotation.')
    parser.add_argument(
        '--dataset',
        required=True,
        help='the path to the dataset to be annotated')
    parser.add_argument(
        '--template',
        required=True,
        metavar='S',
        help='the initial excel to fill with the dataset')
    parser.add_argument(
        '--save',
        default="annotate.xlsx",
        metavar='S',
        help='where to save the excel')

    args = parser.parse_args()

    dataset = []
    with open(args.dataset) as f:
        for line in f:
            line = line.split("\t")
            sentence = line[1]
            sentence_id = line[0]
            label = line[2]
            dataset.append((sentence_id, sentence, label))

    annotate.parse(args.dataset, args.template, args.save)


if __name__ == "__main__":
    main()
