import json

movies_catalog = {
    "The Shawshank Redemption": {
        "genres": ("Drama", "Crime"),
        "rating": 5.0,
        "review": "An inspiring and emotional masterpiece with unforgettable performances."
    },

    "The Dark Knight": {
        "genres": ("Action", "Crime", "Drama"),
        "rating": 5.0,
        "review": "A thrilling superhero film elevated by an iconic villain."
    },

    "Inception": {
        "genres": ("Sci-Fi", "Action", "Thriller"),
        "rating": 4.9,
        "review": "A brilliant mind-bending story that rewards careful attention."
    },

    "Interstellar": {
        "genres": ("Sci-Fi", "Adventure", "Drama"),
        "rating": 5.0,
        "review": "A breathtaking journey through space filled with emotion and wonder."
    },

    "The Godfather": {
        "genres": ("Crime", "Drama"),
        "rating": 5.0,
        "review": "One of the finest crime dramas ever created."
    },

    "Titanic": {
        "genres": ("Romance", "Drama"),
        "rating": 4.8,
        "review": "A touching love story with spectacular visuals and heartbreaking moments."
    },

    "Toy Story": {
        "genres": ("Animation", "Family", "Adventure"),
        "rating": 4.8,
        "review": "A charming animated classic loved by both kids and adults."
    },

    "Finding Nemo": {
        "genres": ("Animation", "Family", "Comedy"),
        "rating": 4.7,
        "review": "A heartwarming underwater adventure packed with memorable characters."
    },

    "The Conjuring": {
        "genres": ("Horror", "Mystery", "Thriller"),
        "rating": 4.6,
        "review": "Delivers genuine scares with a gripping supernatural story."
    },

    "Parasite": {
        "genres": ("Thriller", "Drama", "Comedy"),
        "rating": 4.9,
        "review": "A clever social commentary that keeps surprising until the end."
    },

    "Avengers: Endgame": {
        "genres": ("Action", "Adventure", "Sci-Fi"),
        "rating": 4.8,
        "review": "An epic conclusion that satisfies years of storytelling."
    },

    "Joker": {
        "genres": ("Drama", "Crime", "Thriller"),
        "rating": 4.7,
        "review": "A powerful character study with an outstanding lead performance."
    },

    "Frozen": {
        "genres": ("Animation", "Family", "Musical"),
        "rating": 4.4,
        "review": "Catchy songs and lovable characters make it enjoyable for families."
    },

    "The Lion King": {
        "genres": ("Animation", "Adventure", "Drama"),
        "rating": 4.9,
        "review": "An emotional coming-of-age tale with timeless music."
    },

    "The Matrix": {
        "genres": ("Sci-Fi", "Action"),
        "rating": 4.9,
        "review": "A groundbreaking science fiction film with revolutionary action."
    },

    "La La Land": {
        "genres": ("Musical", "Romance", "Drama"),
        "rating": 4.6,
        "review": "A visually beautiful musical with bittersweet romance."
    },

    "1917": {
        "genres": ("War", "Drama"),
        "rating": 4.7,
        "review": "An intense war film that feels incredibly immersive."
    },

    "Ford v Ferrari": {
        "genres": ("Sport", "Drama", "Biography"),
        "rating": 4.7,
        "review": "An exciting racing drama driven by excellent performances."
    },

    "Schindler's List": {
        "genres": ("History", "Biography", "Drama"),
        "rating": 5.0,
        "review": "A deeply moving historical film that leaves a lasting impact."
    },

    "The Good, the Bad and the Ugly": {
        "genres": ("Western", "Adventure"),
        "rating": 4.8,
        "review": "A legendary western featuring unforgettable characters and music."
    },

    "The Silence of the Lambs": {
        "genres": ("Crime", "Thriller", "Mystery"),
        "rating": 4.9,
        "review": "An intelligent thriller with unforgettable suspense and brilliant acting."
    },

    "Gladiator": {
        "genres": ("Action", "Drama", "History"),
        "rating": 4.8,
        "review": "An epic historical adventure that delivers powerful emotions."
    },

    "The Notebook": {
        "genres": ("Romance", "Drama"),
        "rating": 4.5,
        "review": "A sweet romantic drama, although its pacing may feel slow to some viewers."
    },

    "Shrek": {
        "genres": ("Animation", "Comedy", "Family"),
        "rating": 4.7,
        "review": "A hilarious animated film with clever humor for every age."
    },

    "Mad Max: Fury Road": {
        "genres": ("Action", "Adventure", "Sci-Fi"),
        "rating": 4.8,
        "review": "A nonstop action spectacle with breathtaking visuals."
    },

    "The Ring": {
        "genres": ("Horror", "Mystery"),
        "rating": 4.3,
        "review": "The atmosphere is creepy, but the ending may not satisfy everyone."
    },

    "The Prestige": {
        "genres": ("Mystery", "Drama", "Sci-Fi"),
        "rating": 4.8,
        "review": "A fascinating mystery filled with clever twists."
    },

    "Pirates of the Caribbean": {
        "genres": ("Adventure", "Fantasy", "Action"),
        "rating": 4.7,
        "review": "An entertaining pirate adventure led by a memorable cast."
    },

    "The Hangover": {
        "genres": ("Comedy", "Adventure", "Crime"),
        "rating": 4.4,
        "review": "Packed with outrageous comedy, though some jokes feel dated."
    },

    "A Quiet Place": {
        "genres": ("Horror", "Drama", "Sci-Fi"),
        "rating": 4.6,
        "review": "Creative storytelling and constant tension make it highly engaging."
    },

    "The Social Network": {
        "genres": ("Biography", "Drama"),
        "rating": 4.7,
        "review": "A sharp and well-written portrayal of ambition and innovation."
    },

    "The Wolf of Wall Street": {
        "genres": ("Biography", "Comedy", "Crime"),
        "rating": 4.7,
        "review": "Wildly entertaining, but its long runtime can feel excessive."
    },

    "The Nun": {
        "genres": ("Horror", "Mystery"),
        "rating": 3.4,
        "review": "The visuals are impressive, but the story lacks originality."
    },

    "Fantastic Beasts": {
        "genres": ("Fantasy", "Adventure", "Family"),
        "rating": 4.1,
        "review": "An enjoyable fantasy adventure, even if it doesn't reach Harry Potter's heights."
    },

    "Up": {
        "genres": ("Animation", "Adventure", "Family"),
        "rating": 4.9,
        "review": "An emotional adventure with one of animation's best openings."
    },

    "Braveheart": {
        "genres": ("History", "War", "Drama"),
        "rating": 4.7,
        "review": "An inspiring historical epic filled with memorable battles."
    },

    "The Emoji Movie": {
        "genres": ("Animation", "Comedy", "Family"),
        "rating": 2.1,
        "review": "The colorful visuals cannot hide the weak storytelling."
    },

    "Cats": {
        "genres": ("Musical", "Fantasy"),
        "rating": 1.8,
        "review": "Strange visual effects and a confusing plot make it difficult to enjoy."
    },

    "Morbius": {
        "genres": ("Action", "Sci-Fi", "Horror"),
        "rating": 2.7,
        "review": "Interesting ideas are overshadowed by an underwhelming script."
    },

    "The Last Airbender": {
        "genres": ("Fantasy", "Adventure", "Action"),
        "rating": 1.9,
        "review": "Despite its source material, the adaptation feels disappointing."
    },

    "The Truman Show": {
        "genres": ("Drama", "Comedy", "Sci-Fi"),
        "rating": 4.8,
        "review": "A thought-provoking story that remains surprisingly relevant today."
    },

    "Whiplash": {
        "genres": ("Drama", "Music"),
        "rating": 4.9,
        "review": "An intense and unforgettable film driven by phenomenal performances."
    },

    "The Grand Budapest Hotel": {
        "genres": ("Comedy", "Adventure", "Crime"),
        "rating": 4.7,
        "review": "Its unique style and witty humor make every scene enjoyable."
    },

    "Knives Out": {
        "genres": ("Mystery", "Comedy", "Crime"),
        "rating": 4.8,
        "review": "A clever detective story filled with entertaining twists."
    },

    "The Revenant": {
        "genres": ("Adventure", "Drama", "Thriller"),
        "rating": 4.7,
        "review": "Stunning cinematography and powerful acting create an unforgettable experience."
    },

    "Zombieland": {
        "genres": ("Comedy", "Horror", "Action"),
        "rating": 4.4,
        "review": "A fun mix of zombie action and comedy that rarely slows down."
    },

    "Train to Busan": {
        "genres": ("Horror", "Action", "Thriller"),
        "rating": 4.8,
        "review": "An emotional zombie thriller packed with suspense."
    },

    "John Wick": {
        "genres": ("Action", "Crime", "Thriller"),
        "rating": 4.7,
        "review": "Stylish action sequences make this an exciting watch."
    },

    "The Imitation Game": {
        "genres": ("Biography", "Drama", "History"),
        "rating": 4.7,
        "review": "A fascinating historical drama about one of computing's greatest minds."
    },

    "Your Name": {
        "genres": ("Animation", "Romance", "Fantasy"),
        "rating": 4.9,
        "review": "Beautiful animation and heartfelt storytelling leave a lasting impression."
    },

    "Weathering With You": {
        "genres": ("Animation", "Fantasy", "Romance"),
        "rating": 4.6,
        "review": "The visuals are gorgeous, though the plot occasionally feels predictable."
    },

    "Mulan": {
        "genres": ("Animation", "Adventure", "Family"),
        "rating": 4.5,
        "review": "An inspiring tale with memorable songs and lovable characters."
    },

    "Free Guy": {
        "genres": ("Action", "Comedy", "Sci-Fi"),
        "rating": 4.3,
        "review": "A fun concept that delivers plenty of laughs and action."
    },

    "Moonfall": {
        "genres": ("Sci-Fi", "Adventure", "Disaster"),
        "rating": 2.8,
        "review": "The visual effects impress, but the story struggles to stay convincing."
    },

    "Green Book": {
        "genres": ("Drama", "Biography", "Comedy"),
        "rating": 4.8,
        "review": "A heartfelt road-trip story featuring outstanding chemistry between its leads."
    },

    "The Room": {
        "genres": ("Drama", "Romance", "Psychological"),
        "rating": 1.6,
        "review": "Poor acting and awkward dialogue make it unintentionally funny."
    },

    "Dragon Ball Super: Broly": {
        "genres": ("Animation", "Action", "Fantasy"),
        "rating": 4.7,
        "review": "Fantastic animation delivers thrilling battles from start to finish."
    },

    "Detective Pikachu": {
        "genres": ("Adventure", "Comedy", "Family"),
        "rating": 4.2,
        "review": "An enjoyable family film with charming Pokémon characters."
    },

    "Resident Evil": {
        "genres": ("Action", "Horror", "Sci-Fi"),
        "rating": 3.8,
        "review": "The action is entertaining, although the plot is fairly average."
    },

    "Pixels": {
        "genres": ("Comedy", "Sci-Fi", "Action"),
        "rating": 2.9,
        "review": "A nostalgic premise is let down by inconsistent humor."
    }

}

