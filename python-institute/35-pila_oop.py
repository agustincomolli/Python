class Stack():
    def __init__(self):
        self.__stack_list = []


    def push(self, item):
        self.__stack_list.append(item)


    def pop(self):
        last = self.__stack_list[-1]
        del self.__stack_list[-1]
        return last


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    
    def push(self, item):
        self.__sum += item
        Stack.push(self, item)


    def pop(self):
        last = Stack.pop(self)
        self.__sum -= last
        return last
    

    def get_sum(self):
        return self.__sum


stack_object = Stack()
stack_object.push(1)
stack_object.push(2)
stack_object.push(3)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

stack_object = AddingStack()
for i in range(5):
    stack_object.push(i)

print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())