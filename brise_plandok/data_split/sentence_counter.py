import json
import sys

def count_sentences_in_doc(doc):
    cnt = 0
    for section in doc["sections"]:
        if _ignore_section(section):
            continue
        cnt += len((section['sens']))
    return cnt

def _ignore_section(section):
    return section['text'] == "" or section['id'] == 0

def main():
    for line in sys.stdin:
        doc = json.loads(line.strip())
        print(f"{doc['id']}\t{count_sentences_in_doc(doc)}")

if __name__ == "__main__":
    main()