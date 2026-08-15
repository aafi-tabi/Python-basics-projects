movies_catalog = {
    "john wick": ["action", "crime", "thriller"],
    "mad max: fury road": ["action", "adventure", "sci-fi"],
    "mission: impossible – fallout": ["action", "spy", "thriller"],
    "the dark knight": ["action", "crime", "superhero"],
    "top gun: maverick": ["action", "drama", "adventure"],
    "avengers: endgame": ["superhero", "action", "sci-fi"],
    "spider-man: into the spider-verse": ["animation", "superhero", "adventure"],
    "logan": ["superhero", "action", "drama"],
    "black panther": ["superhero", "action", "adventure"],
    "interstellar": ["sci-fi", "adventure", "drama"],
    "the matrix": ["sci-fi", "action", "cyberpunk"],
    "blade runner 2049": ["sci-fi", "thriller", "mystery"],
    "arrival": ["sci-fi", "drama", "mystery"],
    "dune": ["sci-fi", "adventure", "drama"],
    "the lord of the rings: the fellowship of the ring": ["fantasy", "adventure", "action"],
    "harry potter and the sorcerer's stone": ["fantasy", "adventure", "family"],
    "the chronicles of narnia: the lion, the witch and the wardrobe": ["fantasy", "adventure", "family"],
    "the hobbit: an unexpected journey": ["fantasy", "adventure", "action"],
    "the hangover": ["comedy", "adventure", "buddy"],
    "superbad": ["comedy", "coming-of-age", "teen"],
    "21 jump street": ["comedy", "action", "crime"],
    "free guy": ["action", "comedy", "sci-fi"],
    "titanic": ["romance", "drama", "historical"],
    "the notebook": ["romance", "drama", "melodrama"],
    "la la land": ["romance", "musical", "drama"],
    "pride & prejudice": ["romance", "drama", "historical"],
    "the conjuring": ["horror", "supernatural", "mystery"],
    "hereditary": ["horror", "psychological", "drama"],
    "a quiet place": ["horror", "sci-fi", "thriller"],
    "it": ["horror", "supernatural", "drama"],
    "se7en": ["crime", "thriller", "mystery"],
    "gone girl": ["thriller", "mystery", "crime"],
    "knives out": ["mystery", "comedy", "crime"],
    "shutter island": ["mystery", "thriller", "psychological"],
    "the godfather": ["crime", "drama", "gangster"],
    "the departed": ["crime", "thriller", "drama"],
    "pulp fiction": ["crime", "drama", "dark comedy"],
    "goodfellas": ["crime", "drama", "biography"],
    "the shawshank redemption": ["drama", "crime", "prison"],
    "forrest gump": ["drama", "romance", "comedy"],
    "the pursuit of happyness": ["drama", "biography", "family"],
    "whiplash": ["drama", "music", "psychological"],
    "paddington 2": ["family", "comedy", "adventure"],
    "the parent trap": ["family", "comedy", "romance"],
    "mary poppins": ["family", "fantasy", "musical"],
    "toy story": ["animation", "comedy", "family"],
    "spirited away": ["animation", "fantasy", "adventure"],
    "coco": ["animation", "family", "fantasy"],
    "your name": ["animation", "romance", "fantasy"],
    "jurassic park": ["adventure", "sci-fi", "thriller"],
    "pirates of the caribbean: the curse of the black pearl": ["adventure", "fantasy", "action"],
    "indiana jones and the raiders of the lost ark": ["adventure", "action", "historical"],
    "the revenant": ["adventure", "drama", "survival"],
    "the greatest showman": ["musical", "drama", "biography"],
    "mamma mia!": ["musical", "romance", "comedy"],
    "les misérables": ["musical", "drama", "historical"],
    "schindler's list": ["historical", "drama", "war"],
    "oppenheimer": ["biography", "historical", "drama"],
    "gladiator": ["historical", "action", "drama"],
    "alien": ["horror", "sci-fi", "thriller"],
    "aliens": ["action", "sci-fi", "horror"],
    "the martian": ["sci-fi", "adventure", "drama"],
    "gravity": ["sci-fi", "thriller", "drama"]
}

