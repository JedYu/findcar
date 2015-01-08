#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import tornado.web
from app import handlers as handler
from config import DEBUG


class Application(tornado.web.Application):
    def __init__(self):
        handlers = handler
        settings = dict(
            autoescape = None,
            debug = DEBUG,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
