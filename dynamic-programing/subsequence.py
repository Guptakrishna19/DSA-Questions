def long(nums):
    n=len(nums)
    arr=[1] * n  #initially array value is 1 of each index
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                arr[i]=max(arr[i],arr[j]+1)
    return max(arr)
arr=[10, 20, 30, 40, 50, 60, 70, 80]
print(long(arr))