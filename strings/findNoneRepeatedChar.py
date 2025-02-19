#Find the first non-repeating character in a string.
def FindNonrepeatedcharacter(s):
    firstNoneRepeated = {}
    for i in s:
        if i in firstNoneRepeated:
            firstNoneRepeated[i] += 1
        else:
            firstNoneRepeated[i] = 1
    for i in s:
        if firstNoneRepeated[i] == 1:
            return i
    return None
s="hello"
print(FindNonrepeatedcharacter(s))