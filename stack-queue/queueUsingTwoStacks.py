class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            print("Underflow Error: Queue is empty")
            return None
            
# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.dequeue())  # Should print 2
queue.enqueue(4)
print(queue.dequeue())  # Should print 3
print(queue.dequeue())  # Should print 4
print(queue.dequeue())  # Should trigger "Underflow Error: Queue is empty"