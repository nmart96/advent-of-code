## Advent of Code
## Day 3
# answer = 8085

# Rucksak Reorganization

import fileinput

prioritySum = 0

for line in fileinput.input():
	firstCompartment = line[0 : int(len(line)/2)]
	secondCompartment = line[int(len(line)/2) : len(line)]
	secondCompartment.replace("\n", "")
	
	for char1 in firstCompartment:
		priority = 0
		for char2 in secondCompartment:
			if (char1 == char2):
				# ord gets ascii value
				# a is priority 1
				# Z is priority 52
				if (ord(char1) >= ord('a')):
					priority = ord(char1) - (ord('a') - 1)
				else:
					priority = ord(char1) - (ord('A') - 1) + 26

				prioritySum += priority
				break
		if (priority != 0):
			break

print(prioritySum)