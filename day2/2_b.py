import sys
from itertools import permutations

input_file = open(sys.path[0] + "\\input.txt", "r")
input_array = input_file.readlines()

total = 0

for row in input_array:
    
    row_list = map(int, row.replace('\n', '').split('\t'))
    
    for number in permutations(row_list, 2):
        if number[0] % number[1] == 0:
            total += number[0] / number[1]

print(total)
