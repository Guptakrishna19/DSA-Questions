# Find the duplicate number in an array where each number appears twice except one
def findDuplicate(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
arr=[1,2,3,4,5,6,7,1,2,3,4,5,6]
print(findDuplicate(arr))
