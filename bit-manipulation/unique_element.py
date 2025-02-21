def unique(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]: #if element is repeated
                count +=1
        if count==1: #if element is not repeated
            return arr[i]
print(unique([1,2,3,4,1,4,3]))