genres = [
    "Action",
    "Adventure",
    "Animation",
    "Biography",
    "Comedy",
    "Crime",
    "Disaster",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Horror",
    "Music",
    "Musical",
    "Mystery",
    "Psychological",
    "Romance",
    "Sci-Fi",
    "Sport",
    "Thriller",
    "War",
    "Western"
]

positive_review_words = {
    "good", "great", "excellent", "amazing", "awesome",
    "masterpiece", "inspiring", "emotional", "unforgettable",
    "thrilling", "brilliant", "breathtaking", "touching",
    "charming", "heartwarming", "gripping", "clever",
    "epic", "powerful", "outstanding", "lovable",
    "timeless", "groundbreaking", "beautiful",
    "immersive", "exciting", "intelligent", "memorable",
    "creative", "sharp", "entertaining", "enjoyable",
    "gorgeous", "phenomenal", "thought-provoking",
    "witty", "stunning", "stylish", "fascinating",
    "fun", "suspense", "wonder", "rewarding",
    "engaging", "spectacular"
}

negative_review_words = {
    "bad", "boring", "poor", "weak", "confusing",
    "disappointing", "underwhelming", "lacks", "lack",
    "slow", "dated", "average", "predictable",
    "strange", "awkward", "excessive", "difficult",
    "cannot", "hide", "overshadowed", "struggles",
    "unoriginal", "inconsistent", "convincing",
    "disappoint", "fairly", "let", "down"
}

def movie_review_classification():
    for key,values in movies_catalog.items():
        pos_review = neg_review = False
        for i in values["review"].strip().split():
            for j in positive_review_words:
                if i == j:
                    pos_review = True
                    break
            for k in negative_review_words:
                if i == k:
                    neg_review = True
                    break
        if neg_review == True:
            values.update({"review_classification": "Neg"})
        elif pos_review == True:
            values.update({"review_classification": "Pos"})
        else:
            values.update({"review_classification": "Neutral"})



movie_review_classification()

try:
    with open("movies_catalog.json","w") as file:
        json.dump(movies_catalog,file, indent=4, ensure_ascii=False)
except FileExistsError:
    print("\n")
    print("\"movies_catalog.json\" already exists")
else:
    print("\n")
    print("\"movies_catalog.json\" saved successfully")


try:
    with open("movies_genres.JSON","w") as file:
        json.dump(genres, file, indent=4)
except FileExistsError:
    print("\n")
    print("\"movies_genres.JSON\" already exist")
else:
    print("\n")
    print("\"movies_genres.JSON\" saved successfully")
