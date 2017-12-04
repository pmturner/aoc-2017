import sys

input_file = open(sys.path[0] + "\\input.txt", "r")
input_list = input_file.readlines()

valid_count = 0

for passphrase_line in input_list:
	passphrase_list = passphrase_line.split()

	sorted_passphrase_parts = map(sorted, passphrase_list)

	passphrase_array = []
	for passphrase in sorted_passphrase_parts:
		passphrase_array.append(''.join(passphrase))


	#can't set a list since they are unhashable
	passphrase_array_set = set(passphrase_array)

	if len(passphrase_list) == len(passphrase_array_set):
		valid_count += 1

print(valid_count)