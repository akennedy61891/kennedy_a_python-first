# import the random package so that we can generate random numbers
from random import randint

#choices is an array => a container that can hold multiple items  
choices = ["Rock", "Paper", "Scissors",]

#make a computer choose a weapon
computer_choice = choices[randint(0,2)]

#set lives for computer and player
player_life = 3
computer_life = 3

player = False

#set up our loop 
while player is False:
	#set player to True by making a selection
	print("===============================")
	print("Your lives:", player_life, "/3")
	print("Computer lives:", computer_life, "/3")
	print("===============================")
	print("Choose your Weapon!")
	player = input("Rock, Paper or Scissors?\n")

#quit game
	if player == "quit":
		exit()

#choices of player and computer
	print("Player chooses:", player)
	print("computer chooses: ", computer_choice)

#set the restart command
	if player == "restart":
		player_life = 3
		computer_life = 3
		player = False
		computer_choice = choices [randint(0,2)]

#check for a tie = choices are the same
	if player == computer_choice:
		print("Tie! You live to shoot another day")
		
	#check to see if the computer choice beats our choice or not
	elif player == "Rock":
		if computer_choice == "Scissors":
			computer_life = computer_life -1
			print("You Won! Do a happy dance!")

		else:
			player_life = player_life -1
			print("You Lose!", player, "covers", computer_choice)

	elif player == "Paper":
		if computer_choice == "Scissors":
			player_life = player_life -1
			print ("You Lose!", computer_choice, "cut", player)
		else:
			computer_life = computer_life -1
			print("You won!", player, "covers", computer_choice)

	elif player == "Scissors": 
		if computer_choice == "Paper":
			computer_life = computer_life -1
			print ("You Win!", player, "cuts", computer_choice)
		else:
			player_life = player_life -1
			print ("You Lose!", computer_choice, "smashes", player)
	elif player == "quit":
		exit()
	else:
		print("Check your spelling... that's not a valid choice\n")

	#check for win or lose

	#reset the game loop and start over again

	player = False
	computer_choice = choices[randint(0,2)]

	if player_life == 0:
		print()
		print("Your lives: ", player_life)
		print("Computer lives: ", computer_life)
		print("Too bad, so sad! You lose!")
		player = input("restart or quit?\n")
		if player == "quit":
			exit()
		else: 
			print("Check your spelling...")
		player = False
		computer_choice = choices[randint(0,2)]


	if computer_life == 0:
		print()
		print("Your lives: ", player_life)
		print("Computer lives: ", computer_life)
		print("Fantastic! you beat the game!")
		player = input("restart or quit?\n")
		if player == "quit":
			exit()
		else: 
			print("Check your spelling...")
	player = False
	computer_choice = choices[randint(0,2)]
