Python Mini Projects

A collection of small Python projects built to practice and demonstrate core programming concepts — CLI design, file/JSON handling, text processing, and simple recommendation logic.

Each project lives in its own folder with its own script(s) and a short write-up of what it does and how to run it.

Projects
Project	Description	Key Concepts
AI Prompt Cost & Token Estimator (CLI)	Estimates token count and API cost for a given prompt, from the command line.	CLI input handling, string parsing, cost calculation
Build a Learning Chatbot (Rule-Based AI)	A simple rule-based chatbot that matches user input to predefined responses.	Conditional logic, string matching, loops
Habit Tracker & Text Analyzer (CLI)	Tracks daily habits and analyzes logged text entries for patterns.	File I/O, data aggregation, CLI menus
Mini Recommendation Engine (Movies)	Recommends movies based on simple similarity/rating logic.	Data structures, filtering/sorting logic
Movies Recommendation System (v2)	Expanded version of the movie recommender using a JSON movie catalog and genre data.	JSON handling, recommendation logic, modular code
AI Text Corpus Manager & Vocabulary Builder	Builds and manages a text corpus/vocabulary list, useful for social post generation.	Text processing, file management
MindTrack: AI Journal and Mood Insights CLI	A CLI journaling tool that logs entries and surfaces mood insights over time.	CLI design, data persistence, basic analysis

Replace the descriptions above with 1–2 accurate sentences per project once you've reviewed each script — recruiters read this table, not the code.

Skills Demonstrated
Python fundamentals: functions, loops, conditionals, data structures
File I/O and JSON data handling
Command-line interface (CLI) design
Basic recommendation/filtering logic
Text processing and simple NLP-adjacent tasks
How to Run

Each project can be run directly with Python 3:

bash
python3 "project_file_or_folder/script.py"

If a project has external dependencies, install them first:

bash
pip install -r requirements.txt

(Add a requirements.txt inside any project folder that needs one — e.g. if you used pandas, numpy, etc.)

Repository Structure
python-mini-projects/
├── ai-prompt-cost-estimator/
│   └── main.py
├── learning-chatbot/
│   └── main.py
├── habit-tracker/
│   └── main.py
├── movie-recommender-v1/
│   └── main.py
├── movie-recommender-v2/
│   ├── recommendation_system.py
│   ├── save_the_movies_data.py
│   ├── movies_catalog.json
│   └── movies_genres.json
├── text-corpus-manager/
│   └── main.py
├── mindtrack-journal-cli/
│   └── main.py
├── LICENSE
└── README.md

This is the target structure — see the "Next Steps" section below for how to get there from the current flat layout.

About This Repo

This repo is a running log of small Python projects I've built while learning and practicing core programming and problem-solving skills. Each one is intentionally scoped small so I can focus on a specific concept (CLI tools, recommendation logic, text processing, data persistence) and finish it end to end.

License

This repository is licensed under the MIT License.
