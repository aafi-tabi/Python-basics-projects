# Python Mini Projects

A portfolio of Python applications built from the ground up — spanning CLI tools, rule-based AI, data-driven recommendation systems, and full applications with authentication and persistence. Each project focuses on solving a concrete problem with clean logic and thoughtful design.

## Featured Projects

### 🧠 MindTrack — AI Journal & Mood Insights CLI
A multi-user journaling application with account creation, secure login, and personalized mood tracking. Journal entries are automatically scored for mood using a custom text-analysis engine, with full history, search, sorting, and a personal profile dashboard.

**Highlights:** Object-oriented design, custom exception handling, user authentication, JSON-backed data persistence, CRUD functionality.

[View Project →](./MindTrack%20AI%20Journal%20and%20Mood%20Insights%20CLI)

### 📊 AI Text Corpus Manager & Vocabulary Builder
A social-media text analysis pipeline that processes posts in real time — detecting hashtags, mentions, and emojis, classifying sentiment, and identifying topics through keyword and bigram analysis. Builds a full word-frequency corpus and exports structured data to multiple formats.

**Highlights:** Tokenization, rule-based NLP, sentiment classification, bigram analysis, multi-format data export (JSON/CSV).

[View Project →](./AI%20Text%20Corpus%20Manager%20%26%20Vocabulary%20Builder-Social%20Posts)

### 🎬 Movies Recommendation System (v2)
A recommendation engine built on a curated catalog of nearly 60 films, complete with genre tagging, ratings, and auto-classified reviews. Offers genre-based recommendations, search, live rating/review updates, and detailed usage analytics — all through a polished menu-driven interface.

**Highlights:** Data modeling, ranking algorithms, sentiment classification, interactive CLI design.

[View Project →](./movies%20recommendation%20system(v2))

## Additional Projects

| Project | Description | Key Concepts |
|---|---|---|
| [Mini Recommendation Engine (Movies)](./Mini%20Recommendation%20Engine%20(Movies).py) | A genre-based movie recommender with login/signup and an interactive accept/reject recommendation flow. | Data structures, filtering & ranking logic |
| [Learning Chatbot (Rule-Based AI)](./Build%20a%20Learning%20Chatbot%20(Rule-Based%20AI).py) | A chatbot that starts with a small knowledge base and grows it dynamically as users teach it new topics during conversation. | Conditional logic, adaptive session state |
| [AI Prompt Cost & Token Estimator](./AI%20Prompt%20Cost%20%26%20Token%20Estimator%20(CLI).py) | A budgeting tool that estimates token usage and API cost per prompt, with full usage history and receipts. | CLI design, cost modeling |
| [Habit Tracker & Text Analyzer](./Habit%20Tracker%20%26%20Text%20Analyzer%20(CLI).py) | Logs daily activity and analyzes entries against tracked habits, generating personalized frequency reports. | File I/O, data aggregation |

## Skills Demonstrated

- **Object-Oriented Programming** — classes, encapsulation, custom exceptions
- **Data Persistence** — JSON and CSV as lightweight data stores, structured read/write pipelines
- **Text Processing & NLP Fundamentals** — tokenization, sentiment classification, keyword and bigram-based topic detection
- **Application Design** — multi-file architecture, authentication flows, menu-driven CLI systems
- **Problem Solving** — translating real-world use cases (journaling, recommendations, social analytics) into working software

## Getting Started

Each project can be run directly with Python 3. Multi-file projects should be run from within their own directory:

```bash
cd "movies recommendation system(v2)"
python3 save_the_movies_data.py
python3 recommendation_system.py
```

Single-file projects run directly:

```bash
python3 "AI Prompt Cost & Token Estimator (CLI).py"
```

Some projects use the `emoji` package:
```bash
pip install emoji
```

## About

This repository reflects my ongoing practice in Python development — moving from focused CLI tools toward more complete applications involving authentication, data persistence, and lightweight natural language processing. Each project was built independently, with an emphasis on clean structure and practical functionality.

## License

This repository is licensed under the [MIT License](./LICENSE).
