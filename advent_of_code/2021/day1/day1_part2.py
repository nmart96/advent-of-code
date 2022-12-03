# find the number of times a measurement increases
# increases from the previous measurement

import fileinput
depth = 0
numIncrease = 0
arr = []
for line in fileinput.input("input.txt"):
	arr.append(int(line))
for i in range(2,len(arr)-1):
	firstWindow = arr[i-2] + arr[i-1] + arr[i]
	secondWindow = arr[i-1] + arr[i] + arr[i+1]
	if (secondWindow > firstWindow):
		numIncrease += 1

print(numIncrease)

# solution = 1491