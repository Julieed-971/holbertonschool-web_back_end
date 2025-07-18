#!/usr/bin/env python3
"""Module for a basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('./templates/0-index.html')
