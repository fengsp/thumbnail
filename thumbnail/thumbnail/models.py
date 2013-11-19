from flask import g, abort
from werkzeug.local import LocalProxy
from rq import Queue
from redis import StrictRedis

import thumbnail


def get_thumb_q():
    redis_conn = getattr(g, '_redis_conn', None)
    if redis_conn is None:
        try:
            redis_conn = g._redis_conn = StrictRedis(
                host=thumbnail.app.config['REDIS_HOST'], \
                port=thumbnail.app.config['REDIS_PORT'], \
                db=thumbnail.app.config['REDIS_DB'])
        except:
            abort(503)
    thumb_q = Queue('thumb', connection=redis_conn)
    return thumb_q


thumb_q = LocalProxy(get_thumb_q)
