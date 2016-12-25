# -*- coding: utf-8 -*-

import os
from flask import Flask, request
from wechat_sdk import WechatConf, WechatBasic

app = Flask(__name__)

conf = WechatConf(
    #token = os.environ['WECHAT_TOKEN'],
    appid = os.environ['WECHAT_APPID'],
    appsecret = os.environ['WECHAT_SECRET'],
    #encrypt_mod = os.environ['WECHAT_ENCRYPT_MOD'], # normal/compatible/safe -> 明文/兼容/安全
    #encoding_aes_key = os.environ['WECHAT_ENCODING_AES_KEY'],
)
wechat = WechatBasic(conf = conf)

@app.route('/', methods=['GET'])
def index():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    if wechat.check_signature(signature, timestamp, nonce):
        return echostr
    else:
        return 'Signature check failed'

@app.route('/hello')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run()
