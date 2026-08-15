from entering_the_data import accessing_the_logs_files, closing_the_log_files
import json
from datetime import datetime
import csv

message = None
social_posts_catalog_backup = dict()
files_log = dict()
pos_words = []
neg_words = []
social_posts_catalog = dict()
usernames = []
topic_words = dict()
words = []
words_count = []
bigrams = []
bigrams_count = []
accuracy_score = 0

def accessing_the_data(file_name,log_file):
    global message

    try:
        with open(file_name,"r",encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        message = f"{file_name} not found"
        print(f"{file_name} not found")
    except json.JSONDecodeError:
        message = "Data corrupted"
        print("Data corrupted")
    else:
        message = f"{file_name} loaded successfully"
        print(f"{file_name} loaded successfully")
    finally:
        time_stamp = datetime.now().strftime('%D %H:%M:%S')
        id = int(len(log_file) + 1)
        log_file.update({id:
                            {"file_name": file_name,
                            "time_stamp": time_stamp,
                            "message": message}})
    return data



print("\n")
social_posts_catalog_backup = accessing_the_logs_files("social_posts_catalog_backup.JSON")

print("\n")
files_log = accessing_the_logs_files("files_log.JSON")

print("\n")
social_posts_catalog = accessing_the_data("social_posts_catalog.JSON",social_posts_catalog_backup)

print("\n")
pos_words = accessing_the_data("positive_words.JSON",files_log)

print("\n")
neg_words = accessing_the_data("negative_words.JSON",files_log)

print("\n")
usernames = accessing_the_data("usernames.JSON",files_log)

print("\n")
topic_words = accessing_the_data("topic_words.JSON",files_log)


def tabular_format():
    with open("social_posts_catalog_tabular_form.csv","w",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["serial_no","user_id","username","text","topic","classification","number_of_words","special_elements","contain_hashtags","contain_mentions","mention_persons","mentioned_hashtags","posted_time","contain_punctuation","punctuation","contain_emojis","emojis","no_of_likes","no_of_comments","no_of_shares","processed"])
        for key,values in social_posts_catalog.items():
            mention = ",".join(values["mention_persons"])
            hastags = ",".join(values["mentioned_hashtags"])
            punctuation = ",".join(values["punctuation"])
            emojis = ",".join(values["emojis"])
            writer.writerow([key,values["user_id"],values["username"],values["text"],values["topic"],values["classification"],values["number_of_words"],values["special_elements"],values["contain_hashtags"],values["contain_mentions"],values["mention_persons"],values["mentioned_hashtags"],values["posted_time"],values["contain_punctuation"],values["punctuation"],values["contain_emojis"],values["emojis"],values["no_of_likes"],values["no_of_comments"],values["no_of_shares"],values["processed"]])


def human_readable_form():
    with open("social_posts_catalog_human_readable.csv","w",encoding="utf-8") as file:
        writer = csv.writer(file)
        for key,values in social_posts_catalog.items():
            writer.writerow([f"{values["posted_time"]} : posted by: {values["username"]} | Likes: {values["no_of_likes"]} | Comments: {values["no_of_comments"]} | Shares: {values["no_of_shares"]} | Hastags: {" , ".join(values["mentioned_hashtags"])} | Mentions: {" , ".join(values["mention_persons"])}"])


tabular_format()

human_readable_form()

print("\n")
closing_the_log_files("files_log.JSON",files_log)

print("\n")
closing_the_log_files("social_posts_catalog_backup.JSON",social_posts_catalog_backup)