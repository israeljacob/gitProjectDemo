import re
import sys
sys.path.append('../server/utilities')
from config import LIST_OF_OWNERS


def data_pull(path):
    """
    Reads a log file and extracts timestamped messages into a dictionary.

    Parameters:
    path (str): Path to the log file.

    Returns:
    dict: A dictionary where keys are timestamps and values are messages.
    """

    with open(path, encoding="utf-8") as file:
        lines = file.readlines()

    log_data = {}
    current_timestamp = None
    current_message = []

    timestamp_pattern = re.compile(r"^--- \d{2}:\d{2}:\d{2} \d{2}/\d{2}/\d{4} ---$")

    for line in lines:
        line = line.strip()
        if timestamp_pattern.match(line):
            if current_timestamp is not None:
                log_data[current_timestamp] = " ".join(current_message).strip()
            current_timestamp = line.strip('-').strip()
            current_message = []

        elif current_timestamp:
            current_message.append(line)

    if current_timestamp and current_message:
        log_data[current_timestamp] = " ".join(current_message).strip()

    return log_data

def get_list_of_owners(list_of_machine_names):
    return LIST_OF_OWNERS[:len(list_of_machine_names)]

def split_data(decrypted_data):
    """
    Gets the decrypted data that includes the time stamp and the data and splits it into 2.
    :param decrypted_data:
    :return: time stamp, data
    """
    my_split_data = decrypted_data.split('\n')
    return my_split_data[0], my_split_data[1], my_split_data[2], "\n".join(my_split_data[2:])

