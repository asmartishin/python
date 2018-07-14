#!/usr/bin/env python

import argparse

from flask import Flask, request, Response

app = Flask(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080)
    return parser.parse_args()


@app.route('/', methods=['POST'])
def root():
    data = request.get_json(force=True)
    app.logger.info(data)
    return Response(status=200)


if __name__ == '__main__':
    args = parse_args()
    app.run(host='::', port=args.port, debug=True)

