
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def lca(root, n1, n2):
  
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA lies in left subtree
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA lies in right subtree
    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root.data


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Find LCA of nodes 10 and 14
ancestor = lca(root, 10, 14)
if ancestor:
    print(f"LCA of 10 and 14 is {ancestor}")
else:
    print("LCA not found")