# find the number of times a measurement increases
# increases from the previous measurement

import fileinput
depth = 0
numIncrease = 0
for line in fileinput.input("input.txt"):
	if (True == fileinput.isfirstline()):
		depth = int(line)
	else:
		if (depth < int(line)):
			numIncrease += 1
		depth = int(line)

print(numIncrease)

# solution = 1466