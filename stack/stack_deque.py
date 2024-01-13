from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(' initial stack:',stack)

print(stack.pop())
print(stack.pop())
print('After pop stack:',stack)