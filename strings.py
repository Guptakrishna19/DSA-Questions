
#Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
s="madam"
print(is_palindrome(s))

#Reverse words in a given sentence without using extra space.
def reverseWords(s):
    return ' '.join(s.split()[::-1])  #s.split() splits the string into a list of words, and [::-1] reverses the list.
s="Hello World"
print(reverseWords(s))

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

#Implement a function to check if two strings are anagrams.

def checkAnagram(s1,s2):
    # If lengths are not equal, they can't be anagrams
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
s1="listen"
s2="silent"
print(checkAnagram(s1,s2))