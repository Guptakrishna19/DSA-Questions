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
