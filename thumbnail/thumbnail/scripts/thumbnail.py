#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, sys
from multiprocessing import cpu_count, Process
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))))
reload(sys)
sys.setdefaultencoding('utf-8')

from rq import Queue, Connection, Worker
from redis import StrictRedis

from thumbnail.conf.settings import *


NUM_WORKERS = cpu_count() * 4


redis_conn = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def work():
    with Connection(connection=redis_conn):
        qs = [Queue('thumb')]
        w = Worker(qs)
        w.work()


for i in range(NUM_WORKERS):
    Process(target=work, args=()).start()
