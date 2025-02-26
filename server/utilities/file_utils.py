import os
import sys
from datetime import datetime
sys.path.append('../server/utilities')
from config import LIST_OF_OWNERS

DATA_FOLDER = 'data'

def generate_log_filename():
    return "log_" + datetime.now().strftime("%Y-%m-%d") + ".txt"

def create_machine_folder(machine_name):
    machine_folder = os.path.join(DATA_FOLDER, machine_name)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)
    return machine_folder

def get_machine_name_list():
    return [folder for folder in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, folder))]

def get_machine_name(owner):
    index = LIST_OF_OWNERS.index(owner)
    return get_machine_name_list()[index]