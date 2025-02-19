class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.value < l2.value: # Compare the values of the two nodes
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next # Move current to the next node

    if l1:
        current.next = l1 # Append the remaining elements of l1
    if l2:
        current.next = l2 # Append the remaining elements of l2

    return dummy.next

# Create first sorted linked list: 1 -> 3 -> 5
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

# Create second sorted linked list: 2 -> 4 -> 6
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

# Merge the two sorted linked lists
merged_list = merge_two_sorted_lists(l1, l2)

# Print the merged sorted linked list
current = merged_list
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

