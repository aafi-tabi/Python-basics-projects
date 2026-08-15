budget = None
prompt_history = []
cost_history = []
choice  = 1 
models = {1:200,
          2:500}
model_choice = None
def main_menu():
    print("*" * 18) 
    print("Choose from the menu")
    print("*" * 18) 
    print("1 - Estimate a prompt cost")
    print("2 - View a prompt history")
    print("3 - Show remaining budget")
    print("4 - Exit")

def sub_menu():
    print("*" * 25) 
    print("Which model do you want to use?")
    print("*" * 25) 
    print(f"1 - Basic -> Price: $200 per {1000:,} tokens")
    print(f"2 - Pro -> Price: $500 per {1000:,} tokens")
    print("3 - Exit")

def get_budget():
    global budget
    while True:
        budget = input("Enter your budget (in $): ")
        try:
            budget = float(budget)
            break
        except ValueError:
            print("Try again")

def get_valid_input():
    while True:
        choice = input("Enter a choice: ")

        if choice.isdigit():
            choice = int(choice)
            return choice
        else:
            print("You did not enter a valid digit")
            
def calculate_cost(model_choice,prompt):
    token_count = len(prompt)/4
    per_token_cost = models[model_choice]/1000
    used_tokens_cost = token_count  * per_token_cost
    return used_tokens_cost,token_count

def token_budget(used_tokens_cost,token_count):
    global budget
    if used_tokens_cost > budget:
            print("Your budget is low")
            print("\n")
    else:
        budget -= used_tokens_cost
        prompt_history.append(prompt)
        cost_history.append(used_tokens_cost)
        print(f"{"*" * 20:^10}")
        print(f"{"Receipt":^10}")
        print(f"{"*" * 20:^10}")
        print(f"Tokens used: {token_count:<10.2f}")
        print(f"Tokens used cost: {used_tokens_cost:<10.2f}")
        print(f"{"-" * 10:^10}")

        
def prompt_model_cost_estimation(model_choice,prompt):
    used_tokens_cost,token_count = calculate_cost(model_choice,prompt)
    print("\n")
    token_budget(used_tokens_cost,token_count)

def prompt_history_with_cost():
    if len(prompt_history) > 0:
        print(f"{"history":>30} - {"cost":<10}")
        for history,cost in zip(prompt_history, cost_history):
            print(f"{history:>30} - {cost:<10.2f}")
        print("\n")
    else:
        print("Your prompt history is empty")

def prompt_budget():
    print(f"{"-" * 15:^10}")
    print(f"Budget: {budget:^10.2f}")
    print(f"{"-" * 15:^10}")
      
print("\n")
get_budget()
print("\n")

while choice != 0:
    model_choice = 1
    main_menu()
    print("\n")
    choice = get_valid_input()
    print("\n")
    
    if choice == 1: 
        while True:   
            prompt = input("Enter a prompt: ").lower()

            if len(prompt) > 0:
                break
            else:
                print("Try again")
        print("\n")

        while model_choice != 0:
            sub_menu()
            print("\n")
            model_choice = get_valid_input()
            print("\n")

            if model_choice == 1:
                prompt_model_cost_estimation(1,prompt)
                print("\n")

            elif model_choice == 2:
                prompt_model_cost_estimation(2,prompt)
                print("\n")

            elif model_choice == 3:
                print("Exit successfully")
                print("\n")
                break

            else:
                print("Try again")
                print("\n")
                model_choice = 1

    elif choice == 2:
        prompt_history_with_cost()
        print("\n")

    elif choice == 3:
        prompt_budget()
        print("\n")

    elif choice == 4:
        print("Good Bye")
        print("\n")
        break

    else: 
        print("You have entered a wrong choice")
        print("Try again")
        print("\n")
        choice = 1
        