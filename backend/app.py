import os
from datetime import datetime
from flask import Flask, request, jsonify
import logging
from encryption.decryption import Decryption

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', filename='app.log', filemode='w')

CURRENT_FOLDER = os.getcwd()
PARENT_FOLDER = os.path.abspath(os.path.join(CURRENT_FOLDER, os.pardir))

DATA_FOLDER = 'data'
KEY = open(PARENT_FOLDER + '\\key.txt', 'r').read()
app = Flask(__name__)

def generate_log_filename():
    return "log_" + datetime.now().strftime("%Y-%m-%d") + ".txt"


def split_data(decrypted_data):
    """
    Gets the decrypted data that includes the time stamp and the data and splits it into 2.
    :param decrypted_data:
    :return: time stamp, data
    """
    my_split_data = decrypted_data.split('\n')
    return my_split_data[0], my_split_data[1]

def create_machine_folder(machine_name):
    """
    Creates a folder if not exists.
    :param machine_name:
    :return: The folder path.
    """
    global DATA_FOLDER
    machine_folder = os.path.join(DATA_FOLDER, machine_name)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)
    return machine_folder

@app.route('/api/upload', methods=['POST'])
def upload_data():
    """
    Gets the posted data and manages storing it in the database.
    :return The status of the HTTP request.:
    """
    data = request.data
    try:
        machine_name = data[:14].decode('utf-8')
        machine_folder = create_machine_folder(machine_name)
        decrypted_data =  Decryption(KEY).decrypt(data[15:])
    except Exception as e:
        logging.error(e)
        return jsonify({'status': False, 'message': str(e)}), 400
    if not decrypted_data:
        logging.info('No data received to the server.')
        return jsonify({'message': 'No input decrypted_data provided'}), 400

    log_data, data = split_data(decrypted_data)

    file_path = os.path.join(machine_folder, generate_log_filename())
    with open(file_path, 'a') as f:
        f.write(log_data + '\n' + data + '\n' * 2)
    logging.info('Data saved to ' + file_path)
    return jsonify({"status": "success", "file": file_path}), 200

if __name__ == '__main__':
    app.run(debug=True)