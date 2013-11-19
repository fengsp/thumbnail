# -*- encoding: utf-8 -*-
# import json
import os

from flask import Blueprint
from flask import request, Response
from flask import abort
from PIL import Image
from models import thumb_q


thumb = Blueprint('thumb', __name__)
    
    
def thumbnail(src_file, dest_dir, width, height):
    src_file = os.path.join('/tmp', src_file)
    dest_dir = '/tmp/thumbnail'
    if not os.path.exists(src_file):
        raise Exception('src_file does not exists')
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    
    im = Image.open(src_file)
    im_dup = im.copy()
    im_dup.thumbnail((width, height), Image.ANTIALIAS)

    basename = os.path.basename(src_file)
    filename, ext = os.path.splitext(basename)
    targetname = filename + '_' + str(width) + '_' + str(height) + ext
    
    im_dup.save(os.path.join(dest_dir, targetname))
    


@thumb.route('/<image>/')
def index(image):
    width = request.args.get('w', None)
    height = request.args.get('h', None)
    try:
        width = int(width)
        height = int(height)
    except:
        abort(400)
    
    thumb_q.enqueue(thumbnail, args=(image, '', width, height,))
    return Response('1')
