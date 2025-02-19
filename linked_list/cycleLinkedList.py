#Detect a cycle in a linked list and find the starting node of the cycle.
class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = head.next  # Create a cycle

cycle_start = detect_cycle(head)
if cycle_start:
    print(f"Cycle detected at node with value: {cycle_start.value}")
else:
    print("No cycle detected")
