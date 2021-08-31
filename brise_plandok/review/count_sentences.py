import json
import sys

def count_sentences(doc):
    cnt = 0
    for section in doc["sections"]:
        if section['text'] == "":
            continue
        cnt += len((section['sens']))
    print(f"{doc['id']};{cnt}")

def main():
    for line in sys.stdin:
        doc = json.loads(line.strip())
        count_sentences(doc)

if __name__ == "__main__":
    main()