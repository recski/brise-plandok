import argparse
from brise_plandok.data_split.utils.xlsx import distribute_xlsx_files, genereate_xlsx_files
from brise_plandok.data_split.utils.assignments import fill_assigments_with_batch
from brise_plandok.data_split.utils.cycles import get_cycle
from brise_plandok.data_split.assignment_loader import load_assignments
from brise_plandok.data_split.sentence_stat import calculate_sentence_counts
from brise_plandok.data_split.utils.doc_tracking import get_next_batch, load_doc_tracking_data
from brise_plandok.data_split.utils.assignments import get_assignment
import logging


def generate_batch(doc_tracking_file, batch_size, json_folder, cycle_nr, annotators_folder, xlsx_folder, generate_xlsx, override, update):
    docs = load_doc_tracking_data(doc_tracking_file)
    next_docs = get_next_batch(docs, batch_size)
    logging.info(f"next documents to assign: {next_docs}")

    calculate_sentence_counts(docs, next_docs, json_folder)

    cycle_df = get_cycle(cycle_nr)
    assignment_df = load_assignments(docs, annotators_folder)
    partition = get_assignment(next_docs)
    logging.info(f"partition: {partition}")

    fill_assigments_with_batch(docs, cycle_df, assignment_df, partition)
    logging.info(f"assignments with new batch:\n{assignment_df}")

    if not generate_xlsx:
        logging.info(f"No xlsx files will be generated. Job done")
        return
    
    genereate_xlsx_files(next_docs, json_folder, xlsx_folder, override)
    distribute_xlsx_files(xlsx_folder, assignment_df, annotators_folder)


    # copy excels to annotator folders
    # update assigments
    # update dataset
    pass
    # To do
    # - error handling
    # - documentation
    # - logging


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    parser.add_argument("-jf", "--json-folder", type=str)
    parser.add_argument("-c", "--cycle", type=int)
    parser.add_argument("-af", "--annotators-folder", type=str)
    parser.add_argument("-xf", "--xlsx-folder", type=str, default=None)
    parser.add_argument("-g", "--generate-xlsx",
                        default=False, action="store_true")
    parser.add_argument("-o", "--override", default=False, action="store_true")
    parser.add_argument("-u", "--update", default=False, action="store_true")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    generate_batch(args.dataset_file, args.batch_size, args.json_folder, args.cycle,
                   args.annotators_folder, args.xlsx_folder, args.generate_xlsx, args.override, args.update)


if __name__ == "__main__":
    main()
