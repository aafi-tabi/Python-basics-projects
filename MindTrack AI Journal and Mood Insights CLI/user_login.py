import json
from datetime import datetime
from entering_the_data import accessing_the_log_files,accessing_the_user_data,closing_the_log_files,users_logs_file,staff_logs_file

time_stamp = None
users = None
journal_entries = None
user_profiles = None


class InvalidDateOfBirth(Exception):
    pass

class InvalidData(Exception):
    pass

class InvalidUsername(Exception):
    pass

class InvalidInput(Exception):
    pass

def check_dob_format(dob):
    if(len(dob) != 10):
        raise InvalidDateOfBirth(f"""Invalid format
                                    Try again""")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
         raise InvalidDateOfBirth(f"""Invalid data of birth entered
                                            Try again""")
    
def check_data(data,datatype):
    if not isinstance(data,datatype):
        raise InvalidData(f"""Invalid data entered
                            Try again""")

def check_case_of_username(username):
    if username != username.lower():
        raise InvalidUsername("""Username should be in lowercase
                            Try again""")
    
def check_user_input(input):
    if not input.isalpha():
        raise InvalidInput("""Invalid input
Try again""")

class User:
    id = 0
    name = None
    _age = None
    username = None
    password = None
    __password = None
    dob = None

    def __init__(self,id=0,name="",age=0,username="",dob=""):
        self.id = id
        self.name = name
        self._age = age
        self.username = username
        self.__password  = users[self.id][self.username]
        self.dob = dob
        print("loading a data")

    def check_password(self,password):
        self.__password = users[self.id][self.username]
        if password == self.__password:
            print("Password matched successfully")
            print("\n")
            u.__password = password
            return True

        print("password not matched")
        print("Try again")
        print("\n")
        return False

    def get_data(self):
        return self.id,self.username,self.__password,self.name,self.age,self.dob
        
u = User()

