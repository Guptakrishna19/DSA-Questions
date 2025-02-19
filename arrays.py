# question no 3 remaining



#Write a program to find the missing number in an array of integers from 1 to N.
def findMissingNumber(arr):
    n=len(arr) + 1 
    expectedSum = n * (n+1) // 2 
    actualSum = sum(arr) 
    return expectedSum - actualSum
arr=[1,2,3,4,6,7,8]
print(findMissingNumber(arr))

#Given an array, rotate it by K positions to the right.

def rotatearray(arr,k):
    k = k % len(arr) # to check if k is greater than or equal to the length of the array if k is equall to n then the array will be same as the original array
    return arr[-k:] + arr[:-k]
arr=[1,2,3,4,5,6,7]
k=3
print(rotatearray(arr,k))

# Find the duplicate number in an array where each number appears twice except one
def findDuplicate(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
arr=[1,2,3,4,5,6,7,1,2,3,4,5,6]
print(findDuplicate(arr))

#Implement a function to merge two sorted arrays into a single sorted array.
def mergeSortedArray(arr1,arr2):
    arr1.sort()
    arr2.sort()
    return arr1 + arr2
arr1=[1,2,3,4,5]
arr2=[6,7,8,9,10]
print(mergeSortedArray(arr1,arr2))