import random
MyNum = random.randint(1,1000)

print("I'm thinking if a number between 1 and 1000. Enter your guess!")
guesses = 0
guess = int(raw_input())

while guess != MyNum:
	if guess > MyNum:
		print("Nope, too high. Try again!")
		guess = int(raw_input())
		guesses = guesses + 1
	if guess < MyNum:
		print("Nope, too low. Try again!")
		guess = int(raw_input())
		guesses = guesses + 1
	if guess == MyNum:
		print("Hooray, you won! You took " + str(guesses) + " amount of guesses.")
		
