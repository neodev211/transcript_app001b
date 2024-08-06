# /api/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Flask Vercel Example - Hello World"), 200