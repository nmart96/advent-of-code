# find the most common bit for each corresponding place
# in the list

# gamma rate is the resulting binary number
# epsilon rate is the result number of the least common bit

import fileinput
import math

def main():
	diag = []
	for line in fileinput.input("input.txt"):
		diag.append(line.split('\n')[0])

	length = len(diag[0])
	gamma = ""
	epsilon = ""
	for i in range(0,length):
		numZeroes = 0
		numOnes = 0
		for line in diag:
			if (line[i] == '0'):
				numZeroes += 1
			else:
				numOnes += 1
		print(numZeroes, numOnes)
		if (numZeroes > numOnes):
			gamma += '0'
			epsilon += '1'
		else:
			gamma += '1'
			epsilon += '0'
	print(gamma, epsilon)
	gammaInt = strToBin(gamma)
	epsilonInt = strToBin(epsilon)
	print(gammaInt, epsilonInt)
	print(gammaInt*epsilonInt)

def strToBin(input):
	result = 0
	i = 0
	for index in range(len(input)-1, -1, -1):
		if (input[index] == '1'):
			result += int(math.pow(2,i))
		i += 1
	return result

main()

# solution = 3429254
