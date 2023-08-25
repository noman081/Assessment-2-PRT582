
import random

class guessGame(object):
    # To show details and instruction for the user
    def show_detail(self):
        print('Welcome to the game of Noman')

    def generate_random_number(self):
        return random.randint(1000, 9999)

    def check_guess(self, secret_number, guess):
        hints = []
        for i in range(4):
            if guess[i] == secret_number[i]:
                hints.append('o')
            elif guess[i] in secret_number:
                hints.append('x')
            else:
                hints.append('_')  # Placeholder for digits that don't match
        print(type(secret_number), type(guess), type(hints))
        return hints
    
    def play_game(self):
        self.show_detail()
        secret_number = [int(digit) for digit in str(self.generate_random_number())]
        print(secret_number)
        attempts = 1
        while True:
            guess = input("Guess the 4-digit number:Press q to quit ")
            if guess.lower() == "q":
                break
            if len(guess) != 4 or not guess.isdigit():
                print("Please enter a valid 4-digit number (Press q to quit).")
                continue
            guess = [int(digit) for digit in guess]
            hints = self.check_guess(secret_number, guess)
            if hints == ['o', 'o', 'o', 'o']:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                play_again = input("Do you want to play again? (y for play again): ").lower()
                if play_again.lower() == "y":
                    self.play_game()
                else:
                    break
            attempts += 1