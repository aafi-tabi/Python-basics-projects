import pandas as pd
from datetime import datetime
import numpy as np

class Title:
    show_id = 0
    type_ = None
    title = None
    director = None
    cast = None
    country = None
    date_added = None
    release_year = None
    rating = 0
    listed_in = None
    description = None
    description_list = None
    primary_country = None
    years_bw_release_and_added = None
    year_added = None
    day_added = None
    month_added = None

    def __init__(self, show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country):
        self.show_id = show_id
        self.type_ = type_
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.listed_in = listed_in
        self.description = description
        self.description_list = description_list
        self.month_added = month_added
        self.day_added = day_added
        self.year_added = year_added
        self.years_bw_release_and_added = years_bw_release_and_added
        self.primary_country = primary_country

class Movie(Title):
        runtime = 0
        def __init__(self, show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country, mins_duration):
             super().__init__(show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country)
             self.runtime = mins_duration

        def showDetails(self):
            print(f"Movie name: {self.title}")
            print(f"Description: {self.description}")
            print(f"Rating: {self.rating}")
            print(f"Genres: {self.listed_in}")
            print(f"Cast: {self.cast}")
            print(f"Director: {self.director}")
            print(f"Duration in mins: {self.runtime}")
            print(f"{"-"*35:<10}")

class TVShow(Title):
    seasons = 0
    def __init__(self, show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country, seasons_duration):
        super().__init__(show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country)
        self.seasons = seasons_duration

    def showDetails(self):
        print(f"TV Show name: {self.title}")
        print(f"Description: {self.description}")
        print(f"Rating: {self.rating}")
        print(f"Cast: {self.cast}")
        print(f"Director: {self.director}")
        print(f"Duration in seasons: {self.seasons}")
        print(f"{"-"*35:<10}")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)

netflix_data = pd.read_csv("netflix_titles.CSV")
media_genres = dict()
tvShow_genres = dict()
movies_genres = dict()

def data_info():
    print(f"{"="*35:^35}")
    print(f"{"DATA INFO":^35}")
    print(f"{"="*35:^35}")
    print(f"First 5 rows of file: {netflix_data.head()}")
    print(f"{"-"*35:<10}")
    print(f"Info about the file: {netflix_data.info()}")
    print(f"{"-"*35:<10}")

    print(f"Shape of Date: {netflix_data.shape}")
    print(f"{"-"*35:<10}")

    print(f"""Info about the NULL values: 
    {netflix_data.isnull().sum()}""")
    print(f"{"-"*35:<10}")

def data_cleaning():
    netflix_data["director"] = netflix_data["director"].fillna("Unknown")
    netflix_data["country"] = netflix_data["country"].fillna("Unknown")
    netflix_data["cast"] = netflix_data["cast"].fillna("Unknown")
    netflix_data["listed_in"] = netflix_data["listed_in"].fillna("Unknown")

    netflix_data.dropna(subset="date_added", inplace=True)
    netflix_data.dropna(subset="rating", inplace=True)
    netflix_data.dropna(subset="duration", inplace=True)

    print(f"{"="*35:^35}")
    print(f"{"DATA CLEANING":^35}")
    print(f"{"="*35:^35}")
    print(f"""Info about the NULL values after cleaning: 
    {netflix_data.isnull().sum()}""")
    print(f"{"-"*35:<10}")

    print(f"Shape of a Data after cleaning: {netflix_data.shape}")
    print(f"{"-"*35:<10}")

def min_categorize(type_list):
    if type_list[1] == "min":
        return type_list[0]
    else:
        return -1

def season_categorize(type_list):
    if type_list[1].lower() == "seasons" or type_list[1].lower() == "season":
        return type_list[0]
    else:
        return -1

def converting_to_datetime():
    netflix_data["release_year"] = netflix_data["release_year"].astype(str)
    netflix_data["release_year"] = pd.to_numeric(netflix_data["release_year"], errors="coerce")
    netflix_data["date_added"] = pd.to_datetime(netflix_data["date_added"], format="mixed")

def data_splitting():
    global netflix_data
    netflix_data["cast"] = netflix_data["cast"].str.split(", ")
    netflix_data["listed_in"] = netflix_data["listed_in"].str.split(", ")
    netflix_data["description"] = netflix_data["description"].str.replace(",", "")
    netflix_data["description_list"] = netflix_data["description"].str.split()
    netflix_data["country"] = netflix_data["country"].str.split(", ")

