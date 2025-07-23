# --- QUIZ GAME FUNCTION ---

# Importing the random library for shuffling options and randomness
import random

# Display a welcome message
def welcome_message(name):
    print("\n--- Quiz Game ---")
    return f"\nWelcome to the Quiz Game, {name}! Let's test your knowledge!"

# Ask a question and chek the user's answer
def ask_question(question_data):
    # Split the questions data into parts
    parts = question_data.split("|")
    question = parts[0]
    options = parts[1].split(",")
    correct_answer = parts[2]
    category = parts[3]

    # Shuffle the answer options
    random.shuffle(options)

    # Disply category and question
    print("\nCategory:", category)
    print(question)

    # Display options
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user answer
    while True:
        # Convert input to an integer and check if it's a valid answer
        try:
            answer = int(input("Enter your answer number (1-4): "))
            if answer in range(1, 5):
                selected_option = options[answer - 1]
                #Check if selected answer is correct
                if selected_option == correct_answer:
                    print("Correct!")
                    return True
                else:
                    print(f"Incorrect! The correct answer was: {correct_answer}")
                    return False
            else:
                print("Invalid input! Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# Show final message
def farewell_message(name, score, counter):
    return f"Thanks for playing, {name}! You scored {score} out of {counter}. Well done!"

# Quiz game manager
def quiz_game(name):
    question_bank = [
        "What is the capital of France?|Paris,London,Berlin,Madrid|Paris|Geography",
        "Who won the FIFA World Cup in 2018?|Germany,Argentina,France,Brazil|France|Sports",
        "What is the largest planet in our solar system?|Earth,Jupiter,Saturn,Venus|Jupiter|Science"
    ]
    #Shuffle the questions
    random.shuffle(question_bank)

    print(welcome_message(name))

    score = 0
    counter = 0
    # Disply each question
    for question_data in question_bank:
        counter += 1
        if ask_question(question_data):
            score += 1
    #Disply final score
    print(farewell_message(name, score, counter))


# --- BMI CALCULATOR FUNCTION ---

#Calculate and disply BMI
def bmi_calculator(name):
    print("\n--- BMI Calculator ---")
    print(f"Let's start, {name}!")
    
    # Ask the user for measurment units
    units = input("Choose units: 1 = Metric, 2 = Imperial: ")
    
    try:
        # For metric calculation
        if units == "1":
            weight = float(input("Enter weight in kilograms: "))
            height = float(input("Enter height in meters: "))
            bmi = weight / (height ** 2)
        # For imperial calculation
        elif units == "2":
            weight = float(input("Enter weight in pounds: "))
            height = float(input("Enter height in inches: "))
            bmi = (weight * 703) / (height ** 2)
        else:
            print("Invalid input. Enter option 1 or 2.")
            return
        # determine categories
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        # Round the result to 1 decimal after a comma
        bmi = round(bmi, 1)
        # Disply the result
        print(f"{name}, your BMI is {bmi}. You are {category}.")
    except ValueError:
        print("Please enter numbers only.")


# Get the user's choice between Quiz game and BMI calculator
def get_user_choice():
    print("What would you like to do?")
    print("1. Play the Quiz Game")
    print("2. Use the BMI Calculator")
    choice = input("Enter 1 or 2: ")
    return choice
    
        
# Ask the user if the user wants to continue            
def ask_to_continue():
    while True:
        continue_or_not = input("\nDo you want to do something else? (Y/N): ").strip().upper()
        if continue_or_not == "Y":
            return True
        elif continue_or_not == "N":
            print("Goodbye!")
            return False     
        else:
            print("Invalid input. Please enter Y- if you wish to continue, N - don't.")
            
# --- MAIN FUNCTION ---  
def main():
    name = input("Enter your name: ")
    print(f"\nHi, {name}!")
# Loop throught the menu until the user decides to stop
    while True:
        choice = get_user_choice()
        
        if choice == "1":
            quiz_game(name) # Call the quiz_game function
        elif choice == "2":
            bmi_calculator(name) # all the bmi_calculator function
        else:
            print("Invalid choice.")

        if not ask_to_continue():
            break
main()

