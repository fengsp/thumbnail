# -*- encoding: utf-8 -*-
import os


DEBUG = False
if os.path.exists(os.path.join(os.path.dirname(__file__), 'debug')):
    DEBUG = True


if DEBUG:
    REDIS_HOST = '192.168.4.167'
    REDIS_PORT = 6379
    REDIS_DB = 0
