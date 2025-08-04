class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root

# Example Usage:
# Construct a sample tree:
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

# root = TreeNode(4)
# root.left = TreeNode(2, TreeNode(1), TreeNode(3))
# root.right = TreeNode(7, TreeNode(6), TreeNode(9))

# inverted_root = invertTree(root)

# Now, inverted_root would represent:
#       4
#      / \
#     7   2
#    / \ / \
#   9  6 3  1