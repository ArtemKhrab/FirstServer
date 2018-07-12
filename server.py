from flask import Flask
from flask import render_template
from flask import jsonify
from sys import platform
from datetime import datetime
import json
from urllib.request import urlopen


urlInfo = urlopen('http://ipinfo.io/json')
data = json.load(urlInfo)

IP = data['ip']
city = data['city']
country = data['country']


app = Flask(__name__)


@app.route("/getserverinfo", methods=['GET'])
def info():
    return jsonify({'os': platform}, {'time': datetime.now()}, {'location': [city, country]})


@app.route("/getbeautifulinfo", methods=['GET'])
def binfo():
    return render_template('table.html', city=city, country=country, os=platform, time=datetime.now())


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2455)
