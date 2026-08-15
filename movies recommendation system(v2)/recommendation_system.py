import json
import time

try:
    with open("movies_catalog.JSON","r") as file:
        movies_catalog = json.load(file)
except FileNotFoundError:
    print("\"movies_catalog.JSON\" not found")

try:
    with open("movies_genres.JSON","r") as file:
        movies_genres = json.load(file)
except FileNotFoundError:
    print("\"movies_catalog.JSON\" not found  ")

user_choice_movies_genres = []
top_recommendations = dict()
recommended_movies = dict()
user_choice_movies_genres = []
movie_search_count = 0
movie_review_update_count = 0
movie_rating_update_count = 0
user_choice_movie_genres = None

def loading_movies():
    spinner = ["\\","/","-","."]
    for  i in range(8):
        print(f"\r{spinner[i%4]}",end="")
        time.sleep(0.3)
    print("\n")

def main_menu():
    global movie_search_count
    global movie_review_update_count
    global movie_rating_update_count
    global user_choice_movie_genres

    user_choice = True
    while user_choice == True:
        print("\n")
        print(f"{"=" * 30:^30}")
        print(f"{"MAIN MENU":^30}")
        print(f"{"=" * 30:^30}")
        
        print(f"{"1 - Enter your favourite genres":<30}")
        print(f"{"2 - Movies recommendendation":<30}")
        print(f"{"3 - Search a movie":<30}")
        print(f"{"4 - Update a movie review":<30}")
        print(f"{"5 - Update a movie rating":<30}")
        print(f"{"6 - Genre average rating":<30}")
        print(f"{"7 - Personalized recommendations for you":<30}")
        print(f"{"8 - Final Movies Report":<30}")
        print(f"{"9 - Exit":<30}")
        print(f"{"-"*30:<10}")

        try:
            choice = int(input(f"{"Enter a choice: ":<28}"))
            

            if choice == 1:
                user_choice_movie_genres = user_genre_choice()
            elif choice == 2:
                if len(recommended_movies) > 0:
                    movie_recommendation_suggestion()
                else:
                    print("No recommendations yet")
            elif choice == 3:
                movie_search_count = movie_search()
            elif choice == 4:
                movie_review_update_count = movie_review_update()
            elif choice == 5:
                movie_rating_update_count = movie_rating_update()
            elif choice == 6:
                average_of_movies_genre_rating()
            elif choice == 7:
                top_recommendations_selected()
            elif choice == 8:
                movies_report()
            elif choice == 9:
                print("Exiting successfully")
                loading_movies()
                print("\n")
                user_choice = False
            else:
                print(f"{"-"*30:<10}")
                print(f"{"Wrong choice":<30}")
                print(f"{"Try again":<30}")
                print("\n")
        except ValueError:
            print(f"{"-"*30:<10}")
            print(f"{"choice is invalid":<30}")
            print(f"{"Try again":<30}")
            print("\n")
    
def movies_genres_choice_by_user():
    global movies_catalog
    matched_genres_counter = 0
    global recommended_movies 

    for key,values in movies_catalog.items():
        matched_genres_counter = 0
        for i in values["genres"]:
            for j in user_choice_movies_genres:
                if i == j:
                    matched_genres_counter += 1
        if matched_genres_counter > 0:
            values.update({"matched_genres": matched_genres_counter})
            recommended_movies.update({key:values})

    recommended_movies = dict(sorted(recommended_movies.items(), key=lambda x: x[1]["matched_genres"],reverse=True))
    for key,values in recommended_movies.items():
        del values["matched_genres"]

def user_genre_choice():
    print("\n")
    print(f"{"=" * 30:<30}")
    print(f"{"USER GENRE CHOICE":<30}")
    print(f"{"=" * 30:<}")
    print("\n")
    global user_choice_movies_genres
    user_genre_choice_ = True
    while user_genre_choice_ == True:
        user_genre_choice_input = input("Enter a favourite genre in one word(quit to exit): ").title().strip().replace(",","").replace("!","").split()
        if len(user_genre_choice_input) != 1 and user_genre_choice_input !=["Quit"]:
            print("lenght of a words exceeded")
            print("Try again")
            print("\n")
        elif user_genre_choice_input == ["Quit"]:
            user_genre_choice_ = False
        else:
            matched_genre = False
            for i in user_choice_movies_genres:
                if "".join(user_genre_choice_input) == i:
                    matched_genre = True
            if matched_genre == False:
                user_choice_movies_genres.append("".join(user_genre_choice_input))
    movies_genres_choice_by_user()
    return user_choice_movies_genres

