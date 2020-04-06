# Working on it
import random
from sys import exit

username = ""
count = 0
score = 0
guessed = False

def start():
	global username
	global number
	global count
	global score
	global guessed
	
	username = input("Enter player name: ")
	number = random.randint(1, 100)

	count = 0
	score = 0
	guessed = False
	print (number)

	while (count < 5):
		print()
		guess = int(input("Enter your guess: "))
		print()
		count += 1
		if (guess == number): 
			guessed = True
			if count == 1:
				print ("Supercalifragilisticexpialidocious!")
				check_result()
				break
			else:
				print ("Wow! you guessed it right")
				check_result()
				break
			
		elif guess < number:
			print ("You guessed a lesser number.")
			print ("You have %d chances left." % (5 - count))
		
		elif guess > number:
			print ("You guessed a higher number")
			print ("You have %d chances left." % (5 - count))

start()

def check_result():
	if (guessed == True):
		if (count < 3):
			print ("You're amazing at this game", username)
			print ("You took only %d chances to guess it right" % count)
		else:
			print ("You took %d chance to guess it right" % count)
	else:
		print ("Better luck next time", username)
	

print ("Do you want to play again? Y/N")
choice = input("> ")			

if(choice == "Y"):
	start()
else:
	exit(0)
			