import random


class NumberGame:
    """
    NumberGame core
    """

    def __init__(self, high_number, player_name):
        self.high_number = high_number
        self.player_name = player_name
        self.com_number = random.randint(1, self.high_number)
        self.play_again = 'n'
        self.guess = None
        self.guess_count = 1

    def start(self):
        """
        Starts the game
        """
        self.play_again = 'n'
        self.guess_count = 0
        self.greeting()
        self.game_loop()

    def generate_num(self):
        self.com_number = random.randint(1, self.high_number)
        self.guess_count = 0

    def greeting(self):
        print('Well {}, I am thinking of a number between 1 and {}.'.format(self.player_name, self.high_number))

    def game_loop(self):
        """
        Loops the game
        """
        # 6 valid guesses allowed
        # Loop in case of invalid input
        while True:
            # Get input and check for valid input
            try:
                self.guess = int(input('Take a guess.\n'))
                if 1 <= self.guess <= self.high_number:
                    break
                else:
                    print('Invalid input.')
            except ValueError:
                print('Invalid input')
        self.guess_count += 1
        # Give user clues
        if self.guess < self.com_number and self.guess_count < 6:
            print('Too low.')
            self.game_loop()
        elif self.guess > self.com_number and self.guess_count < 6:
            print('Too high.')
            self.game_loop()
        elif self.guess == self.com_number:
            self.you_win()
            self.high_number += 20
            self.again()
        else:
            print('Nice try. My number was {}.'.format(self.com_number))
            self.high_number = 20
            self.again()

    def you_win(self):
        print('Way to go {}! You guessed my number in {} guesses.'.format(self.player_name, self.guess_count))

    def again(self):
        """
        Check if they want to play again.
        """
        self.play_again = input('Do you want to play again?\n(y/n)')
        if self.play_again == 'y':
            self.generate_num()
            self.greeting()
            self.game_loop()
        else:
            print('Thanks for playing {}!'.format(self.player_name))
            return

#TODO add scoring system
# def high_score():
#     with open('high_score.txt', 'r') as f:
#         content = []
#         for line in f:
#             content.append(line.strip())
#     scores = content[1:]

def main():
    difficulty = 1
    high_number = 20 * difficulty
    player_name = input('Hello! What is your name?\n')
    game = NumberGame(high_number, player_name)
    game.start()


# Executes code for testing
if __name__ == "__main__":
    main()
