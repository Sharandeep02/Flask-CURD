from flask import Flask, request
import random
from flask_sse import sse

app = Flask(__name__)


@app.route("/stream")
def stream():
    print('in stream')
    return sse.stream()


def generate_data():
    while True:
        return f"data:{random.randint(1, 100)}"
    if data % 5 == 0:
        data = data.replace("5", "0")


if __name__ == '__main__':
    app.run(debug=True, port=8081)