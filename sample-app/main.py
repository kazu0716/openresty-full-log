# -*- coding: utf-8 -*-
import gzip
import json

from flask import Flask, abort, jsonify, request

app = Flask(__name__)


@app.route('/large_res_body', methods=['POST'])
def large_res():
    with gzip.open("res_body.json.gz", "rt", "utf_8") as f:
        body = json.load(f)
    res = jsonify(body)
    res.headers['account_id'] = 11111111
    return res, 201

@app.route('/small_res_body', methods=['POST'])
def small_res():
    res = jsonify({"test": "test"})
    res.headers['account_id'] = 11111111
    return res, 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
