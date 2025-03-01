import json

import requests
from logger.writer.IWriter import IWriter


class NetWorkWriter(IWriter):
    def __init__(self):
        with open('../config.json', 'r') as config_file:
            self.url = json.load(config_file)['post_link']

    def send_data(self, data: str) -> None:
        response = requests.post(self.url, data=data)
