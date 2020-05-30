from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('mall_es.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def order():
    name_receive = request.form['customer_name']
    count_receive = request.form['order_count']
    addr_receive = request.form['customer_addr']
    phone_receive = request.form['customer_phone']


    order = {
       'customer_name': name_receive,
       'order_count': count_receive,
       'customer_addr': addr_receive,
       'customer_phone': phone_receive
    }

    db.esmall.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/orderlist', methods=['GET'])
def read_orderlist():
		# 1. get all orders
    orderlist = list(db.esmall.find({},{'_id':0}))

    return jsonify({'result': 'success', 'orderlist': orderlist})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)