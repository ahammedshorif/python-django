# Number Guessing Game with Constraints

# Import the random module to generate a random number
import random

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)

# Define the maximum number of attempts
max_attempts = 7

# Print introduction to the game
print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess correctly. Good luck!\n")

# Start the for loop to manage the 7 attempts
for attempt in range(1, max_attempts + 1):
    # Get the user's guess and convert it to an integer
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    # Check if the guess is out of the valid range (1-100)
    if guess < 1 or guess > 100:
        print("Invalid guess! Please enter a number between 1 and 100.")
        # Skip this attempt and move to the next iteration using continue
        continue

    # Compare the guessed number with the correct one
    if guess == correct_number:
        # If guessed correctly, show success message and exit the loop
        print(f"Congratulations! You've guessed the correct number {correct_number} in {attempt} attempts!")
        break
    elif guess < correct_number:
        # Feedback if the guess is too low
        print("Too low! Try again.")
    else:
        # Feedback if the guess is too high
        print("Too high! Try again.")

# After the loop, check if the player didn't guess the correct number in 7 attempts
else:
    # If loop ends without a correct guess, display the correct number
    print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {correct_number}.")
