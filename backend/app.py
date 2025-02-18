import os
from datetime import datetime

from flask import Flask, request, jsonify
from encryption.decryption import Decryption

CURRENT_FOLDER = os.getcwd()
PARENT_FOLDER = os.path.abspath(os.path.join(CURRENT_FOLDER, os.pardir))
DATA_FOLDER = 'data'
KEY = open(PARENT_FOLDER + '\\key.txt', 'r').read()
app = Flask(__name__)

def generate_log_filename():
    return "log_" + datetime.now().strftime("%Y-%m-%d") + ".txt"


def split_data(decrypted_data):
    my_split_data = decrypted_data.split('\n')
    return my_split_data[0], my_split_data[1]

def write_to_file(machine_folder, file_path, log_data, data):
    if not os.path.exists(file_path):
        with open(os.path.join(machine_folder, generate_log_filename()), 'a') as f:
            f.write(log_data + '/n' + data + '/n' * 2)
    else:
        with open(file_path, 'a') as f:
            f.write(log_data + '/n' + data + '/n' * 2)

def create_machine_folder(machine):
    global DATA_FOLDER
    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)
    return machine_folder

@app.route('/api/upload', methods=['POST'])
def upload_data():
    data = request.data
    print(data)
    machine_name = data[:14].decode('utf-8')
    machine_folder = create_machine_folder(machine_name)
    decrypted_data =  Decryption(KEY).decrypt(data[15:])
    print(decrypted_data)
    if not decrypted_data:
        return jsonify({'message': 'No input decrypted_data provided'}), 400

    log_data, data = split_data(decrypted_data)

    file_path = os.path.join(machine_folder, generate_log_filename())
    with open(file_path, 'a') as f:
        f.write(log_data + '\n' + data + '\n' * 2)
    return jsonify({"status": "success", "file": file_path}), 200

if __name__ == '__main__':
    app.run(debug=True)