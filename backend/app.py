import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import sys
from pathlib import Path
from data_pull_in_dict import data_pull

sys.path.append('../encryptionDecryption')
from decryption import Decryption
from encryption import Encryption

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', filename='log.txt', filemode='w')

CURRENT_FOLDER = os.getcwd()
PARENT_FOLDER = os.path.abspath(os.path.join(CURRENT_FOLDER, os.pardir))

DATA_FOLDER = 'data'
KEY = open(PARENT_FOLDER + '/key.txt', 'r').read()
app = Flask(__name__)
CORS(app)
OWNERS_FILE = open('Full_Names.txt', 'r')
LIST_OF_OWNERS = OWNERS_FILE.read().splitlines()
OWNERS_FILE.close()

def generate_log_filename():
    return "log_" + datetime.now().strftime("%Y-%m-%d") + ".txt"


def split_data(decrypted_data):
    """
    Gets the decrypted data that includes the time stamp and the data and splits it into 2.
    :param decrypted_data:
    :return: time stamp, data
    """
    my_split_data = decrypted_data.split('\n')
    return my_split_data[0], "\n".join(my_split_data[1:])

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

def get_list_of_owners(list_of_machine_names):
    global LIST_OF_OWNERS
    return LIST_OF_OWNERS[:len(list_of_machine_names)]

def encrypt_data(names_of_owners):
    encrypt = Encryption(KEY)
    for i, name in enumerate(names_of_owners):
        names_of_owners[i] = encrypt.encryption(name)
    return names_of_owners


def get_machine_name_list():
    machine_name_list = []
    for folder in os.listdir(DATA_FOLDER):
        if os.path.isdir(os.path.join(DATA_FOLDER, folder)):
            machine_name_list.append(folder)
    return machine_name_list

def get_machine_name(owner):
    global LIST_OF_OWNERS
    index = LIST_OF_OWNERS.index(owner)
    return get_machine_name_list()[index]

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
        f.write("--- "+log_data + ' ---\n' + data + '\n' * 2 )
    logging.info('Data saved to ' + file_path)
    return jsonify({"status": "success", "file": file_path}), 200


@app.route('/api/list_machines_target_get', methods=['GET'])
def list_machines():
    if not os.path.exists(DATA_FOLDER):
        return jsonify([]), 400
    machines = get_machine_name_list()
    if not machines:
        return jsonify([]), 400
    names_of_owners = get_list_of_owners(machines)
    encrypted_owners = encrypt_data(names_of_owners)
    return jsonify(encrypted_owners),200

@app.route('/api/computer_data/<owner_name>', methods=['GET'])
def computer_data(owner_name):
    try:
        computer_name = get_machine_name(owner_name)
    except:
        return jsonify({'status': False, 'message': 'Machine not found'}), 400
    all_data = dict()
    all_data_final = dict()
    global CURRENT_FOLDER
    folder_path = Path(CURRENT_FOLDER+"/data/" + computer_name)
    for file in folder_path.iterdir():
        file_str = str(file)
        if "log" in file_str:
            idx_file_name = file_str.find("log_")
            all_data[file_str[idx_file_name:]] = data_pull(file_str)
    all_data_final[owner_name] = all_data
    return jsonify(all_data_final), 200

def search_computer(computer_name,folder_path):
    flag = True
    for folder in folder_path.iterdir():
        str_folder = str(folder)
        idx = str_folder.find("/data/") + 6
        if computer_name == str_folder[idx:]:
            flag = False
            break
    return flag

if __name__ == '__main__':
    app.run(debug=True)







