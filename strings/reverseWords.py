#Reverse words in a given sentence without using extra space.
def reverseWords(s):
    return ' '.join(s.split()[::-1])  #s.split() splits the string into a list of words, and [::-1] reverses the list.
s="Hello World"
print(reverseWords(s))