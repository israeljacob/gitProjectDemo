import os

CURRENT_FOLDER = os.getcwd()
PARENT_FOLDER = os.path.abspath(os.path.join(CURRENT_FOLDER, os.pardir))
GRANDFATHER_FOLDER = os.path.abspath(os.path.join(PARENT_FOLDER, os.pardir))

DATA_FOLDER = 'data'
KEY_FILE_PATH = os.path.join(PARENT_FOLDER, 'utilities', 'key.txt')

with open(KEY_FILE_PATH, 'r') as key_file:
    KEY = key_file.read()

OWNERS_FILE_PATH = 'Full_Names.txt'
with open(OWNERS_FILE_PATH, 'r') as file:
    LIST_OF_OWNERS = file.read().splitlines()
