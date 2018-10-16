# import the random package so that we can generate random numbers
from random import randint

#choices is an array => a container that can hold multiple items 
# arrays are 0-based -> the first item is 0, the second is 1, etc. 
choices = ["Rock", "Paper", "Scissors", "Spock", "fire"]

#make the computer choose an array randomly 

computer_choice = choices [randint (0,4)]

print("Computer chooses: ", computer_choice)