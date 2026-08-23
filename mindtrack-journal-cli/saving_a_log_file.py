import json

log_file = dict()

try:
    with open("staff_logs_file.JSON", "w") as file:
        json.dump(log_file, file, indent=4, ensure_ascii=False)
except OSError:
    message = "\"staff_logs_file\" could not be saved"
    print("\"staff_logs_file\" could not be saved")
except ValueError:
    message = """\"staff_logs_file\" corrupted
JSON format is required"""
    print("""\"staff_logs_file\" corrupted
JSON format is required""")
else:
    message = "\"staff_logs_file\" saved successfully"
    print("\"staff_logs_file\" saved successfully")

try:
    with open("users_logs_file.JSON", "w") as file:
        json.dump(log_file, file, indent=4, ensure_ascii=False)
except OSError:
    message = "\"users_logs_file\" could not be saved"
    print("\"users_logs_file\" could not be saved")
except ValueError:
    message = """\"users_logs_file\" corrupted
JSON format is required"""
    print("""\"users_logs_file\" corrupted
JSON format is required""")
else:
    message = "\"users_logs_file\" saved successfully"
    print("\"users_logs_file\" saved successfully")
