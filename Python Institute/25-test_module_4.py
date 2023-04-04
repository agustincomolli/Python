dictionay = {}
my_list = ["a", "b", "c", "d"]

for i in range(len(my_list) - 1):
    dictionay[my_list[i]] = (my_list[i],)

for i in sorted(dictionay.keys()):
    k = dictionay[i]
    print(k[0])


print()


def fun(x):
    global y

    y = x * x
    return y


fun(2)
print(y)

print()


def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

print()

tuple = (1, 2, 3)
# tuple[1] = tuple[1] + tuple[2]

print()


def any():
    print(var + 1, end="")


var = 1
any()
print(var)

print()


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


# print(fun(fun(2)) + 1)

print()
# dictionary = {"one": "two", "three": "one", "two": "three"}
# v = dictionay["one"]

# for k in range(len(dictionay)):
#     v = dictionay[v]

#print(v)


print()
tup = (1,2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)


def fun(x, y ,z):
    return x + 2 * y + 3 * z

print(fun(0,z = 1, y=3))