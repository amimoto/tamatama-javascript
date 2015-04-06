#!/usr/bin/python

"""
For this example, you'll need to install a number of python
modules that aren't marked as normal dependencies for walky.
You can get them automatically install via pip:

pip install -r python-requirements.txt

"""

import signal
import logging
import sys
import os
import datetime
import threading
import time

import flask

ASSETS_PATH = "assets"
STATIC_ASSETS_PATH = os.path.join(ASSETS_PATH,"static")
TEMPLATE_ASSETS_PATH = os.path.join(ASSETS_PATH,"templates")

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

# Create the Flask App that will let us do http requests
app = flask.Flask(__name__,
                template_folder=TEMPLATE_ASSETS_PATH,
                static_folder=STATIC_ASSETS_PATH
                )

@app.route("/")
def route_index():
    return flask.render_template("index.html")

app.run(host='0.0.0.0')
