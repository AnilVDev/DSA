from queue import LifoQueue

stack = LifoQueue(maxsize = 3)
print(stack.qsize())

stack.put('a')
stack.put('10')
stack.put('b')
print(stack.full())

print(stack.get())
print(stack.get())
print(stack.get())
print(stack.empty())