from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/greeting')
def hello_world():
    name = request.args.get("name")
    greeting = "Hello ",name
    return jsonify({"Greeting":greeting})


if __name__ == '__main__':
    app.run()