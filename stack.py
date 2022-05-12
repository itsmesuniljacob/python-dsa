"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    def get_stack(self):
        return self.items

    def peek(self):
        return self.items[-1]

myStack = Stack()
myStack.push('A')
myStack.push('B')
print(myStack.is_empty())
print(myStack.peek())
myStack.push('C')
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())

