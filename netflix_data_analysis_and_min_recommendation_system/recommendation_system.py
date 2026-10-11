import pandas as pd
from datetime import datetime
from data_cleaning import media_catalog, tvShow_catalog, movie_catalog, movies_genres, media_genres, tvShow_genres
import time

watchList = []
movie_recommendations = []
tvshow_recommendations = []
media_recommendations = []

class InvalidInput(Exception):
     pass

def checkDataType(data, type_):
    if isinstance(data, type_) == False:
        raise InvalidInput(f"Invalid Input")

def loading():
    loading_ = ["/", "\\", "|", ".", "-"]
    for i in range(10):
        print(f"\r{loading_[i%4]:^10}", end="")
        time.sleep(0.5)
    print("\n")

# NEW: ranks titles by how many genres they share with the target (most shared first)
def rank_by_shared_genres(target, catalog):
    scored = []
    for item in catalog:
        if item.title != target.title:
            shared = len(set(target.listed_in).intersection(set(item.listed_in)))
            if shared >= 1:
                scored.append((shared, item))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [item for shared, item in scored]

def recommendation_choice():
    user_choice = False
    while(user_choice != True):
        choice = input("Do you want to continue (y/n): ").lower()
        if choice == "n":
            user_choice = True
            return False
        elif choice == "y":
            user_choice = True
            return True
        else:
            print("Invalid choice")


def media_choice():
    correct_media_input = False
    while(correct_media_input != True):
            print(f"{"-"*20:<10}")
            print("1 - Movie")
            print("2 - TV Shows")
            print("3 - Both")
            print(f"{"-"*20:<10}")
            try:
                media_input = int(input("Enter your choice: "))
                checkDataType(media_input, int)
                correct_media_input = True
            except (InvalidInput, ValueError) as error:
                print(error)

    return media_input

def addToWatchlist(media):
    global watchList

    correct_watchList_choice = False
    while correct_watchList_choice != True:
        watchList_choice = input("Do you want to add it in watchlist? (y/n): ").lower().strip()
        if len(watchList_choice) == 1 and (watchList_choice == "y" or watchList_choice == "n"):
            correct_watchList_choice = True
        else:
            print("Invalid choice")

    if correct_watchList_choice == True:
        if watchList_choice == "y":
            if media not in watchList:
                watchList.append(media)

def searchByYear():
    print(f"{"="*30:^30}")
    print(f"{"SEARCH BY YEAR":^30}")
    print(f"{"="*30:^30}")

    correct_year_input = False
    while(correct_year_input != True):
        try:
            year_input = int(input("Enter a year: "))
            checkDataType(year_input, int)
            correct_year_input = True
        except (InvalidInput, ValueError) as error:
            print(error)

    media_input = media_choice()
    year_found = False

    if media_input == 1:
        loading()
        for movie in movie_catalog:
            if movie.release_year == year_input:
                year_found = True
                movie.showDetails()
                addToWatchlist(movie)
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
    elif media_input == 2:
        loading()
        for tvshow in tvShow_catalog:
            if tvshow.release_year == year_input:
                year_found = True
                tvshow.showDetails()
                addToWatchlist(tvshow)
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
    else:
        loading()
        for media in media_catalog:
            if media.release_year == year_input:
                year_found = True
                media.showDetails()
                addToWatchlist(media)
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break

    if year_found == False:
        print(f"{"-"*30:<10}")
        print("No media found for that year")
        print(f"{"-"*30:<10}")
    return

def searchByKeyword():
    print(f"{"="*30:^30}")
    print(f"{"SEARCH BY KEYWORD":^30}")
    print(f"{"="*30:^30}")

    keyword_found = False
    keyword_input = input("Enter a keyword: ").strip().lower()
    loading()
    for media in media_catalog:
        # CHANGED: punctuation is stripped from each word, so "love." now matches "love"
        if keyword_input in (word.lower().strip(".,!?;:'\"()") for word in media.description_list):
            keyword_found = True
            media.showDetails()
            addToWatchlist(media)
            end_the_loop = recommendation_choice()
            if end_the_loop == False:
                break

    if keyword_found == False:
        print(f"{"-"*30:<10}")
        print("Keyword not matched")
        print(f"{"-"*30:<10}")
    return

