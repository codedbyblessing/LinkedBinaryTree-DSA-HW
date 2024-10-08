
from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree):
    bin_tree.data = LinkedBinaryTree()
    def subtree_min_and_max(root):

        if root.left is None and root.right is None:
            return (root.data, root.data)

        elif root.left is None and root.right is not None:
            right_leaf = subtree_min_and_max(root.right)
            return (min(right_leaf[0], root.data), max(right_leaf[1], root.data))

        elif root.left is not None and root.right is None:
            left_leaf = subtree_min_and_max(root.left)
            return (min(left_leaf[0], root.data), max(left_leaf[1], root.data))

        else:
            right_leaf = subtree_min_and_max(root.right)
            left_leaf = subtree_min_and_max(root.left)
            return (min(left_leaf[0], right_leaf[0], root.data), max(left_leaf[1], right_leaf[1], root.data))
    if bin_tree.root is None:
        raise Exception("min and max does nto exists on the tree")
    return subtree_min_and_max(bin_tree.root)
