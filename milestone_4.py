import random


class Hangman():

    def __init__(self, word_list, num_lives=5):
        self.word_list:list = word_list
        self.num_lives:int = num_lives
        self.word:str = random.choice(self.word_list)
        self.word_guessed:list = ["_" for _ in range(0,len(self.word))]
        self.num_letters:int = len(set(self.word))
        self.list_of_guesses:list = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if guess == self.word[i].lower():
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        while True:
            guess = input("Guess a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
        


test = Hangman(["Banana", "Strawberry", "Apple"])

test.ask_for_input()