def new_columns():
    netflix_data["month_added"] = netflix_data["date_added"].dt.month_name()
    netflix_data["day_added"] = netflix_data["date_added"].dt.day
    netflix_data["year_added"] = netflix_data["date_added"].dt.year
    netflix_data["years_between_release_and_added"] = netflix_data["release_year"] - netflix_data["year_added"]
    netflix_data["primary_country"] = netflix_data["country"].str[0]

def duration_spliting():
    global netflix_data
    netflix_data["duration_list"] = netflix_data["duration"].str.split()
    netflix_data["mins_duration"] = netflix_data["duration_list"].apply(min_categorize)
    netflix_data["mins_duration"] = pd.to_numeric(netflix_data["mins_duration"], errors="coerce")
    netflix_data["seasons_duration"] = netflix_data["duration_list"].apply(season_categorize)
    netflix_data["seasons_duration"] = pd.to_numeric(netflix_data["seasons_duration"], errors="coerce")
    netflix_data.drop(columns=["duration_list"], inplace=True)
    netflix_data.drop(columns=["duration"], inplace=True)

def sorting_by_releaseYear():
    global netflix_data
    netflix_data.sort_values(["release_year"], inplace=True)

def organizing_categorical_columns():
    print(f"{"="*35:^35}")
    print(f"{"CATEGORICAL COLUMNS REPORT":^35}")
    print(f"{"="*35:^35}")
    print(f"""Rating of the netflix data: 
{netflix_data["rating"].value_counts()}""")
    print(f"{"-"*35:<10}")

    print(f"""Type of media on netflix data: 
{netflix_data["type"].value_counts()}""")
    print(f"{"-"*35:<10}")

    print(f"""Number of Movies added on netflix per year: 
{netflix_data["year_added"].value_counts()}""")
    print(f"{"-"*35:<10}")

    print(f"""Top 10 countries to produce Movies: 
{netflix_data["primary_country"].value_counts().head(10)}""")
    print(f"{"-"*35:<10}")

    temp_netflix_data = netflix_data.copy()
    temp_netflix_data = temp_netflix_data.explode("listed_in")
    print(f"""Top 10 genres: 
{temp_netflix_data["listed_in"].value_counts().head(10)}""")
    print(f"{"-"*35:<10}")

    print(f"""Top 10 directors: 
{netflix_data["director"].value_counts().drop("Unknown", errors="ignore").head(10)}""")
    print(f"{"-"*35:<10}")

    print(f"""Top 10 Country insights: 
{netflix_data.groupby(["primary_country","type"]).size().drop("Unknown", level="primary_country", errors="ignore").sort_values(ascending=False).head(10).unstack().max(axis=1)}""")
    print(f"{"-"*35:<10}")

    print(f"""Average Release Year per Rating:
{netflix_data.groupby("rating")["release_year"].mean()}""")
    print(f"{"-"*35:<10}")

    temp_netflix_data = netflix_data.copy()
    temp_netflix_data = temp_netflix_data.explode("listed_in")
    print(f"""Top genres of 5 countries: 
{temp_netflix_data.groupby(["primary_country","listed_in"]).size().sort_values(ascending=False).head()}""")
    print(f"{"-"*35:<10}")

    temp_netflix_data = netflix_data.copy()
    temp_netflix_data["mins_duration"] = pd.to_numeric(temp_netflix_data["mins_duration"], errors="coerce")
    print(f"""Runtime trend over time: 
{temp_netflix_data.groupby("release_year")["mins_duration"].mean()}""")
    print(f"{"-"*35:<10}")