def searchByGenre():
    print(f"{"="*30:^30}")
    print(f"{"SEARCH BY GENRE":^30}")
    print(f"{"="*30:^30}")

    genre_input = input("Enter a genre to search: ").strip().title()
    media_input = media_choice()

    if media_input == 1:
        if genre_input in movies_genres:
            loading()
            for movie in movies_genres[genre_input]:
                movie.showDetails()
                addToWatchlist(movie)
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
        else:
            print(f"{"-"*30:<10}")
            print("Movie not found")
            print(f"{"-"*30:<10}")
    elif media_input == 2:
        if genre_input in tvShow_genres:
            loading()
            for tvshow in tvShow_genres[genre_input]:
                tvshow.showDetails()
                addToWatchlist(tvshow)
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
        else:
            print(f"{"-"*30:<10}")
            print("TVShow not found")
            print(f"{"-"*30:<10}")
    else:
        if genre_input in media_genres:
            loading()
            for media in media_genres[genre_input]:
                media.showDetails()
                addToWatchlist(media)
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
        else:
            print(f"{"-"*30:<10}")
            print("Media not found")
            print(f"{"-"*30:<10}")

    return

def searchAMedia():
    print(f"{"="*30:^30}")
    print(f"{"SEARCH A MEDIA":^30}")
    print(f"{"="*30:^30}")

    target = None
    found = False
    media_input = media_choice()
    if media_input == 1:
        # CHANGED: both sides are compared in lowercase, so titles like "WALL-E" now match
        movie_input = input("Enter a movie name: ").lower().strip()
        loading()
        for movie in movie_catalog:
            if movie.title.lower() == movie_input:
                movie.showDetails()
                found = True
                target = movie
                break
        if found == True:
            # CHANGED: recommendations are ranked by number of shared genres
            for movie in rank_by_shared_genres(target, movie_catalog):
                if movie not in movie_recommendations:
                    movie_recommendations.append(movie)
        if found == False:
            print(f"{"-"*30:<10}")
            print("Movie not found")
            print(f"{"-"*30:<10}")

    elif media_input == 2:
        tvShow_input = input("Enter a TV Show name: ").lower().strip()
        loading()
        for tvshow in tvShow_catalog:
            if tvshow.title.lower() == tvShow_input:
                tvshow.showDetails()
                found = True
                target = tvshow
                break
        if found == True:
            for tvshow in rank_by_shared_genres(target, tvShow_catalog):
                if tvshow not in tvshow_recommendations:
                    tvshow_recommendations.append(tvshow)
        if found == False:
            print(f"{"-"*30:<10}")
            print("TV Show not found")
            print(f"{"-"*30:<10}")

    else:
        media_input = input("Enter a media name: ").lower().strip()
        loading()
        for media in media_catalog:
            if media.title.lower() == media_input:
                media.showDetails()
                found = True
                target = media
                break
        if found == True:
            for media in rank_by_shared_genres(target, media_catalog):
                if media not in media_recommendations:
                    media_recommendations.append(media)
        if found == False:
            print(f"{"-"*30:<10}")
            print("Media not found")
            print(f"{"-"*30:<10}")

    input(f"Press any key to return to menu: ")
    return

def recommendations():
    print(f"{"="*30:^30}")
    print(f"{"RECOMMENDATIONS":^30}")
    print(f"{"="*30:^30}")

    media_input = media_choice()
    if media_input == 1:
        if len(movie_recommendations) >= 1:
            loading()
            for movie in movie_recommendations:
                movie.showDetails()
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
        else:
            print(f"{"-"*30:<10}")
            print("Movie not found")
            print(f"{"-"*30:<10}")
    elif media_input == 2:
        if len(tvshow_recommendations) >= 1:
            loading()
            for tvshow in tvshow_recommendations:
                tvshow.showDetails()
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
        else:
            print(f"{"-"*30:<10}")
            print("TV Show not found")
            print(f"{"-"*30:<10}")
    else:
        if len(media_recommendations) >= 1:
            loading()
            for media in media_recommendations:
                media.showDetails()
                end_the_loop = recommendation_choice()
                if end_the_loop == False:
                    break
        else:
            print(f"{"-"*30:<10}")
            print("Media not found")
            print(f"{"-"*30:<10}")
    return

def menu():

    correct_choice = False
    while(correct_choice != True):
        print(f"{"="*20:^20}")
        print(f"{"MAIN MENU":^20}")
        print(f"{"="*20:^20}")
        print("1 - Search a movie by title")
        print("2 - Search movies by year")
        print("3 - Search by a keyword")
        print("4 - Search by genres")
        print("5 - Recommendations based on your Search")
        print("6 - Exit")
        print(f"{"-"*20:<10}")

        try:
            choice = int(input("Enter a choice: "))
            checkDataType(choice, int)
            correct_choice = True
        except (InvalidInput, ValueError) as error:
            print(error)

        if correct_choice == True:
            correct_choice = False
            if choice == 1:
                searchAMedia()
            elif choice == 2:
                searchByYear()
            elif choice == 3:
                searchByKeyword()
            elif choice == 4:
                searchByGenre()
            elif choice == 5:
                recommendations()
            elif choice == 6:
                correct_choice = True
                loading()
                exit(0)
            else:
                print("Invalid Choice")

menu()
