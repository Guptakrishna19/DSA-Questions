def binarySearch(arr,item):
    starting_index=0
    ending_index=len(arr)
    while starting_index <= ending_index:
        mid=(starting_index+ending_index)//2
        if arr[mid]==item:
            return mid
        elif arr[mid] < item:
            starting_index=mid+1
        else:
            ending_index=mid-1
    return -1
arr=[1,2,3,4,5,6,7,8,9]
item=5
print(binarySearch(arr,item))