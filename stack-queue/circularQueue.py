class Circular:
    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        
    def isFull(self): #to check if the queue is full
        return (self.rear + 1) % self.capacity == self.front
    
    def isEmpty(self): #to check if the queue is empty
        return self.front == -1 
    
    def peek(self): # get the front element of the queue
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[self.front] 
      
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        item = self.queue[self.front] # Get the front element
        if self.front == self.rear:  # If only one element was present
            self.front = self.rear = -1  # Reset queue
        else:
            self.front = (self.front + 1) % self.capacity  # Move front circularly
        return item

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return 
        i = self.front
        while True:
            print(self.queue[i],end = " ")
            if i == self.rear:
                break
            i= (i+1) % self.capacity
        print() 
            
 # Example Usage
c = Circular(6)
print("Checking queue :",c.display())
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.enqueue(40)
c.enqueue(50)
c.display()  # Output: 10 20 30 40 50
print("Front element:", c.peek())  # Output: Front element: 10
print("deleting element:",c.dequeue())
c.display()  # Output: 20 30 40 50