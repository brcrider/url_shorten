from flask import Flask, jsonify, request
from models import create_table
from routes import shorter_url, retrieve_long_url, update_short_url
app = Flask(__name__)

@app.route('/shorten', methods=['POST'])
def shorten():
    return shorter_url(request.json.get('url'))

@app.route('/retrieve/<short>', methods=['GET'])
def retrieve(short):
    return retrieve_long_url(short)

@app.route('/update/<short>', methods=['PUT'])
def update(short):
    return update_short_url(short, request.json.get('url'))

if __name__ == "__main__":
    create_table()
    app.run(debug=True)