def satistical_analysis():
    print(f"{"="*35:^35}")
    print(f"{"STATISTICAL ANALYSIS":^35}")
    print(f"{"="*35:^35}")
    temp_netflix_data = netflix_data.copy()
    temp_netflix_data["mins_duration"] = pd.to_numeric(temp_netflix_data["mins_duration"], errors="coerce")
    runtime_duration = temp_netflix_data[temp_netflix_data["mins_duration"] > -1]

    print(f"Average of a runtime: {np.mean(runtime_duration["mins_duration"]):.2f}")
    print(f"{"-"*35:<10}")
    print(f"Median of a runtime: {np.median(runtime_duration["mins_duration"]):.2f}")
    print(f"{"-"*35:<10}")
    print(f"Standard deviation of a runtime: {np.std(runtime_duration["mins_duration"]):.2f}")
    print(f"{"-"*35:<10}")
    print(f"Percentile of runtime(25, 50, 75, 90): {np.percentile(runtime_duration["mins_duration"], [25,50,75,90])}")
    print(f"{"-"*35:<10}")

    runtime_std = np.std(runtime_duration["mins_duration"])
    runtime_mean = np.mean(runtime_duration["mins_duration"])
    netflix_data["runtime_z_score"] = (runtime_duration["mins_duration"] - runtime_mean) / runtime_std
    outliers = netflix_data[(netflix_data["runtime_z_score"] > 3) | (netflix_data["runtime_z_score"] < -3)]
    print(outliers[["title", "mins_duration", "runtime_z_score"]])
    print(f"{"-"*35:<10}")

    temp_netflix_data = netflix_data.copy()
    temp_netflix_data["seasons_duration"] = pd.to_numeric(temp_netflix_data["seasons_duration"], errors="coerce")
    tvshows_duration = temp_netflix_data[temp_netflix_data["seasons_duration"] > -1]
    seasons_std = np.std(tvshows_duration["seasons_duration"])
    seasons_mean = np.mean(tvshows_duration["seasons_duration"])
    netflix_data["seasons_z_score"] = (tvshows_duration["seasons_duration"] - seasons_mean) / seasons_std
    outliers = netflix_data[(netflix_data["seasons_z_score"] > 3) | (netflix_data["seasons_z_score"] < -3)]
    print(outliers[["title", "seasons_duration", "seasons_z_score"]])
    print(f"{"-"*35:<10}")

    print(f"""correlation between release year and runtime: 
{netflix_data["release_year"].corr(netflix_data["mins_duration"])}""")
    print(f"{"-"*35:<10}")

def categorical_features():
    temp_netflix_data = netflix_data.copy()
    temp_netflix_data["mins_duration"] = pd.to_numeric(temp_netflix_data["mins_duration"], errors="coerce")
    runtime_duration = temp_netflix_data[temp_netflix_data["mins_duration"] > -1]
    netflix_data["runtime_category"] = pd.qcut(runtime_duration["mins_duration"], 3, labels=["Short", "Medium", "Long"])

    temp_netflix_data = netflix_data.copy()
    temp_netflix_data["seasons_duration"] = pd.to_numeric(temp_netflix_data["seasons_duration"], errors="coerce")
    tvshows_duration = temp_netflix_data[temp_netflix_data["seasons_duration"] > -1]
    netflix_data["seasons_category"] = pd.cut(tvshows_duration["seasons_duration"], bins=[0, 3, 6, 9], labels=["Limited Series", "Standard", "Long Running"])


def genres_organizing(listed_in, media, genres_catalog):
    for genre in listed_in:
        if genre in genres_catalog:
             genres_catalog[genre].append(media)
        else:
            genres_catalog[genre] = [media]

        if genre in media_genres:
            media_genres[genre].append(media)
        else:
            media_genres[genre] = [media]

data_cleaning()
data_info()
converting_to_datetime()
data_splitting()
new_columns()
duration_spliting()
sorting_by_releaseYear()

movie_catalog = []
tvShow_catalog = []
media_catalog = []

def object_creation():
    global movie_catalog
    global tvShow_catalog
    global media_catalog
    for show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country, mins_duration, seasons_duration in zip(netflix_data["show_id"], netflix_data["type"], netflix_data["title"], netflix_data["director"], netflix_data["cast"], netflix_data["country"], netflix_data["date_added"], netflix_data["release_year"], netflix_data["rating"], netflix_data["listed_in"], netflix_data["description"], netflix_data["description_list"], netflix_data["month_added"], netflix_data["day_added"], netflix_data["year_added"], netflix_data["years_between_release_and_added"], netflix_data["primary_country"], netflix_data["mins_duration"], netflix_data["seasons_duration"]):
        if mins_duration != -1:
            movie = Movie(show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country, mins_duration)
            movie_catalog.append(movie)
            media_catalog.append(movie)
            genres_organizing(listed_in, movie, movies_genres)
        else:
            tvShow = TVShow(show_id, type_, title, director, cast, country, date_added, release_year, rating, listed_in, description, description_list, month_added, day_added, year_added, years_bw_release_and_added, primary_country, seasons_duration)
            tvShow_catalog.append(tvShow)
            media_catalog.append(tvShow)
            genres_organizing(listed_in, tvShow, tvShow_genres)

object_creation()

def category_check():
    print(f"{"="*35:^35}")
    print(f"{"CATEGORY CHECK":^35}")
    print(f"{"="*35:^35}")
    print(f"Number of Movies: {len(movie_catalog)}")
    print(f"{"-"*35:<10}")
    print(f"Number of TVShows: {len(tvShow_catalog)}")
    print(f"{"-"*35:<10}")

organizing_categorical_columns()
satistical_analysis()
categorical_features()
category_check()

netflix_data.to_csv("netflix_cleaned_final.CSV")
