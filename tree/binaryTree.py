# method 1:-

class Tree:
    def __init__(self,n):
        self.data=n
        self.left=None
        self.right=None
def bst(node,min_val='-inf',max_val='-inf'):
    if node is None:
        return
    if node.data <= min_val or node.data >= max_val:
        return False
    return bst(node.left,min_val,node.data) and bst(node.right,node.data,max_val)
        
if __name__ == "__main__":
    # Create a sample binary tree
    #     10
    #    /  \
    #   5    20
    #        / \
    #       9   25
    
    root=Tree(1)
    root.left=Tree(55)
    root.right=Tree(10)
    root.left.left=Tree(25)           
    root.left.right=Tree(4)
    root.right.right=Tree(21)
    
    if bst(root):
        print("The tree is a binary search tree")
    else:
        print("The tree is not a binary search tree")
 
 
        
# method 2:
    
import math
prev = -math.inf

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def checkBST(root):	
	global prev
	if root:
		if not checkBST(root.left):
			return False
		# Handles same valued nodes
		if root.data <= prev:
			return False
		# Set value of prev to current node
		prev = root.data
		return checkBST(root.right)
	return True
# Driver Code
def main():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left=Node(4)
    if checkBST(root):
        print("BST")
    else:
        print("Not BST")

if __name__ == '__main__':
	main()
    