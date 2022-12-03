## Advent of Code
## Day 3 part 3
# answer = 2515

# Rucksak Reorganization

import fileinput

elves = []

for line in fileinput.input():
	line = line.replace("\n", "")
	elves.append(line)

prioritySum = 0
j = 0

for i in range(0, len(elves)):
	priority = 0
	if ( j == 2 ):
		j = 0
		for char1 in elves[i-2]:
			for char2 in elves[i-1]:
				for char3 in elves[i]:
					if ( (char1 == char2) and (char1 == char3) ):
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
			if (priority != 0):
				break
	else:
		j += 1

print(prioritySum)