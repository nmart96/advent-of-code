## Advent of Code Day 1
## nmart
# answer = 69177

import fileinput

caloriesSum = 0
maxCalories = 0

for line in fileinput.input():
	if (line == "\n"):
		if (caloriesSum > maxCalories):
			maxCalories = caloriesSum
		caloriesSum = 0
	else:
		caloriesSum += int(line)

print(maxCalories)