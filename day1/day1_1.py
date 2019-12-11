import sys

def fuel_req(mass):
    return mass // 3 - 2

file = open(sys.argv[1], 'r')

sum = 0
for i in file:
    sum += fuel_req(int(i))

print(sum)
