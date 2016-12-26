# -*- coding: utf-8 -*-

import unittest
from flask_wechat import app
try:
    from urllib import urlencode
except: #Python3
    from urllib.parse import urlencode

class FlaskWechatTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def testCheckSignature(self):
        rv = self.app.get('/')
        assert 404 == rv.status_code

        query = {
            'signature': 'failed',
            'timestamp': 'failed',
            'nonce': 'failed',
            'echostr': 'failed',
        }
        queryStr = '/%s' % (urlencode(query))
        rv = self.app.get(queryStr)
        assert 404 == rv.status_code
