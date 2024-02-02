from flask import Flask

app = Flask(__name__)


@app.route("/api/v0/ping", methods=["POST"])
def ping():
    return {"Result": "Ok"}


@app.route("/api/v0/archive", methods=["POST"])
def archive():
    return {"Result": "Ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
