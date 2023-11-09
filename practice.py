from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/square', methods=['POST'])
def square():
    if request.method != 'POST':
        return jsonify({'error': 'method not allowed'}), 405
    try:
        json_data = request.get_json()
        number = json_data['num']
    except Exception as e:
        return jsonify({'error': 'bad request'}), 400
    if isinstance(number, int):
        res = number * number
        return jsonify({'result':res})
    return jsonify({'error': 'bad request'}), 400


if __name__ == '__main__':
    app.run(debug=True, port=8085)
