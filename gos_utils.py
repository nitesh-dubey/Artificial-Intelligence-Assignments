from random import randint
import math
MAXNUM = 10**6

class StateNode:
	def __init__(self,state_depth,player_num,rem_sticks,val=0):
		self.state_depth=state_depth
		self.player_num=player_num
		self.val=val
		self.rem_sticks=rem_sticks
		self.children=[]
		self.CreateChildren()

	def height(self):  
		h = 0  
		for c in self.children:  
			h = max(h, c.height() + 1)
		return h

	def get_val(self,val):
		if(val==0):
			return MAXNUM*-self.player_num
		elif(val<0): 
			return MAXNUM*-self.player_num
		return 0

	def CreateChildren(self):
		if self.state_depth>=0:
			for i in range(1,3):
				v=self.rem_sticks-i
				self.children.append(StateNode(self.state_depth-1,-self.player_num,v,self.get_val(v)))
  

def alpha_beta(StateNode, state_depth, alpha, beta, player_num):
	if(state_depth==0) or (abs(StateNode.val) == MAXNUM): return StateNode.val

	optim_val=MAXNUM*-player_num

	if (player_num == 1):
		for i in range(len(StateNode.children)):
			child=StateNode.children[i]
			alpha = max(alpha, alpha_beta(child, state_depth - 1, alpha, beta, 1))
			if beta <= alpha:
				break
		return alpha
		
	else:
		for i in range(len(StateNode.children)):
			child=StateNode.children[i]
			beta = min(beta, alpha_beta(child, state_depth - 1, alpha, beta, -1))
			if beta <= alpha:
				break
		return beta
		

def get_decision(sticks,player_num,human_chance=True):
	if human_chance:
		if sticks <= 0:
			if player_num > 0:
				if sticks == 0:
					print("\t BOT wins the Game\n")
				else:
					print("\t You win The Game\n")
			else:
				if sticks == 0:
					print("\t You win the Game\n")
				else:
					print("\t BOT wins the Game\n")
			return 0
		return 1
	else:
		if sticks <= 0:
			if player_num > 0:
				if sticks == 0:
					print("\t BOT-1 wins the Game\n")
				else:
					print("\t BOT-2 wins the Game\n")
			else:
				if sticks == 0:
					print("\t BOT-2 wins the Game\n")
				else:
					print("\t BOT-1 wins the Game\n")
			return 0
		return 1


