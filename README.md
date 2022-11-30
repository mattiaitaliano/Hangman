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

I use the len() function to discover the input lenght and the isdigit() function to understand if the guess is a number or a character. (isdigit() is equal to True when the parameter is a number).

```
if len(guess) == 1 and guess.isdigit() == False:
print("Good guess!")
else:
print("Oops! That is not a valid input.")
```
