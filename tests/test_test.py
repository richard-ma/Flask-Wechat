# -*- coding: utf-8 -*-

from urllib import urlencode
import unittest
import app

class FlaskWechatTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def testCheckSignature(self):
        rv = self.app.get('/')
        assert 'Signature check failed' == rv.data

        query = {
            'signature': '',
            'timestamp': '',
            'nonce': '',
            'echostr': '',
        }
        rv = self.app.get('/%s' % (urlencode(query)))
        assert 'Signature check failed' == rv.data
