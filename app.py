from datetime import datetime
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
