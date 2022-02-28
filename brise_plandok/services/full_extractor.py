import argparse
import os
from logging.config import dictConfig

from flask import Flask, abort, request

from brise_plandok.services.filter_predicted_attributes import filter_json
from brise_plandok.services.filter_psets import filter_psets
from brise_plandok.utils import load_json

HOST = "0.0.0.0"
PORT = 5000
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

DATA_DIR = None

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


@app.route("/brise-extract-api/<doc_id>", methods=["GET"])
def extract_full(doc_id):
    app.logger.info(f"Doc id {doc_id} was requested for full extraction")
    doc_fn = os.path.join(DATA_DIR, doc_id + ".json")
    if os.path.exists(doc_fn):
        return filter_json(load_json(doc_fn))
    else:
        return abort(404)


@app.route("/psets/<doc_id>", methods=["GET"])
def extract_psets(doc_id):
    full = request.args.get("full", default=False, type=lambda v: v.lower() == "true")
    app.logger.info(f"Doc id {doc_id} was requested for psets")
    doc_fn = os.path.join(DATA_DIR, doc_id + ".json")
    if os.path.exists(doc_fn):
        return filter_psets(load_json(doc_fn), full)
    else:
        return abort(404)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--data-directory", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    DATA_DIR = args.data_directory
    app.logger.info(f"Application is started with data folder {DATA_DIR}")
    app.run(debug=True, host=HOST, port=PORT)
