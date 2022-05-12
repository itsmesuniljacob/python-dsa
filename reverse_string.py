from stack import Stack

def reverse_string(stack, str):
    for i in range(len(str)):
        stack.push(str[i])
        s = stack.get_stack()
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

stack = Stack()
print('------------------------------')
print(reverse_string(stack,'Hello'))
print('------------------------------')