#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template

basedir = os.path.abspath(os.path.dirname(__file__))

APP_PORT = 8000

# FLASK APP INIT
app = Flask(__name__, template_folder="templates", static_folder="assets")
# CSRF SETTINGS
WTF_CSRF_ENABLED = False

# FLASK LOGIN MANAGER
app.config['SECRET_KEY'] = \
'FDom\r\xad\xa6\xb8b\xb0\xea\xce\t\xca\x9d\xc7pgV\x00\xe0\x12\x116'
