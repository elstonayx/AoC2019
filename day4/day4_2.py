import sys

def check_valid_password(password):
    password_str = str(password)

    if len(password_str) != 6:
        return False

    number_rep = [0 for i in range(10)]
    is_increasing_digit = True
    is_adj_digit = False
    for i in range(5):
        if password_str[i] > password_str[i+1]:
            is_increasing_digit = False
            break

        if password_str[i] == password_str[i+1]:
            if number_rep[int(password_str[i])] == 0:
                number_rep[int(password_str[i])] = 2
            else:
                number_rep[int(password_str[i])] +=1

    for reps in number_rep:
        if reps == 2:
            is_adj_digit = True
    return is_increasing_digit and is_adj_digit

file = open(sys.argv[1], "r")

for line in file:
    stripped_line = line.rstrip("\n")
    lower_limit = int(stripped_line.split("-")[0])
    upper_limit = int(stripped_line.split("-")[1])

valid_passwords = 0
for i in range(lower_limit, upper_limit):
    if check_valid_password(i):
        valid_passwords += 1

print(valid_passwords)
print(check_valid_password(224444))
print(check_valid_password(111444))
