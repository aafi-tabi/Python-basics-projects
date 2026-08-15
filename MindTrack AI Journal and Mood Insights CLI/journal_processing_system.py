from entering_the_data import accessing_the_log_files,accessing_the_user_data,closing_the_log_files
from user_login import user_confirmation,old_username,new_username,InvalidData,check_data,InvalidInput,check_user_input,getting_a_new_user_name,getting_a_new_user_DOB,new_user_password,users_logs_file,staff_logs_file,User,user
import json
from datetime import datetime
import sys

no_of_todays_journal_entries = 0
todays_mood_score = 0
todays_journal_entry = None
time_stamp = None
date = None
mood_text = None
today_mood = None
journal_id = None

user_choice = user_confirmation()

if(user_choice == "y"):
    new_username(False)
    id,username,password,name,age,dob = User.get_data()
    print(f"{f"""Welcome, {name}
    How are you feeling today?""":^10}")
else:
    old_username()
    id,username,password,name,age,dob = User.get_data()
    print(f"{f"""Welcome back, {name}
    How are you feeling today?""":^10}")

journal_entries = accessing_the_user_data("journal_entries.JSON",id,False)
users = accessing_the_user_data("users.JSON",id,False)
user_profiles = accessing_the_user_data("user_profiles.JSON",id,False)
user_defined_stop_words = accessing_the_user_data("user_defined_stop_words.JSON",id,False)
mood_scores = accessing_the_user_data("mood_scores.JSON",id,False)
mood_analysis = accessing_the_user_data("mood_analysis.JSON",id,False)
print("\n")


def stop_words_func(*args):
    for i in args:
        user_defined_stop_words.append(i)

def mood_analysis_():
    user_mood_history = dict()
    mood_score_sum = 0
    count = 0
    mood_score = []


    for keys,values in mood_analysis.items():
        mood_id = keys.split("_")
        if id == mood_id[0]:
            user_mood_history.update({keys: values})
            count += 1
            mood_score_sum += values["mood_score"]
            mood_score.append(values["mood_score"])

    avg_mood_score = mood_score_sum/count
    max_mood_socre = max(mood_score)
    min_mood_score = min(mood_score)

    return count,avg_mood_score,max_mood_socre,min_mood_score


def mood_score_calculation():
    global today_mood
    global todays_mood_score
    is_mood = False
    user_def_stop_words = list()
    count = 0
    mood_text_list = mood_text.replace(";","").replace(",","").replace(".","").strip().split()
    for word in mood_text_list:
        for mood,scores in  mood_scores.items():
            if word == mood:
                is_mood = True
                todays_mood_score += scores
                count += 1
                break
        if is_mood == False:
            user_def_stop_words.append(word)
        stop_words_func(*user_def_stop_words)

    if(count>0):
        todays_mood_score = todays_mood_score/count

        for mood,scores in mood_scores.items():
            if todays_mood_score == scores:
                today_mood = mood

    mood_analysis.update({journal_id:{"mood_score": todays_mood_score,
                                      "mood": today_mood,
                                      "mood_line": mood_text}})
    
def new_journal_entry():
    global todays_journal_entry
    global time_stamp
    global date
    global mood_text
    global journal_id
    correct_user_choice = False
    print("NEW JOURNAL ENTRY")
    todays_journal_entry_title = input("Enter a title of today's journal entry: ").strip()
    time_stamp = datetime.now().strftime("%H:%M:%S")
    date  = datetime.now().strftime("%Y-%m-%D")
    print(f"Date: {date}")
    print(f"Time: {time_stamp}")
    todays_journal_entry = input("what's on your mind?\n").strip()
    mood_text = input("how are you feeling today? ").strip()
    journal_id = str(id) + "_" + str(len(journal_entries[id]) + 1)
    mood_score_calculation()
    print(f"Today's mood score: {todays_mood_score}")

    while(correct_user_choice != True):
        user_choice = input("""s - Save
c - Cancel \n""").lower()
        try: 
            check_user_input(user_choice)
            correct_user_choice = True
        except InvalidInput as error:
            print(error)

        if(correct_user_choice == True):
            if(user_choice == "s"):
                journal_entries[id].update({journal_id:{"date": date,
                                                        "time_stamp": time_stamp,
                                                        "title": todays_journal_entry_title,
                                                        "journal": todays_journal_entry,
                                                        "mood_score": todays_mood_score}})
                print("Today's journal entry saved successfully")
            elif(user_choice  == "c"):
                print("Today's journal entry not saved")
            else:
                correct_user_choice = False
                print("Invalid choice")
                print("Try again")
                print("\n")
    main_menu()


def sort_journal_entries(factor):
    sorted_by_factor = dict(sorted(journal_entries[id].items(),  key=lambda entry:entry[1][factor]))
    for keys,values in sorted_by_factor.items():
        print("\n")
        print(keys, values)
    
    main_menu()


def search_by(factor):
    correct_user_search_choice = False
    while(correct_user_search_choice != True):
        if factor == "title":
            user_search_choice = int(input("""1 - sort by MoodScore
            2 - sort by Date"""))
        else:
            user_search_choice = int(input("""1 - sort by MoodScore
            2 - sort by Title"""))
        try:
            check_data(user_search_choice,int)
            correct_user_search_choice = True
        except InvalidData as error:
            print(error)

        if(correct_user_search_choice == True):
            if user_search_choice == 1:
                sort_journal_entries("mood_score")
            elif user_search_choice == 2 and factor == "title":
                sort_journal_entries("date")
            elif user_search_choice == 2  and factor == "date":
                sort_journal_entries("title")
            else:
                correct_user_search_choice = False
                print("Invalid choice")
                print("Try again")
                print("\n")

    main_menu()


def view_my_journals():
    correct_user_view_choice = False
    while(correct_user_view_choice != True):
        user_view_choice = int(input("""1 - search by Title
        2 - search by Date"""))
        try:
            check_data(user_view_choice,int)
            correct_user_view_choice = True
        except InvalidData as error:
            print(error)

        if(correct_user_view_choice == True):
            if user_view_choice == 1:
                search_by("title")
            elif user_view_choice == 2:
                search_by("date")
            else:
                correct_user_view_choice = False
                print("Invalid choice")
                print("Try again")
                print("\n")
    main_menu()


def mood_history():
    user_mood_history = dict()
    for keys,values in mood_analysis.items():
        mood_id = keys.split("_")
        if id == mood_id[0]:
            user_mood_history.update({keys: values})

    for key,values in user_mood_history.items():
        print(key, values)

    main_menu()

def member_since():
    for key,values in user_profiles.items():
        if id  ==  key:
            return values["signup_datetime"]
    main_menu()


def update_user_profile():
    global name
    global username
    global password
    global dob
    global user_profiles
    global users
    update_user_profile_dic = dict()
    correct_user_choice_update_choice = False
    while(correct_user_choice_update_choice != True):
        user_choice_update_choice = int(input("""what do you want to update
        1 - Update name
        2 - Update username
        3 - Update Password
        4 - Update DOB \n"""))

        try:
            check_data(user_choice_update_choice,int)
            correct_user_choice_update_choice = True
        except InvalidData  as error:
            print(error)

        if correct_user_choice_update_choice == True:
            if(user_choice_update_choice == 1):
                name =  getting_a_new_user_name(True)
                user_profiles = accessing_the_user_data("user_profiles.JSON",id,False)
            elif(user_choice_update_choice == 2):
                username = new_username(True)
                users = accessing_the_user_data("users.JSON",id,False)
            elif(user_choice_update_choice == 3):
                password = new_user_password(username,True,True)
                users = accessing_the_user_data("users.JSON",id,False)
            elif(user_choice_update_choice == 4):
                dob = getting_a_new_user_DOB(name,True)
                user_profiles = accessing_the_user_data("user_profiles.JSON",id,False)
            else:
                correct_user_choice_update_choice = False
                print("Invalid choice")
                print("Try again")
                print("\n")   

def profile():
    total_enteries,avg_mood_score,max_mood_socre,min_mood_score = mood_analysis_()
    member_signup = member_since()
    print("PROFILE")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Username: {username}")
    print(f"Date of birth: {dob}")
    print(f"Member since: {member_signup}")
    print(f"Total enteries: {total_enteries}")
    print("JOURNAL OVERVIEW")
    print(f"Average mood: {avg_mood_score}")
    print(f"Highest mood: {max_mood_socre}")
    print(f"Lowest mood: {min_mood_score}")

    correct_update_profile_choice = False
    while(correct_update_profile_choice != True):
        update_profile_choice = input("Do you want to update profile? (y/n) ").strip().lower()
        try:
            check_user_input(update_profile_choice)
            correct_update_profile_choice = True
        except InvalidInput as error:
            print(error)

        if(correct_update_profile_choice == True):
            if(update_profile_choice == "y"):
                update_user_profile()
            else:
                print("exit")
        else:
            correct_update_profile_choice = False
            print("Invalid choice")
            print("Try again")
            print("\n")
    main_menu()


def logout():
    correct_logout_choice = False
    while(correct_logout_choice != True):
        logout_choice = int(input("""Are you sure you want to log out?
        1 - Yes
        2 - No \n"""))
        try: 
            check_data(logout_choice,int) 
            correct_logout_choice = True
        except InvalidData as error:
            print(error)

        if(correct_logout_choice == True):
            if(logout_choice == 1):
                closing_the_log_files(staff_logs_file,"staff_logs_file.JSON")
                closing_the_log_files(users_logs_file,"users_logs_file.JSON")
                closing_the_log_files(users,"users.JSON")
                closing_the_log_files(user_profiles,"user_profiles.JSON")
                closing_the_log_files(journal_entries,"journal_entries.JSON")
                closing_the_log_files(user_defined_stop_words,"user_defined_stop_words.JSON")
                closing_the_log_files(mood_scores,"mood_scores.JSON")
                closing_the_log_files(mood_analysis,"mood_analysis.JSON")
                print("exiting")
                sys.exit(0) 
            elif(logout_choice == 2):
                main_menu()
            else:
                correct_logout_choice = False
                print("Invalid choice")
                print("Try again")
                print("\n")


def main_menu():
    print("\n")
    print(f"{"What would you like to do?":^10}")
    print("1. ✍️ Write a new journal")
    print("2. 📖 View my journals")
    print("3. 📊 Mood history")
    print("4. 👤 Profile")
    print("5. 🚪 Logout")

    user_choice = int(input("Enter your choice: "))
    correct_user_choice = False
    while(correct_user_choice != True):
        try:
            check_data(user_choice,int)
            correct_user_choice = True
        except InvalidData as error:
            print(error)

        if correct_user_choice == True:
            if(user_choice == 1):
                new_journal_entry()
            elif(user_choice == 2):
                view_my_journals()
            elif(user_choice == 3):
                mood_history()
            elif(user_choice == 4):
                profile()
            elif(user_choice == 5):
                logout()
            else:
                correct_user_choice = False
                print("Invalid choice")
                print("Try again")
                print("\n")

main_menu()

