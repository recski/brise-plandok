# Python program to read an excel file

# import openpyxl module
import openpyxl
import argparse
from openpyxl.comments import Comment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Alignment
from collections import defaultdict


class Annotate:

    def parse(self, dataset, template, save):
        sentences = []
        labels = []
        sentence_ids = []

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

        # comment = Comment("New attributes can be added here that is not found in the dropdown lists",
        #     "Adam")
        # sheet_obj["H1"].comment = comment

        for i, sen in enumerate(sentences):
            label = labels[i]
            sentence_id = "A" + str(i + 3)
            sentence = "B" + str(i + 3)

            attribute_B = "C" + str(i + 3)
            attribute_class_C = "D" + str(i + 3)

            attribute_D = "E" + str(i + 3)
            attribute_class_E = "F" + str(i + 3)

            attribute_F = "G" + str(i + 3)
            attribute_class_G = "H" + str(i + 3)

            attribute_H = "I" + str(i + 3)
            attribute_class_I = "J" + str(i + 3)

            attribute_J = "K" + str(i + 3)
            attribute_class_K = "L" + str(i + 3)

            sheet_obj[sentence] = sentences[i]
            sheet_obj[sentence_id] = sentence_ids[i]
            sheet_obj[sentence].alignment = Alignment(wrapText=True)
            sheet_obj[sentence_id].alignment = Alignment(wrapText=True)

            data_val.add(sheet_obj[attribute_B])
            data_val.add(sheet_obj[attribute_D])
            data_val.add(sheet_obj[attribute_F])
            data_val.add(sheet_obj[attribute_H])
            data_val.add(sheet_obj[attribute_J])

            data_val_subclass_B = DataValidation(
                type="list", formula1='==INDIRECT($C${0})'.format(str(i + 3)))
            sheet_obj.add_data_validation(data_val_subclass_B)
            data_val_subclass_B.add(sheet_obj[attribute_class_C])

            data_val_subclass_D = DataValidation(
                type="list", formula1='==INDIRECT($E${0})'.format(str(i + 3)))
            sheet_obj.add_data_validation(data_val_subclass_D)
            data_val_subclass_D.add(sheet_obj[attribute_class_E])

            data_val_subclass_F = DataValidation(
                type="list", formula1='==INDIRECT($G${0})'.format(str(i + 3)))
            sheet_obj.add_data_validation(data_val_subclass_F)
            data_val_subclass_F.add(sheet_obj[attribute_class_G])

            data_val_subclass_H = DataValidation(
                type="list", formula1='==INDIRECT($I${0})'.format(str(i + 3)))
            sheet_obj.add_data_validation(data_val_subclass_H)
            data_val_subclass_H.add(sheet_obj[attribute_class_I])

            data_val_subclass_J = DataValidation(
                type="list", formula1='==INDIRECT($K${0})'.format(str(i + 3)))
            sheet_obj.add_data_validation(data_val_subclass_J)
            data_val_subclass_J.add(sheet_obj[attribute_class_K])

            label_splited = label.strip().split(',')

            label_splited = list(set(label_splited))
            if len(label_splited) == 1 and label_splited[0]:
                sheet_obj[attribute_B] = attribute_to_attribute_class[label_splited[0]]
                sheet_obj[attribute_class_C] = label_splited[0]
                sheet_obj[attribute_B].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_C].alignment = Alignment(
                    wrapText=True)
            elif len(label_splited) == 2:
                sheet_obj[attribute_B] = attribute_to_attribute_class[label_splited[0]]
                sheet_obj[attribute_class_C] = label_splited[0]
                sheet_obj[attribute_B].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_C].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_D] = attribute_to_attribute_class[label_splited[1]]
                sheet_obj[attribute_class_E] = label_splited[1]
                sheet_obj[attribute_D].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_E].alignment = Alignment(
                    wrapText=True)
            elif len(label_splited) == 3:
                sheet_obj[attribute_B] = attribute_to_attribute_class[label_splited[0]]
                sheet_obj[attribute_class_C] = label_splited[0]
                sheet_obj[attribute_B].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_C].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_D] = attribute_to_attribute_class[label_splited[1]]
                sheet_obj[attribute_class_E] = label_splited[1]
                sheet_obj[attribute_D].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_E].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_F] = attribute_to_attribute_class[label_splited[2]]
                sheet_obj[attribute_class_G] = label_splited[2]
                sheet_obj[attribute_F].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_G].alignment = Alignment(
                    wrapText=True)
            elif len(label_splited) == 4:
                sheet_obj[attribute_B] = attribute_to_attribute_class[label_splited[0]]
                sheet_obj[attribute_class_C] = label_splited[0]
                sheet_obj[attribute_B].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_C].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_D] = attribute_to_attribute_class[label_splited[1]]
                sheet_obj[attribute_class_E] = label_splited[1]
                sheet_obj[attribute_D].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_E].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_F] = attribute_to_attribute_class[label_splited[2]]
                sheet_obj[attribute_class_G] = label_splited[2]
                sheet_obj[attribute_F].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_G].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_H] = attribute_to_attribute_class[label_splited[3]]
                sheet_obj[attribute_class_I] = label_splited[3]
                sheet_obj[attribute_H].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_I].alignment = Alignment(
                    wrapText=True)
            elif len(label_splited) == 5:
                sheet_obj[attribute_B] = attribute_to_attribute_class[label_splited[0]]
                sheet_obj[attribute_class_C] = label_splited[0]
                sheet_obj[attribute_B].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_C].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_D] = attribute_to_attribute_class[label_splited[1]]
                sheet_obj[attribute_class_E] = label_splited[1]
                sheet_obj[attribute_D].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_E].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_F] = attribute_to_attribute_class[label_splited[2]]
                sheet_obj[attribute_class_G] = label_splited[2]
                sheet_obj[attribute_F].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_G].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_H] = attribute_to_attribute_class[label_splited[3]]
                sheet_obj[attribute_class_I] = label_splited[3]
                sheet_obj[attribute_H].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_I].alignment = Alignment(
                    wrapText=True)

                sheet_obj[attribute_J] = attribute_to_attribute_class[label_splited[4]]
                sheet_obj[attribute_class_K] = label_splited[4]
                sheet_obj[attribute_J].alignment = Alignment(wrapText=True)
                sheet_obj[attribute_class_K].alignment = Alignment(
                    wrapText=True)

        wb_obj.save(save)


def main():
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
