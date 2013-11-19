"""
The project start file...
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
reload(sys)
sys.setdefaultencoding('utf-8')

# from gevent import monkey; monkey.patch_all()
from thumbnail import app
from thumbnail.conf.settings import DEBUG


if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host='0.0.0.0',port=8000)
