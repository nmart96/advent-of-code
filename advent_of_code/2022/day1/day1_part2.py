## Advent of Code Day 1
## nmart
# answer = 207456

import fileinput

caloriesSum = 0
maxCalories = 0
elves = []

for line in fileinput.input():
	if (line == "\n"):
		if (caloriesSum > maxCalories):
			maxCalories = caloriesSum
		elves.append(caloriesSum)
		caloriesSum = 0
	else:
		caloriesSum += int(line)

print(maxCalories)
print(elves)

top3Elves = []
for i in range(3):
	maxCalories = 0
	for elf in elves:
		if (elf > maxCalories):
			maxCalories = elf
	top3Elves.append(maxCalories)
	for elf in elves:
		if (elf == maxCalories):
			elves.remove(elf)
			break

print(top3Elves)

sum3 = 0
for elf in top3Elves:
	sum3 += elf

print(sum3)