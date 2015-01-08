#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from config import TOKEN
from wechat.wechat import WechatApi

class BaseHandler(tornado.web.RequestHandler):

    def abort(self, code):
        raise tornado.web.HTTPError(code)


class WechatHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.wechat =  WechatApi(TOKEN)


    def abort(self, code):
        raise tornado.web.HTTPError(code)
