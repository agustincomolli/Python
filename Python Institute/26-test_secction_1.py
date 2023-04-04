x = float(2)
y = float(4)
print(y ** (1/2))


print("#" * 10)
a = 1
b = 0
a = a^b
b = a^b
a = a^b 
print(a,b)

print("#" * 10)
def func(a,b):
    return b ** a

#print(func(b=2, 2))

print("x" * 10)
lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")


print("x" * 10)
list = [i for i in range(-1, -2)]
print(len(list))

print("#" * 10)
nums = [1,2,3]
vals = nums
del vals[:]
print(len(nums))

print("#" * 10)
dct = {"one": "two", "three": "one", "two": "three"}
v = dct["three"]
for k in range(len(dct)):
    v = dct[v]
print(v)

print("#" * 10)
def func(x, y):
    if x== y:
        return x
    else:
        return func(x, y-1)
    
print(func(0,3))

print("#" * 10)
foo = (1,2,3)
# foo.index(0)

print("#" * 10)
print(1//5+1/5)

print("#" * 10)
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))

print("#" * 10)
# i = 0
# while i < i+ 2:
#     i += 1
#     print("*")
# else:
#     print("*")

print("#" * 10)
x = 3
y= 2
x = x % y
x = x%y
y = y%x
print(y)

print("#" * 10)
# try:
#     print(5/0)
#     break
# except:
#     print("")
# except (ValueError, ZeroDivisionError):
#     print()

print("#" * 10)
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

print("#" * 10)
my_list = [1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)

print("#" * 10)
dct = {}
dct["1"] = (1,2)
dct["2"] = (2,1)
for x in dct.keys():
    print(dct[x][1], end="")

print("#" * 10)
my_list = [x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))

print("#" * 10)
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)