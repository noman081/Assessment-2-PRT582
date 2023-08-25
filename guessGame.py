import random

class guessGame(object):
    # To show details and instruction for the user
    def show_detail(self):
        print('Welcome to the game of Noman')

    def generate_random_number(self):
        return random.randint(1000, 9999)

    
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