def age_of_user():
    global user_profiles 
    user_profiles = accessing_the_user_data("user_profiles.JSON",u.id,False)
    for key,values in user_profiles.items():
        if str(key) == str(u.id):
            name = values["name"]
            dob = datetime.strptime(values["date_of_birth"], "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year
            if (today.month,today.day) < (dob.month,dob.day):
                age = age - 1
            u.age = age
            u.name = name
            u.dob = dob
             

def old_user_password(username):
    correct_old_password = False
    while(correct_old_password != True):
        password = input("Enter your password: ")
        correct_old_password = True

        if(correct_old_password == True):
            correct_old_password = User.check_password(password)

    age_of_user()
    closing_the_log_files(user_profiles,"user_profiles.JSON")

    
def old_username():
    global users
    correct_old_username = False
    while(correct_old_username != True):
        username = input("Enter your username: ")
        try:
            check_case_of_username(username)
            correct_old_username = True
        except InvalidUsername as error:
            print(error)

        if(correct_old_username != True):
                print("Username should be in lowercase")
                print("Try again")
                print("\n")
            
        if(correct_old_username == True):
            users = accessing_the_user_data("users.JSON",u.id,False)
            for keys,values in users.items():
                correct_old_username = False
                for  key, value in values.items():
                    if key == username:
                        u.id = keys
                        print("Username matched successfully")
                        print("\n")
                        u.username = username
                        correct_old_username = True
                        break
                if(correct_old_username == True):
                    break

        if(correct_old_username == False):
            print("Username not matched")
            print("Try again")
            print("\n")

    closing_the_log_files(users,"users.JSON")             
    old_user_password(username)
    
def getting_a_new_user_DOB(name,update_dob):
    global age
    global dob
    global user_profiles
    correct_dob = False
    while(correct_dob != True):
        if(update_dob == False):
            dob = input("Enter your Date of Birth(YYYY-MM-DD): ")
        else:
            user_profiles = accessing_the_user_data("user_profiles.JSON",u.id,False)
            dob = input("Update your DOB(YYYY-MM-DD): ").strip()
        try:
            check_dob_format(dob)
            correct_dob = True
        except InvalidDateOfBirth as error:
            print(error)

        if(correct_dob == True):
            dob = datetime.strptime(dob, "%Y-%m-%d").date()
            todays_date = datetime.now().date()
            age = todays_date.year - dob.year
            if (todays_date.month, todays_date.day) > (dob.month, dob.day):
                age = age - 1

            if(1 <= age <= 15):
                print("You are not eligible")
                print("Age should be greater than 15")
                print("Your account has been suspended")
                print("\n")
                users.pop(u.id,None)
            elif(age < 0):
                correct_dob = False
                print(age)
                print("Invlalid")
                print("Try again")
                print("\n")
            else:
                print(f"{dob} has been saved successfully")
                print("\n")

            if(correct_dob == True):
                u.dob = dob
                u.age = age
                if(update_dob == False):
                    user_profiles = accessing_the_user_data("user_profiles.JSON",u.id,False)
                    journal_entries= accessing_the_user_data("journal_entries.JSON",u.id,False)
                    journal_entries.update({u.id:{}})
                    journal_entries = closing_the_log_files(journal_entries,"journal_entries.JSON")

                dob = datetime.strftime(dob, "%Y-%m-%D")
                user_profiles.update({u.id:{"name": name,
                                            "signup_datetime": time_stamp,
                                            "date_of_birth": dob}})
                closing_the_log_files(user_profiles,"user_profiles.JSON")
                if(update_dob == True):
                    return dob  

def getting_a_new_user_name(update_name):
    global user_profiles
    name_list = None
    correct_new_user_name = False
    while(correct_new_user_name != True):
        if(update_name == False):
            name = input("What is your Fullname? ").title().strip()
        else:
            user_profiles = accessing_the_user_data("user_profiles.JSON",u.id,False)
            name = input("Update your Full Name: ").strip().title()
        try:
            name_list = name.split()
            for i in name_list:
                check_user_input(i)
            correct_new_user_name = True
            u.name = name
        except InvalidInput as error:
            print(error)
    if(update_name == True):
        user_profiles[u.id].update({"name":name}) 
        closing_the_log_files(user_profiles,"user_profiles.JSON")
        return name
    else:
        getting_a_new_user_DOB(name,False)


def new_user_password(new_username,update_password,entering_password):
    global time_stamp
    if entering_password == True:
        if(update_password == False):
            password = input("Enter a password: ")
        else:
            password = input("Update your password: ").strip()

    if update_password == False and entering_password == True:
            if(len(users) > 0):
                for key,values in users.items():
                    u.id = int(key) + 1
                    u.id= u.id
            else:
                u.id = 1
                u.id = u.id
    users = accessing_the_user_data("users.JSON",u.id,False)

    if(entering_password ==False):
        users.update({u.id:{new_username: u.password}})

    if(entering_password == True):
        users.update({u.id:{new_username: password}})

    time_stamp  = datetime.now().strftime("%D %H:%M:%S")
    closing_the_log_files(users,"users.JSON")

    if(update_password == False):
        getting_a_new_user_name(False)
    else:
        return password
    

def new_username(update_username):
    global users
    correct_new_username = False
    while(correct_new_username != True):
        if(update_username == False):
            username = input("Enter your username: ")
        else:
            users = accessing_the_user_data("users.JSON",u.id,False)
            username = input("Update your username: ").strip()
        try:
            check_case_of_username(username)
            correct_new_username = True
        except InvalidUsername as error:
            print(error)

        username_len = len(username.split())
        if(username_len != 1):
            print("len of username has been exceeded")
            correct_new_username = False
        users = accessing_the_user_data("users.JSON",00,False)
        if correct_new_username == True:
            for key,values in users.items():
                if username == key:
                    correct_new_username = False
                    print("Username already exists")
                    print("Enter again")
                    print("\n")
                    break

        if correct_new_username == True:
            print("Username saved successfully")
            print("\n")
            u.username = username
    if(update_username == False):
        new_user_password(username,False,True)
    else:
        new_user_password(username,False,False)
        return username

    
def user_confirmation():
    correct_user_choice = False
    while(correct_user_choice != True):
        user_choice = input("Are you a new user?(y/n) ").lower()
        try:
            check_user_input(user_choice)
            correct_user_choice = True
        except InvalidInput as error:
            print(error)

        if(correct_user_choice == True):
            if(user_choice == "n"):
                return "n"
            elif(user_choice == "y"):
                return "y"
            else:
                print("Wrong choice")
                print("Try again")
                correct_user_choice = False
                
