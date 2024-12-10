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
        for item in request.data.decode().split(","):
            if "len=" in item:
                size_to_response = int(item.split("=")[-1])
                break
    except Exception:
        pass

    size_of_number = len(str(size_to_response))

    return "X" * (size_to_response - size_of_number) + str(size_to_response) if size_to_response else "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
