import json
import logging
import sys

def count_sentences(doc):
    cnt = 0
    for section in doc["sections"]:
        if section['text'] == "":
            continue
        cnt += len((section['sens']))
    print(f"{doc['id']};{cnt}")

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " + "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    for line in sys.stdin:
        doc = json.loads(line.strip())
        count_sentences(doc)

if __name__ == "__main__":
    main()