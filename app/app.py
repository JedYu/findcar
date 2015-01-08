#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handler import WechatHandler,BaseHandler

class CarHandler(WechatHandler):

    def get(self):
        signature = self.get_argument('signature', None)
        timestamp = self.get_argument('timestamp', None)
        nonce = self.get_argument('nonce', None)
        echostr = self.get_argument('echostr', None)

        if self.wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.abort(403)




class PageNotFound(BaseHandler):
    def get(self):
        self.abort(404)


handlers = [('/car', CarHandler),
            (r'.*', PageNotFound),
]
