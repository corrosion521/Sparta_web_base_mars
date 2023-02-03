# setting : flask,dnspython,dbmongo //서버프레임워크(flask)랑 db(mongodb)사용 위해. dnspython은 도메인 받아 송수신시 사용(서버연동)
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 이하 3줄 db사용 위해
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.n0vryb2.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give'] #name_give로 온 것을 받아서
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name':name_receive,
        'address':address_receive,
        'size' :size_receive
    }
    db.mars.insert_one(doc) # db에 넣음.

    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    #db에서 다 가져오자
    order_list = list(db.mars.find({}, {'_id' : False}))#조건 없고, id 없이

    return jsonify({'orders':order_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)