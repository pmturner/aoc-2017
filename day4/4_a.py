import sys

input_file = open(sys.path[0] + "\\input.txt", "r")
all_passphrase_list = input_file.readlines()

valid_count = 0

for passphrases in all_passphrase_list:
	passphrase_list = passphrases.split()

	if len(passphrase_list) == len(set(passphrase_list)):
		valid_count += 1

print(valid_count)