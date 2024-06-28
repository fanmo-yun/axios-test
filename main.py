import flask
import argparse

app = flask.Flask("axios-test")


@app.get('/')
def index():
    return 'axios-test'



parser = argparse.ArgumentParser(description="An axios test app")
parser.add_argument("--ip", type=str, default="127.0.0.1")
parser.add_argument("--port", type=int, default=3333)
args = parser.parse_args()

app.run(host=args.ip, port=args.port, debug=True)
