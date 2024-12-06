from datetime import datetime
from flask import Flask, request

app = Flask(__name__)


@app.route("/api/v0/ping", methods=["POST"])
def ping():
    return {"Result": "Ok"}


@app.route("/api/v0/archive", methods=["POST"])
def archive():
    return {"Result": "Ok"}


@app.route("/api/v0/state", methods=["POST"])
def state():
    return {"Result": "Ok"}


@app.route("/api/v0/datetime", methods=["GET"])
def datetime_endpoint():
    now = datetime.now()
    return {"Result": "Ok", "Datetime": datetime.strftime(now, '%d.%m.%y %H:%M:%S')}


@app.route("/api/v0/echo", methods=["POST"])
def echo():
    return request.data.decode()


@app.route("/api/v0/benchmark", methods=["POST"])
def benchmark():
    size_to_response = 0
    try:
        size_to_response = int(request.data.decode())
    except ValueError:
        pass

    return "X" * size_to_response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