top_recommendations = []
user_choice_movie_genres = []
user_info_database = {
    "aafia" : "aafitabi",
    "aaryan" : "aaryan123",
    "jazib" : "jazib00"
}
username = ["None"]
password = ["None"]
new_username = ["None"]
new_password = ["None"]
conversation_log =[]
name = None
password = None

conversation_log.append(("=" * 10).lower().strip().split())
conversation_log.append("WELCOME".lower().strip().split())
conversation_log.append(("=" * 10).lower().strip().split())

print("\n")
print("=" * 10)
print("WELCOME")
print("=" * 10)
print("\n")

matched_name = False
matched_password = False
user_status_choice = False

while user_status_choice != True:

    conversation_log.append("Are you a new user or old user?".lower().strip().split())
    conversation_log.append("1 - Old User".lower().strip().split())
    conversation_log.append("2 - New User".lower().strip().split())

    print("Are you a new user or old user?")
    print("1 - Old User")
    print("2 - New User")

    conversation_log.append("Enter your choice: ".lower().strip().split())
    user_status = input("Enter your choice: ").lower().strip().split()
    conversation_log.append(user_status)
    print("\n")

    if user_status ==  ["1"] or user_status == ["2"]:

        if user_status == ["1"]:

            user_status_choice = True
            while matched_name != True:
                conversation_log.append("Enter your username: ".lower().strip().split())
                username = input("Enter your username: ").lower().strip().replace(",","").replace("!","").split()
                conversation_log.append(username)
                
                for keys, values in user_info_database.items():
                    if "".join(username) == keys:
                        print("Entered name is correct")
                        print("\n")
                        conversation_log.append("Entered name is correct".lower().strip().split())
                        matched_name = True
                        break

                if matched_name == False:
                    conversation_log.append("Name not matched".lower().strip().split())
                    conversation_log.append("Try again".lower().strip().split())
                    print("Name not matched")
                    print("Try again")
                    print("\n")

            while matched_password != True:
                conversation_log.append("Enter a password: ".lower().strip().split())
                password = input("Enter a password: ")
        
                if "".join(password) == user_info_database["".join(username)]:
                    print("Entered password is correct")
                    print("\n")
                    conversation_log.append("Entered password is correct".lower().strip().split())
                    print("\n")
                    matched_password =  True
                    break

                if matched_password == False:
                    conversation_log.append("Password not matched".lower().strip().split())
                    conversation_log.append("Try again".lower().strip().split())
                    print("Password not matched")
                    print("Try again")
                    print("\n")

            name = "".join(username)
            password = "".join(password)


        elif user_status == ["2"]:

            user_status_choice = True
            matched_new_username = True
            correct_username = False

            while correct_username != True or matched_new_username != False:

                matched_new_username = True
                correct_username = False

                new_username = input("Enter your username(in lowercase): ").strip().split()

                for i in new_username:
                    if i == i.lower():
                        correct_username = True
                    else:
                        correct_username = False
                        break

                if correct_username == False:
                    print("Username shoud be in lowercase!")
                    print("\n")
        

                if correct_username == True:
                    for keys,values in user_info_database.items():
                        if "".join(new_username) == keys:
                            matched_new_username =  True
                            break
                        else:
                            matched_new_username = False
                        
                if correct_username == True:
                    if matched_new_username ==  True:
                        print("Username has already in used")
                        print("Try again")
                        print("\n")

            print("Your new username has been saved")
            print("\n")

            new_password = input("Enter your password: ")
            print("\n")

            password = new_password
            name = "".join(new_username)

        else:
            user_status_choice = False

