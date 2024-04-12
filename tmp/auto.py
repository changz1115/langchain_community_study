# 帮我写一个flask应用，监听80端口，maxnumber为必须的参数，应用的功能计算maxnumber和0之间所有双数的合计 
# 假设输入是100，则输出是2500

from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# 如果有必要，可以添加一个带参数的路由
@app.route("/hello/<string:name>")
def hello(name):
    return f"Hello {name}!"

@app.route('/sum', methods=['GET'])
def sum():
    maxnumber = request.args.get('maxnumber')
    if not maxnumber:
        return jsonify({'code': 400, 'msg': '缺少参数maxnumber'})
    # 计算maxnumber和0之间的双数合计
    sum = 0
    for i in range(1, int(maxnumber)):
        if i % 2 == 0:
            sum += i
    return jsonify({'code': 200, 'msg': f"{sum}"})

if __name__ == "__main__":
    app.run(debug=True)
