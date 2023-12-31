import random

word_list = ['Apple']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.get_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = self.count_unique_letters()
        self.list_of_guesses = []

    def get_random_word(self):
        return random.choice(self.word_list)

    def count_unique_letters(self):
        return len(set(self.word))
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] in guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You Lost! 0 Lives Left')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('You won the game!')
            break

play_game(word_list)




              




