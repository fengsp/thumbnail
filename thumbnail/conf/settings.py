# -*- encoding: utf-8 -*-
import os


DEBUG = False
if os.path.exists(os.path.join(os.path.dirname(__file__), 'debug')):
    DEBUG = True
