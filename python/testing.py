import random as rd
import numpy as np

def computer_choice():
	choice = rd.randint(0,1000)
	if choice in np.arange(0,334): # range one for paper
		return "Paper"
    	#print("range 1", choice)
	elif choice in np.arange(334,667): # range two scissor
		return "Scissor"
    	#print("range 2" , choice)
	elif choice in np.arange(667,1001): # range three for Rock
		return "Rock"
    	#print("range 3", choice)


def compare_me_computer(my_choice):
	my_choice = my_choice
	comp_choice = computer_choice()
	
	if my_choice == computer_choice:
		print("Oooops Please try again!!!")
	else:
		check_winner(my_choice,comp_choice)

def check_winner(my_choice,comp_choice):
	if my_choice == "Rock":
		if comp_choice == "Scissors":
			return "Rocks Win"
		elif comp_choice == "Paper":
			return "Paper Wins"

user_input = input("Please enter 1 for rock, 2 for paper and 3 for scissors: ")

if int(user_input) == 1:
	print("you've chosen Rock")
	compare_me_computer("Rock")
elif int(user_input) == 2:
	print("you've chosen paper")
	compare_me_computer("Paper")
elif int(user_input) ==3:
	print("you've chosen scissors")
	compare_me_computer("Scissors")
else:
	print("please choose a correct number (1, 2 , 3)")
