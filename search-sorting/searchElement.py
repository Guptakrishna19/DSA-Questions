# Search for an element in a rotated sorted array.
def search_rotated_array(nums, target):
    left, right = 0, nums.length - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which part is sorted
        if nums[left] <= nums[mid]:
            # Left part is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right part is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
index = search_rotated_array(nums, target)
print(f"Index of {target}: {index}")