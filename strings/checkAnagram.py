#Implement a function to check if two strings are anagrams.

def checkAnagram(s1,s2):
    # If lengths are not equal, they can't be anagrams
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
s1="listen"
s2="silent"
print(checkAnagram(s1,s2))