from brise_plandok.annotation_process.utils.constants import DOC_HEADER
import json
import sys


def sum_sens_for_docs(df, doc_ids):
    doc_id_col = DOC_HEADER[1]
    nr_sens_col = DOC_HEADER[4]
    return df[nr_sens_col][df[doc_id_col].isin(doc_ids)].sum()


def count_sentences_in_doc(doc):
    cnt = 0
    for section in doc["sections"]:
        if _ignore_section(section):
            continue
        cnt += len((section["sens"]))
    return cnt


def _ignore_section(section):
    return section["text"] == "" or section["id"] == 0


def main():
    for line in sys.stdin:
        doc = json.loads(line.strip())
        print(f"{doc['id']}\t{count_sentences_in_doc(doc)}")


if __name__ == "__main__":
    main()
