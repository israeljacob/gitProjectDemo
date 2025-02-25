import re

def data_pull(path):
    with open(path, encoding="utf-8") as file:
        lines = file.readlines()

    log_data = {}
    current_timestamp = None
    current_message = []

    timestamp_pattern = re.compile(r"^--- \d{2}:\d{2}:\d{2} \d{2}/\d{2}/\d{4} ---$")

    for line in lines:
        line = line.strip()
        if timestamp_pattern.match(line):
            if current_timestamp is not None:
                log_data[current_timestamp] = " ".join(current_message).strip()
            current_timestamp = line.strip('-').strip()
            current_message = []

        elif current_timestamp:
            current_message.append(line)

    if current_timestamp and current_message:
        log_data[current_timestamp] = " ".join(current_message).strip()

    return log_data

