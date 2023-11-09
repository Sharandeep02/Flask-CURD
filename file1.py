from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/square", methods=["POST"])
def square():
    if request.method != "POST":
        return jsonify({"error": "Method Not Allowed"}), 405

    try:
        json_data = request.get_json()
        number = json_data["number"]
    except Exception as e:
        return jsonify({"error": "Bad Request"}), 400

    if isinstance(number, int):
        result = number ** 2

        return jsonify({"result": result})

    return jsonify({"error": "bad request"})


if __name__ == "__main__":
    app.run(debug=True, port=8081)
