from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "a bahia eh linda, o docker eh lindo ..."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
