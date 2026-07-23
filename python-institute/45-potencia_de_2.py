def power_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for value in power_of_2(8):
    print(value)


list_powers = list(power_of_2(3))
print(list_powers)

for i in range(20):
    if i in power_of_2(4):
        print(i)