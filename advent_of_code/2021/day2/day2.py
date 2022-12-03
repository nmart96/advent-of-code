# find the final submarine position
# start at 0 depth, 0 horizontal
# forward increases horizontal
# down increases depth
# up decreases depth
# find final coordinates and multiply

import fileinput
depth = 0
hori = 0
for line in fileinput.input("input.txt"):
	instr = line.split(' ')
	if instr[0] == "forward":
		hori += int(instr[1])
	elif instr[0] == "down":
		depth += int(instr[1])
	elif instr[0] == "up":
		depth -= int(instr[1])

print("%d, %d", hori, depth)
print(hori * depth)

# solution = 1804520