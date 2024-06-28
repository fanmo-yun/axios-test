import argparse
import flask
from person import Person
from flask import jsonify, request

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
def jsonv3():
    data = [Person().jsonformat() for _ in range(0, 100)]
    return jsonify(data)


@app.get('/get/json/v4')
def jsonv4():
    num = request.args.get("num")
    if num is None or num == "":
        return jsonify({
            "msg": "Miss num",
        }), 400

    if num.isnumeric() and int(num) > 0:
        data = [Person().jsonformat() for _ in range(0, int(num))]
        return jsonify(data)
    else:
        return jsonify({
            "msg": "num is 不合法的",
        }), 400


@app.post("/post/v1")
def postv1():
    form_data = request.form.to_dict()
    if not form_data:
        return jsonify({'error': 'No form data found'}), 400
    return jsonify(form_data), 200


parser = argparse.ArgumentParser(description="An axios test app")
parser.add_argument("--ip", type=str, default="127.0.0.1")
parser.add_argument("--port", type=int, default=3333)
args = parser.parse_args()

app.run(host=args.ip, port=args.port, debug=True)
