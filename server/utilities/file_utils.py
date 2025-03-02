import os
import sys
from datetime import datetime
from os.path import split
from typing import final

sys.path.append('../server/utilities')
from config import LIST_OF_OWNERS
from encryption_utils import encrypt_data

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

def get_data(computer_name, filename):
    final_data = dict()
    with open(os.path.join(DATA_FOLDER, computer_name, filename), 'r') as file:
        data = '\n\n'.split(file.read())
        for organ in data:
            split_data = '\n'.split(organ)
            final_data.update({encrypt_data(split_data[0].strip('-').strip()):
                                [encrypt_data(split_data[1]),
                               encrypt_data(''.join(split_data[2:]))]})
    return final_data