def average_of_movies_genre_rating():
    print("\n")
    print(f"{"=" * 40:^40}")
    print(f"{"MOVIES GENRE AVERAGE RATING":^40}")
    print(f"{"=" * 40:^40}")
    print("\n")
    genre_rating_review = dict()

    for i in movies_genres:
        total = 0
        number_of_movies = 0
        for key,values in movies_catalog.items():
            for j in values["genres"]:
                if  i == j:
                    total += values["rating"]
                    number_of_movies += 1
        if number_of_movies > 0:
            genre_rating_avg = total/number_of_movies
            genre_rating_review.update({i: genre_rating_avg})
    loading_movies()
    for key,values in genre_rating_review.items():
        print(f"{f"{key}: {values:.2f}":<10}")



def high_rating_movies():
    top_rating_movie = None
    movie_rating = 0

    for key,values in movies_catalog.items():
        if values["rating"] > movie_rating:
            movie_rating = values["rating"]
            top_rating_movie = key
    return top_rating_movie

def genre_with_most_movies():
    total_movie_genres = 0
    movie_genre_counter = 0
    top_genre = None

    for i in movies_genres:
        total_movie_genres = 0
        for key,values in movies_catalog.items():
            for j in values["genres"]:
                if  i == j:
                    total_movie_genres += 1
        if movie_genre_counter < total_movie_genres:
            movie_genre_counter = total_movie_genres
            top_genre = i
    return top_genre


def movie_search():
    print("\n")
    print(f"{"=" * 20:^30}")
    print(f"{"MOVIES SEARCH":^30}")
    print(f"{"=" * 20:^30}") 
    print("\n")
    movie_search_counter = 0
    movie_search_input = None

    while movie_search_input != "Quit":
        movie_found = False
        movie_search_input = input("Enter a movie to search(quit to exit): ").title().strip()
        if movie_search_input != "Quit":
            movie_search_counter += 1
            for key,values in movies_catalog.items():
                if key == movie_search_input:
                    loading_movies()
                    print(f"{key}: {values}")
                    print("\n")
                    movie_found = True
                    break 
            if movie_found == False:
                print(f"{"-"*30:<10}")
                loading_movies()
                print("Movie not found")
                print("Try again")
                print("\n")
    return movie_search_counter


def movie_recommendation_suggestion():
    print("\n")
    print(f"{"=" * 25:<30}")
    print(f"{"MOVIE RECOMENDATIONS":<30}")
    print(f"{"=" * 25:<30}")
    print("\n")
    global top_recommendations
    more_recommendation  = True
    lenght_of_a_recommended_movies = len(recommended_movies)
    i = 0

    while more_recommendation != False:
        for key, values in recommended_movies.items():
            i += 1
            print(f"{key}: {values}")
            print(f"{"-"*30:<10}")
            print("1 - Accept")
            print("2 - Reject")
            print(f"{"-"*30:<10}")
            try:
                movie_recommendation_choice = int(input("Enter a choice: "))
                if movie_recommendation_choice == 1:
                    top_recommendations.update({key: values})
                elif movie_recommendation_choice == 2:
                    pass
                else: 
                    pass
            except ValueError:
                print("Wrong value")
                print("Try again")
                print("\n")
            try:
                more_recommendation_choice = input("Do you want to see more recommendations(y/n)? ").lower().strip()
                print("\n")
                if more_recommendation_choice == "y":
                    more_recommendation  = True
                elif more_recommendation_choice == "n":
                    more_recommendation = False
                    break
            except ValueError:
                print("Wrong value")
                print("Try again")
                print("\n")
            
            if i == lenght_of_a_recommended_movies:
                print("Recommendations has been ended")
                print("\n")

                more_movies_addition = True
                while more_movies_addition != False:
                    recommended_movies_addition = input("Do you want to add a more movies in your recommendations(y/n):").lower().strip()
                    print("\n")
                    if recommended_movies_addition == "y":
                        movie_found = False
                        movie_name = input("Enter a movie name: ").lower().strip()
                        loading_movies()
                        for key,values in movies_catalog.items():
                            if movie_name == key:
                                top_recommendations.update({key: values})
                                print(f"{key} has been added")
                                print("\n")
                                movie_found = True
                                break
                        if movie_found ==  False:
                            print("Movie not found")
                            print("Try again")
                            print("\n")
                    elif recommended_movies_addition == "n":            
                        more_recommendation = False
                        more_movies_addition = False
                        break
                    else:
                        print("Wrong choice")
                        print("Try again")
                        print("\n") 

        if more_recommendation ==  False:
            break


