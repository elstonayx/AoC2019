import sys

def opcode_1(arr, adder_pos_1, adder_pos_2, result_pos):
    arr[result_pos] = arr[adder_pos_1] + arr[adder_pos_2]

def opcode_2(arr, multiplier_pos_1, multipler_pos_2, result_pos):
    arr[result_pos] = arr[multiplier_pos_1] * arr[multiplier_pos_2]

file = open(sys.argv[1], "r")

number_list = []

for line in file:
    stripped_line = line.rstrip("\n")
    number_list = [int(x) for x in stripped_line.split(",")]

number_list[1] = 12
number_list[2] = 2

ptr = 0
while True:
    if number_list[ptr] == 99:
        break

    pos_1 = number_list[ptr + 1]
    pos_2 = number_list[ptr + 2]
    result_pos = number_list[ptr + 3]

    if number_list[ptr] == 1:
        number_list[result_pos] = number_list[pos_1] + number_list[pos_2]

    elif number_list[ptr] == 2:
        number_list[result_pos] = number_list[pos_1] * number_list[pos_2]

    ptr += 4

print(number_list[0])
