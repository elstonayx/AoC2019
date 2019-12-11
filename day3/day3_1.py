import sys

def get_edge_list(command_list):
    curr_point = [0, 0]
    edge_list = []
    for command in command_list:
        move = command[0]
        value = int(command[1:])

        if move == 'R':
            new_point = [curr_point[0] + value, curr_point[1]]

        elif move == 'L':
            new_point = [curr_point[0] - value, curr_point[1]]

        elif move == 'U':
            new_point = [curr_point[0], curr_point[1] + value]

        elif move == 'D':
            new_point = [curr_point[0], curr_point[1] - value]

        edge_list.append([curr_point, new_point])

        curr_point = new_point

    return edge_list

def get_manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

file = open(sys.argv[1], "r")

input_list = [[], []]
idx = 0
for line in file:
    input_list[idx] = [x.rstrip() for x in line.split(",")]
    idx += 1


edge_list_1 = get_edge_list(input_list[0])
edge_list_2 = get_edge_list(input_list[1])

intersection_list = []

for edge_1 in edge_list_1:
    for edge_2 in edge_list_2:
        # if the x value is the same, it's a vertical line
        if edge_1[0][0] == edge_1[1][0] and edge_2[0][1] == edge_2[1][1]:
                if (edge_1[0][0] > min(edge_2[0][0], edge_2[1][0])
                     and edge_1[0][0] < max(edge_2[0][0], edge_2[1][0])
                     and edge_2[0][1] > min(edge_1[0][1], edge_1[1][1])
                     and edge_2[0][1] < max(edge_1[0][1], edge_1[1][1])):
                    intersection_list.append([edge_1[0][0], edge_2[0][1]])

        if edge_2[0][0] == edge_2[1][0] and edge_1[0][1] == edge_1[1][1]:
                if (edge_2[0][0] > min(edge_1[0][0], edge_1[1][0])
                     and edge_2[0][0] < max(edge_1[0][0], edge_1[1][0])
                     and edge_1[0][1] > min(edge_2[0][1], edge_2[1][1])
                     and edge_1[0][1] < max(edge_2[0][1], edge_2[1][1])):
                    intersection_list.append([edge_2[0][0], edge_1[0][1]])


smallest_manhattan_distance = get_manhattan_distance([0,0], intersection_list[0])
for intersection in intersection_list:
    curr_distance = get_manhattan_distance([0,0], intersection)
    smallest_manhattan_distance = min(curr_distance, smallest_manhattan_distance)

print(smallest_manhattan_distance)
