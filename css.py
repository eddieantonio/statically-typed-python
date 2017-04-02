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

        form button {
            font-size: 8vh;
            float: right;
        }

        main {
            font-size: 20vh;
        }

        form input {
            font-size: 8vh;
            max-width: 6em;
        }
    </style>
    ''' + html)
