import random


class Hangman():

    def __init__(self, word_list, num_lives=5):
        self.word_list:list = word_list
        self.num_lives:int = num_lives
        self.word:str = random.choice(self.word_list)
        self.word_guessed:list = ["_" for _ in range(0,len(self.word))]
        self.num_letters:int = len(set(self.word))
        self.list_of_guesses:list = []
