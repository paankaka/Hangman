import random
import time
import os

name = input("What is your name? ")
time.sleep(0.8)
print("Good Luck ! ", name)
words = ['techno', 'india', 'khakkhu', 'programming', 
		'python', 'university', 'gamer', 'TCS', 
		'whiskey', 'fresher', 'NQT'] 
word = random.choice(words)
time.sleep(0.5)
print("Guess the word")
guesses = ''
turns = 6
while turns > 0:
	failed = 0
	for char in word: 
		if char in guesses: 
			print(char)
		else: 
			print("_",end="")
			failed += 1
	if failed == 0:
		print("\nYou Win") 
		print("The word is: ", word) 
		break
	guess = input("guess a character:")
	guesses += guess 
	if guess not in word:
		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')
		if turns == 0:
			print("It looks like your IQ is less than 69.8 percent of the human population, anyways, the word was", word)

