import random

class guessGame(object):
    # To show details and instruction for the user
    def show_detail(self): # Welcome notes and requirements of the the game!
        print("Welcome to the guess of fun game!\n - Number should be 4 digits\n - Hints:\n  - 'o' indicates that one digit is correct and is in the right spot\n  - ‘x’ indicates that one digit is correct but in the wrong spot\n  - '-' indicates that one digit is incorrect\n")

    def generate_random_number(self): # Generating random number
        return random.randint(1000, 9999)

    def check_guess(self, secret_number, guess):
        hints = []
        for i in range(4):
            if guess[i] == secret_number[i]: # Placeholder for digits that matched.
                hints.append('o')
            elif guess[i] in secret_number: # Placeholder for digits that are not match.
                hints.append('x')
            else:
                hints.append('_')  # Placeholder for digits that don't match.
        return hints
    
    def play_game(self):
        self.show_detail()
        secret_number = [int(digit) for digit in str(self.generate_random_number())]
        attempts = 1
        while True:
            guess = input("Guess the 4-digit number (Press q to quit): ")
            if guess.lower() == "q": # q to quit the game
                break
            if len(guess) != 4 or not guess.isdigit(): # Validating whether the guess number is 4 digits.
                print("Please enter a valid 4-digit number (Press q to quit):")
                continue
            guess = [int(digit) for digit in guess]
            hints = self.check_guess(secret_number, guess) # Get the hints to the guess function
            print('Hints: ',hints)
            if hints == ['o', 'o', 'o', 'o']: # Responding when user got the number correct.
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                play_again = input("\nDo you want to play again? (y for play again): ").lower()
                if play_again.lower() == "y":
                    self.play_game() # Call the play_game function to let user play the game again.
                else:
                    break
            attempts += 1