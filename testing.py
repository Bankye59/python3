import random

def math_game():
    print("Welcome to the Math Game!")
    print("You will be asked random math questions. Try to answer as quickly as possible.")
    print("Let's start!\n")
    
    score = 0
    total_questions = 5  # Number of questions to answer
    
    for i in range(total_questions):
        # Generate two random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        # Randomly choose an operation
        operation = random.choice(['+', '-', '*'])
        
        # Create the math question based on the operation
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        
        # Ask the player for an answer
        player_answer = int(input(f"Question {i+1}: What is {num1} {operation} {num2}? "))
        
        # Check the answer and update score
        if player_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
        
        print()  # Print a newline for spacing
    
    print(f"Game Over! You got {score}/{total_questions} correct.")
    if score == total_questions:
        print("Excellent! Perfect score!")
    elif score >= total_questions // 2:
        print("Good job! Keep practicing to get better.")
    else:
        print("Better luck next time! Keep practicing!")
    
# Start the game
math_game()
