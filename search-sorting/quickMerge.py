def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot=arr.pop()
        less_value=[]
        greater_value=[]
        for i in arr:
            if i <= pivot:
                less_value.append(i)
            else:
                greater_value.append(i)
        return quicksort(less_value)+[pivot]+quicksort(greater_value)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


arr=[4,6,9,7,8,5]
print(quicksort(arr))
print(mergeSort(arr))



