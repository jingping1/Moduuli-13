from flask import Flask, jsonify

app = Flask(__name__)


# 判断素数的逻辑函数
def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 定义路由，<luku> 表示接收一个路径参数
@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    tulos = on_alkuluku(luku)

    # 构造题目要求的响应格式
    vastaus = {
        "Number": luku,
        "isPrime": tulos
    }

    # 使用 jsonify 将字典转换为 JSON 响应
    return jsonify(vastaus)


if __name__ == '__main__':
    # 题目要求端口为 3000
    app.run(use_reloader=False, port=3000)