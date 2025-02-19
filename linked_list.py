#Reverse a singly linked list.

class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
#adding elements to the linked list      
head=LinkedList(1)
head.next=LinkedList(2)
head.next.next=LinkedList(3)

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    # print("None")
    
print_linked_list(head)
print_linked_list(reverse_linked_list(head))


#Detect a cycle in a linked list and find the starting node of the cycle.
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

# Example usage
if __name__ == "__main__":
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
