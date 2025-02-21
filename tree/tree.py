
# method 1:-

class Node:
    def __init__(self, n):
        self.data = n
        self.left = None
        self.right = None

    def printNode(self):
        print(self.data)
        if self.left:
            print(self.left.data)
        else:
            print("None")
            
        if self.left.left:
            print(self.left.left.data)
            
        if self.left.right:
            print(self.left.right.data)
            
        if self.right:
            print(self.right.data)
        else:
            print("None")
       
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.left.left.left = Node(6)
root.printNode()


# method 2:-

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print pre order traversal
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)
# Function to print post order traversal
def printPostorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')
    
    # Recur on right subtree
    printPreorder(node.right)

    # Recur on left subtree
    printPreorder(node.left)
# Function to print post order traversal
def printInorder(node):
    if node is None:
        return

    # Recur on right subtree
    printPreorder(node.right)
    
    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)
# Driver code
if __name__ == '__main__':  #check if the script is being run directly
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)
    
    print("\nPostorder traversal of binary tree is:")
    printPostorder(root)
    
    print("\nInorder traversal of binary tree is:")
    printInorder(root)