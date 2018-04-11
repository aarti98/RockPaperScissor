from random import choice

print("Welcome to the game. Player chooses first!")

#ASK INPUT FROM USER
player= input("Choose (r) for rock, (p) for paper and (s) for scissor \n")
print("You chose " + player + "\n")
 
 #GENERATE COMPUTER'S CHOICE 
computer= choice([1,2,3])


if computer == 1:
	computer = 'r'

elif computer == 2:
	computer = 'p'

else:
	computer = 's'


print("Computer chooses " + str(computer) + "\n")

#COMPARE THE CONDITION
if player == computer:
	print("DRAW!")

elif player == 'r' and computer == 's' or player == 'p' and computer == 'r' or  player == 'p' and computer == 'r':
	print('Player wins!')

else:
	print('Computer wins!')		

