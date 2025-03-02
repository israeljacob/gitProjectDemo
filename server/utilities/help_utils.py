import re
import sys
sys.path.append('../server/utilities')
from config import LIST_OF_OWNERS


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

