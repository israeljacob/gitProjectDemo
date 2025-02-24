import re

def data_pull(path):
    # פתיחת הקובץ לקריאה
    with open(path, encoding="utf-8") as file:
        lines = file.readlines()

    log_data = {}
    current_timestamp = None
    current_message = []

    # תבנית לזיהוי חותמת זמן (דפוס קבוע של שעה ותאריך)
    timestamp_pattern = re.compile(r"^--- \d{2}:\d{2}:\d{2} \d{2}/\d{2}/\d{4} ---$")

    for line in lines:
        line = line.strip()  # הסרת רווחים מיותרים
        if timestamp_pattern.match(line):
            # אם יש חותמת זמן חדשה, שמור את ההודעה הקודמת
            if current_timestamp is not None:
                log_data[current_timestamp] = " ".join(current_message).strip()
            # אתחול חותמת הזמן והודעה חדשה
            current_timestamp = line
            current_message = []

        # צבירת ההודעה תחת חותמת הזמן האחרונה
        elif current_timestamp:
            current_message.append(line)

    # הוספת ההודעה האחרונה
    if current_timestamp and current_message:
        log_data[current_timestamp] = " ".join(current_message).strip()

    # הצגת התוצאה
    return log_data

