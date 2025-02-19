class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    current = head
    while current and current.next: #check if the current node and the next node are not None
        if current.value == current.next.value:
            current.next = current.next.next # removing the duplicate node
        else:
            current = current.next
    return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# Remove duplicates from the sorted linked list
updated_list = remove_duplicates(head)

# Print the updated linked list
current = updated_list
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")