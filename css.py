#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def css(html: str) -> str:
    return ('''
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;

            font: bold 10vh sans-serif;
            color: #333;
            background-color: #fcfcfc;
        }

        main {
            font-size: 20vh;
        }

        form label {
            display: inline-block;
            width: 6.5em;
        }

        form input {
            display: inline-block;
            float: right;
            width: 6em;

            font-weight: bold;
            font-size: 8vh;
        }

        form button {
            margin-top: 1vh;
            float: right;

            font-size: 8vh;
        }
    </style>
    ''' + html)
