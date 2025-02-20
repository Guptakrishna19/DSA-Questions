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
         