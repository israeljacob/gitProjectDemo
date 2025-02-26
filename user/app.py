import json

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/key')
def get_key():
    file = open('../utilities/key.txt', 'r')
    key = file.read().strip()
    file.close()
    return jsonify({'key': key}), 200

@app.route('/usernames_and_passwords')
def get_usernames_and_passwords():
    with open('../server/usernames_and_passwords.json', 'r') as file:
        data = json.load(file)
    return jsonify(data), 200



if __name__ == '__main__':
    app.run(port=8000, debug=True)