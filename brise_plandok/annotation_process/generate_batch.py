import argparse

from brise_plandok import logger
from brise_plandok.annotation_process.assignment_loader import load_assignments
from brise_plandok.annotation_process.sentence_stat import calculate_sentence_counts
from brise_plandok.annotation_process.utils.assignments import (
    fill_assignments_with_batch,
)
from brise_plandok.annotation_process.utils.assignments import get_assignment
from brise_plandok.annotation_process.utils.cycles import get_cycle
from brise_plandok.annotation_process.utils.data import generate_data
from brise_plandok.annotation_process.utils.doc_tracking import (
    get_next_batch,
    load_doc_tracking_data,
    save_doc_tracking_data,
)
from brise_plandok.annotation_process.utils.xlsx import (
    distribute_xlsx_files,
    genereate_xlsx_files,
)


def generate_batch(
    doc_tracking_file,
    batch_size,
    json_folder,
    cycle_nr,
    annotators_folder,
    generate_xlsx,
    xlsx_folder,
    data_folder,
    overwrite,
    update,
    phase,
):
    docs_df = load_doc_tracking_data(doc_tracking_file)
    next_doc_ids = get_next_batch(docs_df, batch_size, True, phase)
    logger.info(f"next documents to assign: {next_doc_ids}")

    calculate_sentence_counts(docs_df, next_doc_ids, json_folder)

    cycle_df = get_cycle(cycle_nr)
    logger.info(f"cycle ({cycle_nr}):\n {cycle_df}")
    assignment_df = load_assignments(docs_df, annotators_folder, phase)
    partition = get_assignment(next_doc_ids, docs_df, cycle_df.shape[0])
    logger.info(f"partition: {partition}")

    fill_assignments_with_batch(docs_df, cycle_df, assignment_df, partition, next_doc_ids, phase)
    logger.info(f"assignments with new batch:\n{assignment_df}")

    if not generate_xlsx:
        logger.info("No xlsx files will be generated. Job done")
        return

    docs = generate_data(next_doc_ids, json_folder, data_folder, phase)
    genereate_xlsx_files(docs, xlsx_folder, overwrite, phase)
    distribute_xlsx_files(xlsx_folder, assignment_df, annotators_folder, update, phase)

    if update:
        save_doc_tracking_data(doc_tracking_file, docs_df)
        logger.info(f"tracking data {doc_tracking_file} was updated")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    parser.add_argument("-jf", "--json-folder", type=str)
    parser.add_argument("-c", "--cycle", type=int)
    parser.add_argument("-af", "--annotators-folder", type=str)
    parser.add_argument("-xf", "--xlsx-folder", type=str, default=None)
    parser.add_argument("-df", "--data-folder", type=str, default=None)
    parser.add_argument("-g", "--generate-xlsx", default=False, action="store_true")
    parser.add_argument("-o", "--overwrite", default=False, action="store_true")
    parser.add_argument("-u", "--update", default=False, action="store_true")
    parser.add_argument("-p", "--phase", default=1, type=int)
    return parser.parse_args()


def main():
    args = get_args()
    generate_batch(
        args.dataset_file,
        args.batch_size,
        args.json_folder,
        args.cycle,
        args.annotators_folder,
        args.generate_xlsx,
        args.xlsx_folder,
        args.data_folder,
        args.overwrite,
        args.update,
        args.phase,
    )


if __name__ == "__main__":
    main()
