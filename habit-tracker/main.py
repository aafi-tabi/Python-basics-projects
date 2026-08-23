logs = []
keywords = ["run", "study", "read", "water", "sleep"]
daily_habit_counts = []
user_entry = "daily"  # dummy value so the while loop runs at least once


def text_refine(text):
    return text.lower().strip().replace(",", "").replace("!", "").split()


while user_entry != ["quit"]:
    count = 0
    print("\n")
    user_entry = input("Enter a today's activities (quit to exit): ")
    user_entry = text_refine(user_entry)

    if user_entry == ["quit"]:
        break
    else:
        logs.append(user_entry)

    found_keywords = []
    for keyword in keywords:
        for word in user_entry:
            if keyword == word:
                found_keywords.append(keyword)
                count += 1

    daily_habit_counts.append(count)

if len(logs) > 0:
    zero_daily_count_habits = daily_habit_counts.count(0)
    most_habits = max(daily_habit_counts)
    most_habits_index = daily_habit_counts.index(most_habits)

    print("\n")

    keywords_count = []
    keyword_total = 0
    for keyword in keywords:
        for entry in logs:
            for word in entry:
                if keyword == word:
                    keyword_total += 1
        keywords_count.append(keyword_total)
        keyword_total = 0

    keyword_count_max = max(keywords_count)
    keywords_count_index = keywords_count.index(keyword_count_max)
    max_appeared_habit = keywords[keywords_count_index]

    print("=" * 15)
    print("Daily Report")
    print("=" * 15)
    print(f"How many days you performed zero matching habits: {zero_daily_count_habits}")
    print(f"The day you performed most matching habits: {most_habits_index + 1}")
    print(f"The number of maximum matching habits: {most_habits}")
    print(f"The activities you logged on day {most_habits_index + 1}: {logs[most_habits_index]}")
    print(f"List of your daily habits count: {sorted(daily_habit_counts)}")
    print(f"Average of your daily habits count: {sum(daily_habit_counts) / len(daily_habit_counts):.2f}")
    print(f"The habit that you performed most: {max_appeared_habit}")
    print(f"How many times did you perform {max_appeared_habit}: {keyword_count_max}")
else:
    print("No report to show")
