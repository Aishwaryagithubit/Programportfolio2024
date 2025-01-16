import json
import random

try:
    # Load data from file
    with open("info.json", "r") as f:
        data = json.load(f)
    # Load default responses from file
    with open("responses.txt", "r") as file:
        random_responses = [line.strip() for line in file.readlines()]
    # Store conversation record
    record = open("recordlog.txt", 'a')

except Exception:
    print(f"Sorry, an error occurred: {Exception}")

# Function to handle chatbot interaction
def chat():
    print("Welcome to the University Chatbot System")
    # Ask user to enter their name and greet
    user = input("Please enter your name: ").strip()
    print(f"Hello {user}, how can I help you?")
     
    # List of available agents 
    agents = ["Nil", "Siya", "Niva", "Max", "Ram", "Mimi", "Isha"]
    agent = random.choice(agents)

    def select_agent(current_agent):
        print(f"I am your agent {current_agent}. Nice to meet you.")
        while True:
            # Ask if user wants to switch agents
            change_agent = input("Do you like to switch agent? (y for yes or n for no): ").strip().lower()
            if change_agent == "y":
                # Ask user to enter new agent
                new_agent = input("Choose an agent (Nil, Siya, Niva, Max, Ram, Mimi, Isha): ").strip()
                if new_agent in agents and new_agent != current_agent:
                    return new_agent
                print("Invalid choice!! Please select a different valid agent.")
            elif change_agent == "n":
                return current_agent
            print("Enter 'y' or 'n'.")

    # Selected agent after user decision
    agent = select_agent(agent)
    if record:
        record.write(f"This conversation started with {user}.\n")
        record.write(f"Agent: {agent}\n")

    while True:
        # Prompt user to ask
        user_ask = input(f"{user}, How can I help you?: ").strip()
        # Stop conversation if user asks to end
        if user_ask.lower() in ["exit", "bye", "quit", "end", "finish"]:
            print(f"Thank you {user}, Have a great day.")
            if record:
                record.write(f"This conversation ended with {user}.\n")
            break
        
        # Search for matching keyword in data and select a response
        response = ""
        for keyword, responses in data.items():
            if keyword.lower() in user_ask.lower():
                response = random.choice(responses)
                break
        
        # If no response is found, choose a random response from default responses
        if not response:
            response = random.choice(random_responses)

        # If response is still not set, ask the user to provide one
        if response == random.choice(random_responses):
            print("I'm not sure how to respond to that.")
            add_response = input("Would you like to add a suitable response? (y/n): ").strip().lower()
            if add_response == 'y':
                user_response = input("Please provide the correct response: ").strip()
                keyword = user_ask.lower()

                # Add new entry to data
                if keyword in data:
                    data[keyword].append(user_response)
                else:
                    data[keyword] = [user_response]

                # Update the JSON file
                with open("info.json", 'w') as f:
                    json.dump(data, f, indent=4)

                print("Thank you! I've added that response.")
                response = user_response
            else:
                response = random.choice(random_responses)
        print(response)
        if record:
            record.write(f"{user}: {user_ask}\n")
            record.write(f"{agent}: {response}\n")

    # Close log file when conversation ends
    record.close()
# Call function
chat()
