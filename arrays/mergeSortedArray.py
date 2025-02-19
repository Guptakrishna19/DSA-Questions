#Implement a function to merge two sorted arrays into a single sorted array.
def mergeSortedArray(arr1,arr2):
    arr1.sort()
    arr2.sort()
    return arr1 + arr2
arr1=[1,2,3,4,5]
arr2=[6,7,8,9,10]
print(mergeSortedArray(arr1,arr2))