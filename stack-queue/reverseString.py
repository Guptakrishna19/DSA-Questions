def reverse_string(s):
    stack = []
    for i in s:
        stack.append(i)
    result = ""
    while stack:
        result += stack.pop()
    return result
s="Hello"
print(reverse_string(s))
