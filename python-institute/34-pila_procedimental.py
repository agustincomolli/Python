stack = []

def push(item):
    stack.append(item)


def pop():
    last = stack[-1]
    del stack[-1]

    return last


push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())