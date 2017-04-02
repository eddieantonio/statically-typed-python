#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, request
from css import css as _


app = Flask(__name__)


@app.route('/')
def home():
    return _('''
        <form action="/" method="POST">
            <label> a = <input name=a> </label><br />
            <label> b = <input name=b> </label><br />
            <button type=submit> Add! </button>
        </form>
    ''')


@app.route('/', methods=['POST'])
def add_integers():
    a = request.form['a']
    b = request.form['b']
    answer = a + b
    return _('''
        <main>{a} + {b} = {answer}</main>
    '''.format(a=a, b=b, answer=answer))


if __name__ == '__main__':
    app.run(debug=True)
