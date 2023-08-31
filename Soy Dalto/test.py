count = 0
total = 0
average = 0
number = int(input())

while number != 55:
    count += 1
    total += number

print(count)
print(total)
print(round(total / count))