from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# 数据库连接配置
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "airport_db"  # 请改为你实际的数据库名
}


@app.route('/kenttä/<string:icao>')
def hae_lentokentta(icao):
    try:
        yhteys = mysql.connector.connect(**db_config)
        kursori = yhteys.cursor(dictionary=True)

        # 执行查询
        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchone()

        yhteys.close()

        if tulos:
            # 构造题目要求的响应格式
            vastaus = {
                "ICAO": tulos['ident'],
                "Name": tulos['name'],
                "Municipality": tulos['municipality']
            }
            return jsonify(vastaus)
        else:
            return jsonify({"error": "Airport not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # 题目要求端口为 3000
    app.run(use_reloader=False, port=3000)