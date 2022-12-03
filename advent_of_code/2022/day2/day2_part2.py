## Advent of Code
## Day 2 part 2
# answer = 11980

## First column is opponent's play
## Second column is my play

## A is opponent rock
## B is opponent paper
## C is opponent scissors

## X == lose
## Y == draw
## Z == win

## my rock is Score of 1
## my paper is Score of 2
## my scissors is Score of 3

## Outcome Scores
## 0 if I lose
## 3 if I draw
## 6 if I win

## output sum of my shape + my outcome for all rounds

import fileinput

outcome = 0
for line in fileinput.input():
	oppShape = line.split(' ')[0][0] # gets one character
	myShape = line.split(' ')[1][0] # gets first character

	if (myShape == 'X'): # lose
		outcome += 0
		if (oppShape == 'A'):
			# scissors
			outcome += 3
		elif (oppShape == 'B'):
			# rock
			outcome += 1
		else: # 'C' paper
			outcome += 2
	elif (myShape == 'Y'): # draw
		outcome += 3
		if (oppShape == 'A'):
			# rock
			outcome += 1
		elif (oppShape == 'B'):
			# paper
			outcome += 2
		else: # 'C' scissors
			outcome += 3
	else: # win
		outcome += 6
		if (oppShape == 'A'):
			# paper
			outcome += 2
		elif (oppShape == 'B'):
			# scissors
			outcome += 3
		else: # 'C' rock
			outcome += 1

print(outcome)





