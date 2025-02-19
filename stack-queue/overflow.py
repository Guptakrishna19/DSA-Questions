class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
    
    def push(self, value):
        if len(self.stack) < self.capacity:
            self.stack.append(value)
        else:
            print("Overflow Error: Stack is full")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Underflow Error: Stack is empty")
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Underflow Error: Stack is empty")
            return None

# Example usage
stack = Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)

# Try to push another element, which will cause overflow
stack.push(40)  # Overflow Error

# Peek at the top element
print(stack.peek())  # 30

# Pop elements
print(stack.pop())  # 30
print(stack.pop())  # 20

# Try to pop from an empty stack, which will cause underflow
print(stack.pop())  # 10
print(stack.pop())  # Underflow Error