def top_recommendations_selected():
    print("\n")
    print(f"{"=" * 40:<30}")
    print(f"{"PERSONALIZED RECOMMENDATIONS":<40}")
    print(f"{"=" * 40:<}")
    print("\n")
    loading_movies()
    for key,values in top_recommendations.items():
        print(f"{key}: {values}")

def movie_rating_update():
    print("\n")
    print(f"{"=" * 30:^30}")
    print(f"{"MOVIES RATING UPDATE":^30}")
    print(f"{"=" * 30:^30}")
    print("\n")
    movie_rating_input = None
    movie_rating_update_counter = 0

    while movie_rating_input != "Quit":
        movie_found = False
        movie_rating_input = input("Enter a movie to update(quit to exit): ").title().strip()
        if movie_rating_input != "Quit":
            movie_rating_update_counter += 1
            loading_movies()
            for key,values in movies_catalog.items():
                if key == movie_rating_input:
                    print(f"{key}: {values}")
                    print("\n")
                    movie_found = True
                    break 
            if movie_found == True:
                movie_rating_status = True
                while movie_rating_status != False:
                    try:
                        movie_rating = float(input("Enter a movie rating  to update(0 to 5): "))
                        if 0 <= movie_rating <= 5:
                            values.update({"rating": movie_rating})
                            print(f"{"-"*30:<10}")
                            print("Rating updated successfully")
                            print("\n")
                            movie_rating_status = False
                        else:
                            print(f"{"-"*30:<10}")
                            print("You are entering a wrong rating")
                            print("Try again")
                            print("\n")
                    except ValueError:
                        print("Entered Value is wrong")
                        print("Try again")
                        print("\n")
            if movie_found == False:
                print(f"{"-"*30:<10}")
                print("Movie not found")
                print("Try again")
                print("\n")
    return movie_rating_update_counter


def movie_review_update():
    print("\n")
    print(f"{"=" * 20:^10}")
    print(f"{"MOVIES REVIEW UPDATE":^10}")
    print(f"{"=" * 20:^10}")
    print("\n")
    movie_review_input = None
    movie_review_counter = 0

    while movie_review_input != "Quit":
        movie_found = False
        movie_review_input = input("Enter a movie to update(quit to exit): ").title().strip()
        if movie_review_input != "Quit":
            movie_review_counter += 1
            loading_movies()
            for key,values in movies_catalog.items():
                if key == movie_review_input:
                    print(f"{key}: {values}")
                    print("\n")
                    movie_found = True
                    break 
            if movie_found == True:
                movie_review = input("Enter a movie review to update: ").lower().strip()
                values.update({"review": movie_review})
                print(f"{"-"*30:<10}")
                print("Review updated successfully")
                print("\n")
            if movie_found == False:
                print(f"{"-"*30:<10}")
                print("Movie not found")
                print("Try again")
                print("\n")
    return movie_review_counter

def movies_report():
    print("\n")
    print(f"{"=" * 20:^30}")
    print(f"{"MOVIES REPORT":^30}")
    print(f"{"=" * 20:^30}")
    print("\n")
    loading_movies()
    print(f"{f"Movie search count: {movie_search_count}":<30}")
    print(f"{f"Movie review update count: {movie_review_update_count}":<30}")
    print(f"{f"Movie rating update count: {movie_rating_update_count}":<30}")
    print(f"{f"Your favourite genres: {user_choice_movie_genres}":<30}")
    print(f"{f"Top rating movie: {high_rating_movies()}":<30}")
    print(f"{f"Genre with most movies: {genre_with_most_movies()}":<30}")


main_menu()
