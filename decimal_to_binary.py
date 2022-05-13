from stack import Stack

def decimal_to_binary(num):

    if num == 0 or num < 0:
        return 0
    
    s = Stack()
    
    while num > 0:
        r = num % 2
        s.push(r)
        num = num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    
    return bin_num

print(decimal_to_binary(242))
print(decimal_to_binary(0))
print(decimal_to_binary(-34))