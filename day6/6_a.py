import sys

input_line = open(sys.path[0] + "\\input.txt", "r").readlines()
memory_bank = list(map(int, input_line[0].split('\t')))

bank_cycle_array = []
cycles = 0

while memory_bank not in bank_cycle_array:
	copy = memory_bank[:]
	bank_cycle_array.append(copy)

	max_value = max(memory_bank)
	max_index = memory_bank.index(max_value)

	memory_bank[max_index] = 0

	step = 0
	while step < max_value:
		max_index = (max_index + 1) % len(memory_bank)
		memory_bank[max_index] += 1
		step += 1

	cycles += 1

print(cycles)