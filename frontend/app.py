from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def get_key():
    file = open('../key.txt', 'r')
    key = file.read().strip()
    file.close()
    return jsonify({'key': key}), 200

if __name__ == '__main__':
    app.run(port=8000)