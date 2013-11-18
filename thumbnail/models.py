from flask import g, abort
from pymongo import MongoReplicaSetClient
from werkzeug.local import LocalProxy

from thumbnail import app


def get_user():
    client = getattr(g, '_database', None)
    if client is None:
        try:
            client = g._database = MongoReplicaSetClient(**MONGO_CONFIG)
        except:
            abort(503)
    db = client.woplus
    user = db.user
    return user


User = LocalProxy(get_user)


@app.teardown_appcontext
def close_connection(exception):
    client = getattr(g, '_database', None)
    if client is not None:
        client.close()
