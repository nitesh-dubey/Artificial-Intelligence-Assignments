from gos_utils import *
from random import randint
import math
MAXNUM = 10**6



n_sticks = int(input("\n Enter the total number of Sticks\n"))
state_depth, curr_player = 10,0
game_choice = input('a.) BOT vs BOT or\nb.) BOT vs Player\n')


if game_choice == 'a':
	bot_num = int(input("Do you want to team with bot-1 or bot-2\n"))
	if bot_num == 1:
		curr_player = 1
	else:
		curr_player = -1

	player_bot, opponent_bot = randint(1,3), 0
	print('BOT-{}\'s choice : {}'.format(bot_num, player_bot))


	node2 = StateNode(state_depth,curr_player,n_sticks)
	n_sticks -= player_bot

	while n_sticks > 0:

		curr_player = 1
		if get_decision(n_sticks, curr_player, False):
			curr_player *= -1
			node = StateNode(state_depth,curr_player,n_sticks)
			optim_choice = -10
			optim_val = -curr_player * MAXNUM

			for i in range(len(node.children)):
				nChild = node.children[i]

				newVal = alpha_beta(nChild, state_depth, MAXNUM, -MAXNUM, curr_player)
				if abs(curr_player * MAXNUM - newVal) <= abs(curr_player * MAXNUM - optim_val):
					optim_val = newVal
					optim_choice = i

			optim_choice += 1
			if optim_choice > n_sticks:
				optim_choice = n_sticks

			print("BOT-{}\'s choice : {}".format(3-bot_num, optim_choice))
			n_sticks -= optim_choice
			get_decision(n_sticks, curr_player, False)

		bot_num = 3 - bot_num
		curr_player *= -1


elif game_choice == 'b':

	while curr_player != 1 and curr_player != -1:
		curr_player = input("Want to play first chance ? (y or n) : ")
		if curr_player == 'y':
			curr_player = 1
		else:
			curr_player = -1

		node2 = StateNode(state_depth,curr_player,n_sticks)

		if curr_player == 1:
			print("Pick 1 or 2 or 3 sticks\n")

		while n_sticks > 0:
			if curr_player == 1:
				print("{} sticks remaining\n".format(n_sticks))
				choice = int(input("Human's choice : \n"))
				while choice > n_sticks or choice > 3:
					print("{} sticks remaining. Please Enter valid Input\n".format(n_sticks))
					choice = int(input("Human's choice : \n"))
				n_sticks -= int(float(choice))

			else:
				curr_player = 1

			if get_decision(n_sticks, curr_player):
				curr_player *= -1
				node = StateNode(state_depth,curr_player,n_sticks)
				optim_choice = -10
				optim_val = -curr_player * MAXNUM

				for i in range(len(node.children)):
					nChild = node.children[i]
					newVal = alpha_beta(nChild, state_depth, MAXNUM, -MAXNUM, curr_player)

					if abs(curr_player*MAXNUM-newVal) <= abs(curr_player*MAXNUM-optim_val):
						optim_val = newVal
						optim_choice = i

				optim_choice += 1
				if optim_choice>n_sticks:
					optim_choice = n_sticks
				print("BOT's choice : {}\n".format(optim_choice))
				n_sticks -= optim_choice
				get_decision(n_sticks, curr_player)
			curr_player *= -1
