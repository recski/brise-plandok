import json

def load_json(fn):
    with open(fn) as f:
        return json.load(f)

def dump_json(obj, fn):
    with open(fn, "w") as f:
        json.dump(obj, f)