from collections import deque
class Stack():
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
class Queue():
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Виведе 3
print(stack.peek())  # Виведе 2
print(stack.size())  # Виведе 2
print(stack.is_empty())  # Виведе False
line = Queue()
line.enqueue(1)
line.enqueue(2)
line.enqueue(3)
print(line.dequeue())  # Виведе 1
print(line.peek())  # Виведе 2
print(line.size())  # Виведе 2
print(line.is_empty())  # Виведе False
