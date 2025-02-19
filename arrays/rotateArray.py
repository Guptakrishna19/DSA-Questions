#Given an array, rotate it by K positions to the right.

def rotatearray(arr,k):
    k = k % len(arr) # to check if k is greater than or equal to the length of the array if k is equall to n then the array will be same as the original array
    return arr[-k:] + arr[:-k]
arr=[1,2,3,4,5,6,7]
k=3
print(rotatearray(arr,k))