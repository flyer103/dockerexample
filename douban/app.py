#!/usr/bin/env python3

# --------------------------------------------
# 小王子: 1003078
# 禅与摩托车维修艺术: 6811366
# --------------------------------------------

from flask import Flask, jsonify
import requests


app = Flask(__name__)
api = 'https://api.douban.com/v2/book/'


@app.route('/')
@app.route('/<book_id>')
def book(book_id=None):
    ret = {
        'code': -1,
        'msg': '',
        'data': [],
    }

    if book_id is None:
        ret['msg'] = '参数缺失'
        return jsonify(ret)

    url = '{}{}'.format(api, book_id)
    try:
        res = requests.get(url, timeout=3)
        data = res.json()
        if data.get('code'):
            ret['code'] = data['code']
            ret['msg'] = data['msg']
        else:
            ret['code'] = 0
            ret['msg'] = 'success'
            ret['data'] = res.json()
    except Exception as e:
        ret['msg'] = str(e)

    return jsonify(ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
