from entering_the_data import accessing_the_logs_files, closing_the_log_files, data_saving
import json
from datetime import datetime
import re
import emoji

message = None
social_posts_catalog_backup = dict()
files_log = dict()
pos_words = []
neg_words = []
social_posts_catalog = dict()
usernames = dict()
topic_words = dict()
user_name = False
contain_hashtags = False
contain_mentions = False
contain_emojis= False
contain_punctuations = False
hashtags = []
mentions = []
punctuations = []
emojis = []
numbers_of_words = 0
special_elements = 0
processed_text_input = dict()
tokens = []

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



def processed_text():
    id = 0
    ids = []
    if len(social_posts_catalog) >= 1:
        for key,values in social_posts_catalog.items():
            ids.append(int(key))
        id = max(ids)
    social_posts_catalog.update({int(id)+1: {
            "user_id": processed_text_input["user_id"],
            "username": processed_text_input["username"],
            "text": processed_text_input["text"],
            "topic": processed_text_input["topic"],
            "classification": processed_text_input["classification"],
            "number_of_words": processed_text_input["no_of_words"],
            "special_elements": processed_text_input["special_elements"],
            "contain_hashtags":processed_text_input["contain_hashtags"], 
            "contain_mentions": processed_text_input["contain_mentions"],
            "mention_persons": processed_text_input["mentions"],
            "mentioned_hashtags": processed_text_input["hashtags"],
            "posted_time": processed_text_input["time_stamp"],
            "contain_punctuation":  processed_text_input["contain_punctuations"],
            "punctuation":  processed_text_input["punctuations"],
            "contain_emojis": processed_text_input["contain_emojis"],
            "emojis": processed_text_input["emojis"],
            "no_of_likes":  processed_text_input["no_of_likes"],
            "no_of_comments": processed_text_input["no_of_comments"],
            "no_of_shares": processed_text_input["no_of_shares"],
            "processed": True
    }})
    
    if __name__ == "__main__":
        data_saving("social_posts_catalog.JSON",social_posts_catalog,social_posts_catalog_backup)


def finding_the_topic_of_text():
    word = []
    bigram_pairs = []
    global processed_text_input
    topic_find = False
    topic = None
    for key, values in topic_words.items():
        for i in values:
            for j in tokens:
                if i == j.lower():
                    topic = key
                    topic_find = True
                    break
            if topic_find == True:
                break
        if topic_find == True:
            break
    if topic_find == False:
        for key,values in topic_words.items():
            for j in values:
                count = 0
                word = []
                for i in tokens:
                    if i.isalpha():
                        word.append(i)
                for i in word:
                    count += 1
                    if len(word) == count:
                        break
                    else:
                        bigram_pairs = []
                        bigram_pairs.extend([word[count-1],word[count]])
                        bigram_pairs = " ".join(bigram_pairs)
                        if j == bigram_pairs.lower():
                            topic = key
                            topic_find = True
                            break
                if topic_find == True:
                    break
            if topic_find == True:
                break
                                  
    processed_text_input.update({"topic": topic})
    processed_text()


def text_classification(tokens):
    global processed_text_input
    pos_count = 0
    neg_count = 0
    for i in tokens:
        for j in pos_words:
            if  i.lower() ==  j:
               pos_count += 1
        for k in neg_words:
            if i.lower() == k:
                neg_count += 1
    if pos_count > neg_count:
        processed_text_input.update({"classification": "pos"})
    elif neg_count > pos_count:
        processed_text_input.update({"classification": "neg"})
    else:
        processed_text_input.update({"classification": "neutral"})
    finding_the_topic_of_text()