user_info_database.update({"".join(new_username) : new_password})

    
if name in user_info_database.keys() and password in user_info_database.values():

    if user_status == ["2"]:
        print(f"Welcome, {name.title()}")
        print("\n")
    else:
        print(f"Welome back, {name.title()}")
        print("\n")

    movies_genre_input_sz = False
    movies_genre_input = None
    user_choice = None

    while user_choice != ["quit"]:
        print("Enter your favourite genre one by one:")
        print("Enter \"quit\" to exit:")
        print("0 - Enter genres")

        user_choice = input("Enter a user choice: ").lower().strip().replace(",","").replace("!","").split()
        print("\n")

        if user_choice ==  ["0"]:
            movies_genre_input = None

            while movies_genre_input != ["quit"]:
                movies_genre_input_sz = False
                while movies_genre_input_sz != True:
                    movies_genre_input = input("Enter a genre in one word(\"quit\" to exit): ").lower().strip().replace(",","").replace("!","").split()
                    
                    if len(movies_genre_input) != 1:
                        movies_genre_input_sz = False
                    else:
                        movies_genre_input_sz = True
                        if movies_genre_input != ["quit"]:
                            user_choice_movie_genres.append("".join(movies_genre_input))
                        else:
                            user_choice = ["quit"]
        else: 
            if user_choice != ["quit"]:
                print("Wrong choice")
                print("Try again")

    if len(user_choice_movie_genres) != 0:
        movie_genre = []
        movies_genre = []
        match_genres_in_num = 0
        match_genres_in_num_list = []
        three_genres_matched = dict()
        two_genres_matched = dict()
        one_genres_matched = dict()
        top_recommendations_suggestions = dict()
        top_recommendations = dict()

        for key,values in movies_catalog.items():
            match_genres_in_num = 0
            for j in values:
                for i in user_choice_movie_genres:
                    if i == j:
                        match_genres_in_num += 1
                        movie_genre.append(i)

            movies_genre.append(movie_genre)
            match_genres_in_num_list.append(match_genres_in_num)

            if match_genres_in_num == 3:
                three_genres_matched.update({key : values})
            elif match_genres_in_num == 2:
                two_genres_matched.update({key : values})
            elif match_genres_in_num == 1:
                one_genres_matched.update({key : values})
            else:
                pass
            

        movies_genre = sorted(movies_genre)
        match_genres_in_num_list = sorted(match_genres_in_num_list)

        for keys,values in three_genres_matched.items():
            top_recommendations_suggestions.update({keys :  values})

        if len(top_recommendations_suggestions) < 10:
            for keys, values in two_genres_matched.items():
                top_recommendations_suggestions.update({keys : values})

        if len(top_recommendations_suggestions) < 10:
                for keys, values in one_genres_matched.items():
                    top_recommendations_suggestions.update({keys : values})
                
        print("\n")
        print("choose from these recommendations: ")

        more_recommendations = True
        j = 0
        stop_the_loop = None

        for keys,values in top_recommendations_suggestions.items():
            if j == 0:
                stop_the_loop = keys
                j += 1
                break

        length_of_top_recommendations_suggestions = len(top_recommendations_suggestions)
        i = 1
        while more_recommendations != False:
            for keys,values in top_recommendations_suggestions.items():
                i += 1
                user_recommendation_choice_ = False
                while user_recommendation_choice_ != True:
                    print(f"{keys}: {values}")
                    print("\n")
                    print("1 - accept")
                    print("2 - reject")
                    print("\n")
                    user_recommendation_choice = input("Enter a choice: ").lower().strip().replace(",","").replace("!","").split()

                    if user_recommendation_choice == ["1"]:
                        top_recommendations.update({keys: values})
                        user_recommendation_choice_ = True
                        break
                    elif user_recommendation_choice == ["2"]:
                        user_recommendation_choice_ = True
                        break
                    else:
                        print("Wrong choice has been entered")
                        print("Try again")
                        print("\n")
                        user_recommendation_choice_ = False

                choice  = True
                while choice != False:
                    more_recommendations_choice = input("Suggest more recommendations(y/n): ").lower().strip().replace(",","").replace("!","").split()

                    if more_recommendations_choice == ["y"]:
                        more_recommendations = True
                        choice  = False
                    elif more_recommendations_choice == ["n"]:
                        more_recommendations = False
                        choice  = False
                    else:
                        print("Wrong choice has been entered")
                        print("Try again")
                        print("\n")
                        choice  = True

                if choice == False and more_recommendations == False:
                    break
                if length_of_top_recommendations_suggestions == i:
                    print("\n")
                    print("Recommendations suggestions has been ended")
                    print("\n")
                    more_recommendations = False
                    choice  = False
                    break

    if len(top_recommendations) >= 1:
        print("=" * 30)
        print("Here are your Top Recommendations")
        print("=" * 30)
        for keys,values in top_recommendations.items():
            print(f"{keys}: {values}")
        print("\n")
    else:
        print("No personalized recommendations")
        print("\n")

    print(f"Good Bye,{name.title()}")

