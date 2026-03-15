from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message":"Data Science Model API Running"})

app.run(debug=True)