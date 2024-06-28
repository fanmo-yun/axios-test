import argparse
import flask
from person import Person
from flask import jsonify

app = flask.Flask("axios-test")


@app.get('/')
def index():
    return 'axios-test\n'


@app.get('/version')
def version():
    return '1.0.0\n'


@app.get('/get/json/v1')
def jsonv1():
    p = Person()
    return jsonify(p.jsonformat())


@app.get('/get/json/v2')
def jsonv2():
    data = [Person().jsonformat() for _ in range(0, 50)]
    return jsonify(data)


@app.get('/get/json/v3')
def jsonv2():
    data = [Person().jsonformat() for _ in range(0, 100)]
    return jsonify(data)


@app.get('/get/json/v4')
def jsonv2():
    data = [Person().jsonformat() for _ in range(0, 100)]
    return jsonify(data)


parser = argparse.ArgumentParser(description="An axios test app")
parser.add_argument("--ip", type=str, default="127.0.0.1")
parser.add_argument("--port", type=int, default=3333)
args = parser.parse_args()

app.run(host=args.ip, port=args.port, debug=True)
