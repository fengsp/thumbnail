# -*- encoding: utf-8 -*-
# import json
from urllib import quote_plus, urlopen, urlencode
import time
import json

from flask import Module
thumb = Module(__name__)
from flask import render_template, request
from flask import redirect, abort
    
    
@thumb.route('/')
def index():
    return render_template('index.html')
