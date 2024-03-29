 # LIFO LAST IN, FIRST OUT
class MyStack:

    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        popped_item = self.array.pop()
        return popped_item

    def peek(self):
        return self.__current()

    def __current(self):
        return self.array[self.count()-1]

    def count(self):
        return len(self.array)

    def __iter__(self):
        self.index = self.count()-1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        result = self.array[self.index]
        self.index -= 1
        return result

stack = MyStack()

stack.push(1) # add to stack
stack.push(2)
stack.push(3)
print(f"pop - {stack.pop()}")
print(f"peek {stack.peek()}")
print(f"count {stack.count()}")
stack.push(4)
stack.push(5)
stack.push(6)

for i in stack:
    print(i)



