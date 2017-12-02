import sys

input_file = open(sys.path[0] + "\\input.txt", "r")
input_array = input_file.readlines()

total_sum_array = []
for row in input_array:
    row_list = sorted(map(int, row.replace('\n', '').split('\t')))
    total_sum_array.append(row_list[-1] - row_list[0])
    # print(total_sum_array)

print(sum(total_sum_array))
