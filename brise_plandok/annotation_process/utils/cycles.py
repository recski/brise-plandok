from brise_plandok.annotation_process.utils.constants import (
    ANNOTATORS,
    CYCLE_COL,
    CYCLE_FILE,
)
import itertools
import os
import pandas


def get_cycle(cycle_nr):
    df = pandas.read_csv(
        filepath_or_buffer=os.path.join(os.path.dirname(__file__), CYCLE_FILE),
        sep=";",
        dtype=_generate_dtype(),
    )
    cycle_df = df[df[CYCLE_COL] == cycle_nr].drop(CYCLE_COL, axis=1)
    _check_if_all_annotators_in_cycle(cycle_df, cycle_nr)
    return cycle_df


def _check_if_all_annotators_in_cycle(df, cycle_nr):
    annotators_from_cycle = set(itertools.chain(*df.values))
    for annotator in ANNOTATORS:
        if annotator not in annotators_from_cycle:
            raise ValueError(f"Annotator {annotator} is not in cycle {cycle_nr}.")


def _generate_dtype():
    dtype = {}
    for i in range(len(ANNOTATORS)):
        dtype["annotator_" + str(i + 1)] = str
    return dtype
