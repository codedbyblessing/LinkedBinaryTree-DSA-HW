def is_height_balanced(bin_tree):
    def check_balanced(root):
        if root is None:
            return (True, 0)

        right_leaf = check_balanced(root.right)
        left_leaf = check_balanced(root.left)
        height = max(left_leaf[1], right_leaf[1]) + 1
        if not (left_leaf[0] and right_leaf[0]) or abs(left_leaf[1] - right_leaf[1]) > 1:
            return (False, height)
        return (True, height)
    if bin_tree.root is None:
        raise Exception("Height-Balance Property does not satisfy requirements")
    return check_balanced(bin_tree.root)[0]
