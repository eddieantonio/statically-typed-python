#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hola, mundo'


if __name__ == '__main__':
    app.run(debug=True)
