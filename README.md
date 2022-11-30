# Hangman Project

### Project for AiCore course.

## Set up

I started by populate a list with some words to use them later on in the guessing of the word during the game:

```
word_list = ["apple", "kiwi", "banana", "watermelon", "strawberry"]
```

## Random pick

After that, i want to use the "random" module to pick a random word inside the list written before.

```
word = random.choice(word_list)
```

In order to doing that, i need to import the module:

```
import random
```

## Input by user

I need now the user to guess the rando word picked from the list. To do that I use the input function and save the value inside the variable "guess".

```
guess = input("Enter a single letter: ")
```

## if statement

At this point, we want to check if the user respected the assignment. Thanks to the first IF we both check if the length of the input is equal to one (single letter) and, at the same time, if the guess is a number or a character(letter).

I use the len() function to discover the input lenght and the isalpha() function to understand if the guess is a number or a character. (isalpha() is equal to True when the parameter is a letter).

```
if len(guess) == 1 and guess.isalpha():
print("Good guess!")
else:
print("Oops! That is not a valid input.")
```

## Adding a Class

We defined the "Hangman" class by defining it with the following code:

```
class Hangman():
```

We can then initialize its attributes with the \_**\_init\_\_** function:

```
    def __init__(self, word_list, num_lives=5):
        self.word_list:list = word_list
        self.num_lives:int = num_lives
        self.word:str = random.choice(self.word_list)
        self.word_guessed:list = ["_" for _ in range(0,len(self.word))]
        self.num_letters:int = len(set(self.word))
        self.list_of_guesses:list = []

```

Inside a class we can also define methods to call as function, such as the following:

```
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
```

and

```
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
```

# Final Consideration

## Logic behind the project

The project follow a logic belonging to the utilization of the class Hangman where you structure all the game. As written before, the class inizialize all the attributes needed for running the game, such as randomly choice a word within a list, handle the number of lives and the number of character missed and so on.

Moreover, in this class are defined two methods that are used to give us the opportunity to input a letter, check if it is inside the word, and return us the result of our choice.

Last, after created the "game" object from Hangman's class, we are able to run the game by using all of this functions and attributes until we either win or loose.
