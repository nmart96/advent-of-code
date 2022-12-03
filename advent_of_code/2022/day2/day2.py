## Advent of Code
## Day 2
# answer = 12740

## First column is opponent's play
## Second column is my play

## A is opponent rock
## B is opponent paper
## C is opponent scissors

## X is my rock. Score of 1
## Y is my paper. Score of 2
## Z is my scissors. Score of 3

## Outcome Scores
## 0 if I lose
## 3 if I draw
## 6 if I win

## output sum of my shape + my outcome for all rounds

import fileinput

outcome = 0
for line in fileinput.input():
	oppShape = line.split(' ')[0][0]
	myShape = line.split(' ')[1][0]

	if (myShape == 'X'): # rock
		outcome += 1
		if (oppShape == 'A'):
			# draw
			outcome += 3
		elif (oppShape == 'B'):
			# lose
			outcome += 0
		else: # 'C' win
			outcome += 6
	elif (myShape == 'Y'): # paper
		outcome += 2
		if (oppShape == 'A'):
			# win
			outcome += 6
		elif (oppShape == 'B'):
			# draw
			outcome += 3
		else: # 'C' lose
			outcome += 0
	else: # scissors
		outcome += 3
		if (oppShape == 'A'):
			# lose
			outcome += 0
		elif (oppShape == 'B'):
			# win
			outcome += 6
		else: # 'C' draw
			outcome += 3

print(outcome)





