from datetime import datetime
from flask import Flask, request

app = Flask(__name__)


CUSTOM_OTA_FILENAME = "device_list.txt"
CUSTOM_OTA_URL = "vending.kit-invest.ru/Download/kpl/to4ver"
CUSTOM_OTA_PORT = 80


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


@app.route("/api/v0/get_ota_url", methods=["GET"])
def get_ota_url():
    serial_number_list = []
    serial_number = 0
    try:
        serial_number = int(request.data.decode())
        with open(CUSTOM_OTA_FILENAME, "r") as f:
            for line in f:
                serial_number_list.append(int(line.strip()))
    except Exception as e:
        return {"Result": "Fail", "Error": str(e)}

    return {"Result": "Ok", "Source": "Custom", "Url": CUSTOM_OTA_URL, "Port": CUSTOM_OTA_PORT} if serial_number in serial_number_list else {"Result": "Ok", "Source": "Defualt"}


@app.route("/api/v0/add_to_custom_ota", methods=["POST"])
def add_to_custom_ota():
    serial_number = 0
    try:
        serial_number = int(request.data.decode())
        with open(CUSTOM_OTA_FILENAME, "a") as f:
            f.write(str(serial_number) + "\n")
    except Exception as e:
        return {"Result": "Fail", "Error": str(e)}

    return {"Result": "Ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
