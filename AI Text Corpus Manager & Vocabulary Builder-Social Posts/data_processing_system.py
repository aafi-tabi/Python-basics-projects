from entering_the_data import accessing_the_logs_files, closing_the_log_files, data_saving
import json
from datetime import datetime
import re

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


def collecting_words_only():
    global words
    global words_count
    for key,values in social_posts_catalog.items():
        tokens = re.findall(r'@\w+|#\w+|\w+|[^\w\s]', values["text"])
        for i in tokens:
            count = 0
            if i.isalpha():
                count += 1
                if i not in words:
                    words.append(i)
                    words_count.append(count)
                else:
                    for j in words:
                        if j == i:
                            index = words.index(i)
                            words_count[index] += count


def bigrams_collection():
    global bigrams
    global bigrams_count
    bigram_pairs = []
    for key,values in social_posts_catalog.items():
        count = 0
        tokens = re.findall(r'@\w+|#\w+|\w+|[^\w\s]', values["text"])
        word= []
        for i in tokens:
            appear = 0
            if i.isalpha():
                word.append(i)
        for i in word:    
            appear = 1
            bigram_pairs = []
            count += 1
            if len(word) == count:
                break
            else:
                bigram_pairs.extend([word[count-1],word[count]])
                if bigram_pairs not in bigrams:
                    bigrams.append(bigram_pairs)
                    bigrams_count.append(appear)
                else:
                    for j in bigrams:
                        if j == bigram_pairs:
                            index = bigrams.index(j)
                            bigrams_count[index] += appear


def classification_accuracy_score():
    global accuracy_score
    wrong = 0
    correct = 0
    for key,values in social_posts_catalog.items():
        classification = None
        pos_count = 0
        neg_count = 0
        tokens = re.findall(r'@\w+|#\w+|\w+|[^\w\s]', values["text"])
        for i in tokens:
            for j in pos_words:
                if  i.lower() ==  j:
                    pos_count += 1
            for k in neg_words:
                if i.lower() == k:
                    neg_count += 1
        if pos_count > neg_count:
            classification = "pos"
        elif neg_count > pos_count:
            classification  = "neg"
        else:
            classification = "neutral"
        if values["classification"] == classification:
            correct += 1
        else:
            wrong += 1

    if len(social_posts_catalog) > 0:
        accuracy_score = (correct * 100)/len(social_posts_catalog)
        print(f"Accuracy score: {accuracy_score:.2f}")



            
collecting_words_only()
bigrams_collection()
classification_accuracy_score()

print("\n")
data_saving("words.JSON",words,files_log)

print("\n")
data_saving("words_count.JSON",words_count,files_log)

print("\n")
data_saving("bigrams.JSON",bigrams,files_log)

print("\n")
data_saving("bigrams_count.JSON",bigrams_count,files_log)

print("\n")
closing_the_log_files("files_log.JSON",files_log)

print("\n")
closing_the_log_files("social_posts_catalog_backup.JSON",social_posts_catalog_backup)