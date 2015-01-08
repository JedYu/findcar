# -*- coding: utf-8 -*-
import hashlib
from exceptions import InvalidTokenError

class WechatApi(object):

    def __init__(self, token=None):
        self._token = token

    def check_signature(self, signature, timestamp, nonce):
        """
        验证微信消息真实性
        :param signature: 微信加密签名
        :param timestamp: 时间戳
        :param nonce: 随机数
        :return: 通过验证返回 True, 未通过验证返回 False
        """

        self._check_token()

        if not signature or not timestamp or not nonce:
            return False


        tmp_list = [self._token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = ''.join(tmp_list)

        if signature == hashlib.sha1(tmp_str).hexdigest():
            return True
        else:
            return False


    def _check_token(self):
        """
        检查 Token 是否存在
        :raises NeedParamError: Token 参数没有在初始化的时候提供
        """
        if not self._token:
            raise InvalidTokenError('Please provide Token parameter in the construction of class.')