#Write a program to find the missing number in an array of integers from 1 to N.
def findMissingNumber(arr):
    n=len(arr) + 1 
    expectedSum = n * (n+1) // 2 
    actualSum = sum(arr) 
    return expectedSum - actualSum
arr=[1,2,3,4,6,7,8]
print(findMissingNumber(arr))