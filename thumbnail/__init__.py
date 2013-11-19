from flask import Flask

from .conf.settings import *
from .thumbnail.views import thumb
from .rq_dashboard import RQDashboard


app = Flask(__name__)
app.secret_key = 'thumbnailservice_secret_key'
app.register_blueprint(thumb, url_prefix='/thumbnail')
RQDashboard(app, url_prefix='/admin')


app.config['REDIS_HOST'] = REDIS_HOST
app.config['REDIS_PORT'] = REDIS_PORT
app.config['REDIS_DB'] = REDIS_DB