def processing_the_input(tokens,time_stamp):
    global contain_hashtags
    global contain_mentions 
    global contain_emojis
    global contain_punctuations 
    global hashtags
    global mentions
    global punctuations
    global emojis
    global numbers_of_words
    global special_elements  
    global processed_text_input

    for i in tokens:
        if i.isalpha():
            numbers_of_words += 1
        elif i[0] == "#":
            special_elements += 1
            contain_hashtags = True
            hashtags.append(i[1:])
        elif i[0] == "@":
            special_elements += 1
            contain_mentions = True
            mentions.append(i[1:])
        elif i in emoji.EMOJI_DATA:
            special_elements += 1
            contain_emojis= True
            emojis.append(i)
        else:
            special_elements += 1
            contain_punctuations = True
            punctuations.append(i)

    processed_text_input.update({"time_stamp":time_stamp,
                                "no_of_words": numbers_of_words,
                                 "special_elements": special_elements,
                                 "contain_hashtags": contain_hashtags,
                                 "hashtags": hashtags,
                                 "contain_mentions": contain_mentions,
                                 "mentions": mentions,
                                 "contain_emojis": contain_emojis,
                                 "emojis": emojis,
                                 "contain_punctuations": contain_punctuations,
                                 "punctuations": punctuations})    
    contain_hashtags = False
    contain_mentions = False
    contain_emojis= False
    contain_punctuations = False
    hashtags = []
    mentions = []
    punctuations = []
    emojis = []
    numbers_of_words = 0
    number_of_chracters = 0
    text_classification(tokens)

def comments_input():
    global processed_text_input
    comments_input_check = False
    while comments_input_check != True:
        try:
            comments = int(input("Enter a number of comments: "))
            if isinstance(comments,int):
                comments_input_check = True
                break
        except ValueError:
            print("Incorrect value")
            print("Try again")

    if comments_input_check == True:
        processed_text_input.update({"no_of_comments": comments})

def shares_input():
    global processed_text_input
    shares_input_check = False
    while shares_input_check != True:
        try:
            shares = int(input("Enter a number of shares: "))
            if isinstance(shares,int):
                shares_input_check = True
                break
        except ValueError:
            print("Incorrect value")
            print("Try again")

    if shares_input_check == True:
        processed_text_input.update({"no_of_shares": shares})
    if shares_input_check == True:
            comments_input()


def likes_input():
    global processed_text_input
    likes_input_check = False
    while likes_input_check != True:
        try:
            likes = int(input("Enter a number of likes: "))
            if isinstance(likes,int):
                likes_input_check = True
                break
        except ValueError:
            print("Incorrect value")
            print("Try again")

    if likes_input_check == True:
        processed_text_input.update({"no_of_likes": likes})
    if likes_input_check == True:
        shares_input()

    
def entering_the_text_input():
    global processed_text_input
    global tokens
    input_choice_check = False
    quit_loop = False
    while quit_loop != True:
        input_choice_check = False
        print("\n")
        print("1 - Post text")
        print("2 - Content text")
        try:
            input_choice = int(input("Enter your choice(0 to exit): "))
            if input_choice == 1:
                raw_text = input("Enter a post text: ")
                time_stamp = datetime.now().strftime('%Y-%m-%D %H:%M:%S')
                input_choice_check = True
            elif input_choice == 2:
                raw_text = input("Enter a content text: ")
                time_stamp = datetime.now().strftime('%Y-%m-%D %H:%M:%S')
                input_choice_check = True
            elif input_choice == 0:
                quit_loop = True
                break
            else:
                print("Wrong choice")
                print("Try again")
                print("\n")

            if quit_loop == False:
                if input_choice_check == True:
                    likes_input()
                if input_choice_check == True:
                    processed_text_input.update({"text": raw_text})
                    tokens = re.findall(r'@\w+|#\w+|\w+|[^\w\s]', raw_text)
                    processing_the_input(tokens,time_stamp)
        except ValueError:
            print("Invalid choice")


def entering_username():
    global processed_text_input
    username_exist = False
    while username_exist != True:
        username_exist = False
        username = input("Enter your username(quit to exit): ")
        if username != "quit" and username != "Quit" and username != "QUIT":
            for key,values in usernames.items():
                if values == username:
                    processed_text_input.update({"user_id": key})
                    processed_text_input.update({"username": values})
                    username_exist = True
                    break
            if username_exist == True:
                print("\n")
                print("username has been matched")
                print("\n")
                entering_the_text_input()
                break
            if username_exist == False:
                print("\n")
                print("username does not exist")
                print("Try Again")
                print("\n")
        else:
            username_exist = False
            break


print("\n")
entering_username()

print("\n")
closing_the_log_files("files_log.JSON",files_log)

print("\n")
closing_the_log_files("social_posts_catalog_backup.JSON",social_posts_catalog_backup)
