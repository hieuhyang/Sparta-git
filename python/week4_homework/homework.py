from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('1st_week2.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def write_order():
   name = request.form['name_give']
   count = request.form['count_give']
   add = request.form['add_give']
   number = request.form['number_give']

   print(name)
   print(count)
   print(add)
   print(number)

   db.orderCollection.insert_one({
      'name': name,
      'count': count,
      'add': add,
    'number': number,
   })

   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/order', methods=['GET'])
def read_orders():
   order = list(db.orderCollection.find({}, {'_id': False}))
   print(order)
   return jsonify({
      'result':'success', 'msg': '주문을 잘 받아왔습니다!',
      'data': order
   })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)