# Artificial-Intelligence-Assignments

## N Queens Problem: UCS

The ***nQueens_UCS.cpp*** file contains the solution to this problem.\n
UCS - Uniform Cost Search is variation which also considers cost of moving from one state to other into account.

1.) Here The n x n matrix is considered as a graph\n
2.) Travelling from one cell to other has cost value = 1\n
3.) Constraint - No 2 queens should be placed such that they can attack each other.\n
4.) Output - gives the sequence in which the queens should be placed in each column.\n

## Travelling SalesMan Problem: Astar

The ***travelling_salesman.cpp*** contains the solution to this problem.
Astar - A* algorithm is like UCS, which also takes heuristics into account.

1.) The program the number of cities N and distance between each of them as input.\n
2.) output is the order in which salesman should visit the cities.\n

## Genetic algorithm:

The ***genetic.py*** contains the solution to this problem.

A genetic algorithm is a search heuristic that is inspired by Charles Darwin's theory of natural evolution.\n
This algorithm reflects the process of natural selection, where the fittest individuals are selected for reproduction\n
in order to produce offsprings of next generation.\n

## Game of Sticks:

The ***game_of_sticks.py*** contains the solution to this problem using Minmax with Alpha Beta pruning.

It is a game in which there are 2 opponents. Each opponent pics a maximum of 3 sticks in their turn. The opponent to pick last stick looses the game.\n
The user can choose to play with AI or let 2 AIs compete with each other.\n
