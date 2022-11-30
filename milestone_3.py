import random

word_list = ["apple", "kiwi", "banana", "watermelon", "strawberry"]

word = random.choice(word_list)

while True:
    guess = input("Guess a single letter: ")
    if len(guess) == 1 and guess.isdigit() == False:
        break
    else: 
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")