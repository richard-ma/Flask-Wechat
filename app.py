from flask import Flask, request
from wechat_sdk import WechatBasic
from config import conf

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    wechat = WechatBasic(conf = conf)
    if wechat.check_signature(signature, timestamp, nonce):
        return echostr
    else:
        return 'Signature check failed'

@app.route('/hello')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run()
