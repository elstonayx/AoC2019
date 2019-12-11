import sys

def opcode_1(arr, adder_pos_1, adder_pos_2, result_pos):
    arr[result_pos] = arr[adder_pos_1] + arr[adder_pos_2]

def opcode_2(arr, multiplier_pos_1, multipler_pos_2, result_pos):
    arr[result_pos] = arr[multiplier_pos_1] * arr[multiplier_pos_2]

def run_op_code(arr):
    ptr = 0
    while True:
        if arr[ptr] == 99:
            break

        pos_1 = arr[ptr + 1]
        pos_2 = arr[ptr + 2]
        result_pos = arr[ptr + 3]

        if arr[ptr] == 1:
            arr[result_pos] = arr[pos_1] + arr[pos_2]

        elif arr[ptr] == 2:
            arr[result_pos] = arr[pos_1] * arr[pos_2]

        ptr += 4

    return arr[0]

file = open(sys.argv[1], "r")

number_list = []

for line in file:
    stripped_line = line.rstrip("\n")
    number_list = [int(x) for x in stripped_line.split(",")]

for i in range(100):
    for j in range(100):
        new_list = number_list.copy()
        new_list[1] = i
        new_list[2] = j

        try:
            result = run_op_code(new_list)
        except Exception:
            pass
        #print(new_list)

        if result == 19690720:
            print(i * 100 + j)
