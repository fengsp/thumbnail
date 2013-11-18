"""
The project start file...
"""
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
reload(sys)
sys.setdefaultencoding('utf-8')

#from gevent import monkey; monkey.patch_all()

from thumbnail import app
from thumbnail.views import thumb
from thumbnail.conf.settings import DEBUG


app.register_module(thumb)


if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host='0.0.0.0',port=8000)
