bot_knowledge = [["goal", "ai"], ["weather", "spring"], ["hobby", "art"], ["food", "pasta"], ["education", "bs software engineering"]]

conversation_history = []
message_counter = 0
prompt = None
not_understood = 0
before_length_of_bot_knowledge = len(bot_knowledge)

bot_knowledge_topic = None
bot_knowledge_answer = None
command_found = False
command_understand = False

print("\n")
print("WELCOME")
conversation_history.append(("WELCOME".lower().strip().replace("!","").replace(":","").split()))

conversation_history.append(("Enter your name: ".lower().strip().replace("!","").replace(":","").split()))

name = input("Enter your name: ").lower().strip().replace(",","").replace("!","").split()
conversation_history.append(name)

print("\n")
print(f"Hi {" ".join(name).title()}, Nice to meet you")
conversation_history.append(f"Hi {" ".join(name).title()}, Nice to meet you".lower().strip().replace("!","").replace(":","").split())

message_counter += 3

while prompt != ["quit"] and prompt != ["exit"]:

    prompt = input("What's on your mind! ").lower().strip().replace(",","").split()
    conversation_history.append("What's on your mind! ".lower().strip().replace(":","").split())
    conversation_history.append(prompt)

    message_counter += 2
    not_found = 0

    if prompt != ["quit"] and prompt != ["exit"]:
        for i in prompt:
            if  i == "!":
                command_found = True
                break
            
        if command_found == True:
            for j in prompt:
                if j == "full" or j == "conversation":
                    print("=" * 15)
                    print("YOUR CONVERSATION HISTORY")
                    print("=" * 15)
                    message_counter += 3
                    for k in conversation_history:
                        print(" ".join(k))
                        message_counter += 1
                    print("---")
                    print("Full conversation history has been ended")
                    print("\n")
                    command_understand = True
                    break

            for j in prompt:
                if j == "last" or j == "few" or j == "exchanges":
                    print("=" * 15)
                    print("LAST FEW CONVERSATIONS")
                    print("=" * 15)
                    conversation_history.append(f"{"=" * 15}".lower().strip().replace("!","").replace(":","").split())
                    conversation_history.append("LAST FEW CONVERSATIONS".lower().strip().replace("!","").replace(":","").split())
                    conversation_history.append(f"{"=" * 15}".lower().strip().replace("!","").replace(":","").split())
                    message_counter += 3
                    for i in conversation_history[-7:]:
                        print(" ".join(i))
                        message_counter += 1
                    print("These were your few last conversations")
                    print("\n")
                    command_understand = True
                    break

            for j in prompt:
                if j == "current" or j == "size" or j == "bot's" or  j == "knowledge":
                    print("=" * 15)
                    print(f"SIZE OF BOT KNOWLEDGE: {len(bot_knowledge)}")
                    print("=" * 15)
                    conversation_history.append(f"{"=" * 15}".lower().strip().replace("!","").replace(":","").split())
                    conversation_history.append(f"SIZE OF BOT KNOWLEDGE: {len(bot_knowledge)}".lower().strip().replace("!","").replace(":","").split())
                    conversation_history.append(f"{"=" * 15}".lower().strip().replace("!","").replace(":","").split())
                    print("\n")
                    message_counter += 3
                    command_understand = True
                    break

            for j in prompt:
                if j == "longest" or j == "message":
                    sorted_conversation_histroy = sorted(conversation_history)
                    print("=" * 15)
                    print(f"LONGEST CONVERSATION: {" ".join(sorted_conversation_histroy[-1]).title()}")
                    print("=" * 15)
                    conversation_history.append(f"{"=" * 15}".lower().strip().replace("!","").replace(":","").split())
                    conversation_history.append(f"LONGEST CONVERSATION: {" ".join(sorted_conversation_histroy[-1]).title()}".lower().strip().replace("!","").replace(":","").split())
                    conversation_history.append(f"{"=" * 15}".lower().strip().replace("!","").replace(":","").split())
                    print("\n")
                    message_counter += 3
                    command_understand = True
                    
                    break
            

            if command_understand == False:
                conversation_history.append("I did not understand".lower().strip().replace("!","").replace(":","").split())
                conversation_history.append("Try again".lower().strip().replace("!","").replace(":","").split())                            
                print("I did not understand")
                print("Try again")
                print("\n")
                not_understood += 1 
                message_counter += 2

            command_found = False
            command_understand = False
        
        else:
            if command_found == False:
                for i in bot_knowledge:
                    for j in i[0:1]:
                        for k in prompt:
                            if j == k:
                                print(f"Yes! {i[0]} is {i[1]}".title())
                                print("\n")
                                message_counter += 1
                                conversation_history.append(f"Yes! {i[0]} is {i[1]}".lower().strip().replace("!","").replace(":","").split())
                                not_found = 1
                                break
                        if(not_found == 1):
                            break
                    if(not_found == 1):
                        break

            if not_found == 0:
                print("I did not understand")
                conversation_history.append("I did not understand".lower().strip().replace("!","").replace(":","").split())
                message_counter += 1
                not_understood += 1

                teach_bot = input("Do you want to teach the bot about this topic (y/n): ").lower().strip().replace(",","").replace("!","").split()
                conversation_history.append("Do you want to teach the bot about this topic (y/n): ".lower().strip().replace("!","").replace(":","").split())
                conversation_history.append(teach_bot)
                message_counter += 2
                print("\n")

                bot_knowledge_topic = []
                bot_knowledge_answer = []

                if teach_bot == ["y"]:

                    while len(bot_knowledge_topic) != 1:

                        bot_knowledge_topic = input("Enter a topic to teach a bot in one word: ").lower().strip().replace(",","").replace("!","").split()
                        conversation_history.append("Enter a topic to teach a bot in one word: ".lower().strip().replace("!","").replace(":","").split())
                        conversation_history.append(bot_knowledge_topic)
                        message_counter += 2

                        if len(bot_knowledge_topic) != 1:
                            if len(bot_knowledge_topic) > 1:
                                print("Length of the words exceeded.")
                                conversation_history.append("Length of the words exceeded.".lower().strip().replace("!","").replace(":","").split())
                                message_counter += 1
                                print("\n")
                            else:
                                print("Length of a words are low")
                                conversation_history.append("Length of a words are low".lower().strip().replace("!","").replace(":","").split())
                                message_counter += 1
                                print("\n")
                    

                    while len(bot_knowledge_answer) != 1:
                    
                        bot_knowledge_answer = input(f"Tell me about {bot_knowledge_topic[0]}? ").lower().strip().replace(",","").replace("!","").split()
                        conversation_history.append(f"Tell me about {bot_knowledge_topic[0]}? ".lower().strip().replace("!","").replace(":","").split())
                        conversation_history.append(bot_knowledge_answer)
                        message_counter += 2

                        if len(bot_knowledge_answer) != 1:
                            if len(bot_knowledge_answer) > 1:
                                print("Length of the words exceeded.")
                                conversation_history.append("Length of the words exceeded.".lower().strip().replace("!","").replace(":","").split())
                                message_counter += 1
                                print("\n")
                            else:
                                print("Length of a words are low")
                                conversation_history.append("Length of a words are low".lower().strip().replace("!","").replace(":","").split())
                                message_counter += 1
                                print("\n")

                    print("New data has been stored in the bot's knowledge")
                    print("\n")
                

                    teach_bot_knowledge = ["".join(bot_knowledge_topic), "".join(bot_knowledge_answer)]
                    bot_knowledge.append(teach_bot_knowledge)


understood_messages = message_counter - not_understood
performance_score = (understood_messages * 100)/message_counter
after_length_of_bot_knowledge = len(bot_knowledge)
improve_in_length_of_bot = after_length_of_bot_knowledge - before_length_of_bot_knowledge
bot_knowledge_growth = (improve_in_length_of_bot * 100)/after_length_of_bot_knowledge
before_length_of_bot_knowledge = after_length_of_bot_knowledge


print("\n")
print("=" * 8)
print("Report")
print("=" * 8)
print(f"Total messages exchange: {message_counter}")
print(f"Total number of messages that bot did not understood: {not_understood}")
print(f"Performance Score of the bot: {performance_score:.2f}")
if performance_score > 70:
    print("performance judgment: Good")
elif performance_score > 45:
    print("performance judgment: Need improvement")
else:
    print("performance judgment: Very bad")
print(f"Bot's knowledge growth: {bot_knowledge_growth:.2f}")
print("\n")
print("-" * 12)
print("Final knowledge base:")
print("-" * 12)
for index,knowledge in bot_knowledge:
    print(f"{index}, {knowledge}")
print("-" * 7)
print("\n")
