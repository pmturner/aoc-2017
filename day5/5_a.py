import sys

input_file = open(sys.path[0] + "\\input.txt", "r")
input_list = input_file.readlines()
maze = [int(item.replace('\n', '')) for item in input_list]

step_count = jump_index = 0

while 0 <= jump_index < len(maze):
	jump_amount = maze[jump_index]
	maze[jump_index] += 1

	jump_index += jump_amount
	step_count += 1

print(step_count)