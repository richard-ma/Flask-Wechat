# -*- coding: utf-8 -*-

from urllib import urlencode
import unittest
from flask_wechat import app

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
