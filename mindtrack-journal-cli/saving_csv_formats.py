import csv
from entering_the_data import users_logs_file,staff_logs_file

def log_file_csv(filename,file,choice):
    with open(filename,"w",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id","u_id","file_name","time_stamp","message"])
        for keys,values in file.items():
            if choice == 1:
                writer.writerow([keys,values["staff_id"],values["file_name"],values["time_stamp"],values["message"]])
            else:
                writer.writerow([keys,values["user_id"],values["file_name"],values["time_stamp"],values["message"]])

log_file_csv("staff_logs_file.CSV",staff_logs_file,1)
log_file_csv("users_logs_file.CSV",users_logs_file,2)




