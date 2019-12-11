import sys

def fuel_req(mass):
    return mass // 3 - 2

def fuel_for_fuel(total_fuel, mass):
    if mass <= 0:
        return total_fuel

    return fuel_for_fuel(mass + total_fuel, fuel_req(mass))

file = open(sys.argv[1], 'r')

sum = 0
for i in file:
    sum += fuel_for_fuel(0, int(i)) - int(i)

print(sum)
