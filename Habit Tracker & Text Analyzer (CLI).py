each_word_entry = []
logs = []
keywords = ["run", "study", "read", "water", "sleep"]
daily_habit_counts = []
found_keyword_text = None

user_entry = "daily"

def text_refine(text):
    return text.lower().strip().replace(",","").replace("!","").split()

def count_matched():
    found_keywords = []
    for i in keywords:
        for j in user_entry:
            if(i == j):
                found_keywords.append(i)
                count += 1
    
    daily_habit_counts.append(count)
    found_keyword_text = ",".join(found_keywords)


while user_entry != ["quit"]:

    count  = 0
    print("\n")

    user_entry = input("Enter a today's activities(quit to exit): ")
    user_entry = text_refine(user_entry)

    if user_entry == ["quit"]:
        break
    else:
        logs.append(user_entry)
        
    for i in user_entry:
        each_word_entry.append(i)

    found_keywords = []
    for i in keywords:
        for j in user_entry:
            if(i == j):
                found_keywords.append(i)
                count += 1

    daily_habit_counts.append(count)
    found_keyword_text = ",".join(found_keywords)

    daily_matched_habits = "Habits found: " + found_keyword_text

if len(logs) > 0:

    zero_daily_count_habits = daily_habit_counts.count(0)

    most_habits = max(daily_habit_counts)
    most_habits_index = daily_habit_counts.index(most_habits)

    print("\n")

    keywords_count = []

    keyword_total = 0

    for i in keywords:
        for j in logs:
            for k in j:
                if i == k:
                    keyword_total += 1

        keywords_count.append(keyword_total)
        keyword_total = 0

    keyword_count_max = max(keywords_count)
    keywords_count_index = keywords_count.index(keyword_count_max)
    max_appeared_habit = keywords[keywords_count_index]



    print("=" * 15)
    print("Daily Report")
    print("=" * 15)
    print(f"How many days you performed zero matching hobbies: {zero_daily_count_habits}")
    print(f"The day you perform most matching habits: {most_habits_index + 1}")
    print(f"The number of maximum matching habits: {most_habits}")
    print(f"The following matching habits you perform on {most_habits_index + 1} day: {logs[most_habits_index]}")
    print(f"List of you daily habits count: {sorted(daily_habit_counts)}")
    print(f"Average of your daily habits count: {sum(daily_habit_counts)/len(daily_habit_counts):.2f}")
    print(f"the habits that you performed most: {max_appeared_habit}")
    print(f"How many times did you performed the {max_appeared_habit}: {keyword_count_max}")

else:
    print("No report to show")
    