      
      
""" height of the tree """
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def heightOfTree(node):
    if node is None:
        return 0
    else:
        left_depth = heightOfTree(node.left) #get the height of left subtree
        right_depth = heightOfTree(node.right) #get the height of right subtree
        return max(left_depth, right_depth) + 1 #return the maximum of left and right subtree height + 1 because it height level start from 0 to n 

# Constructing the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
    
print('Maximum Depth of the Binary Tree:', heightOfTree(root))         






'''In this code, we will find the highest value in the tree'''
class Tree:
    def __init__(self,n):
        self.data=n
        self.left=None
        self.right=None
        
def highestValue(node):
    if node is None:
        return 
    max_val=node.data
    if node.left is not None:
        let_max=highestValue(node.left)
        max_val=max(max_val,let_max)
    if node.right is not None:
        right_max=highestValue(node.right)
        max_val=max(max_val,right_max)
    return max_val

if __name__ == "__main__":
    root=Tree(1)
    root.left=Tree(55)
    root.right=Tree(10)
    root.left.left=Tree(25)
    root.left.right=Tree(4)
    root.right.right=Tree(21)
    print("The highest value in the tree is:",highestValue(root))
      
      
      
      
