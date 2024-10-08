from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    def expression_helper(prefix_exp_lst, start_pos):
        op = prefix_exp_lst[start_pos]
        if op not in "+-*/":
            tree_root = LinkedBinaryTree.Node(int(op))
            return (tree_root, start_pos + 1)
        left_leaf = expression_helper(prefix_exp_lst, start_pos + 1)
        right_leaf = expression_helper(prefix_exp_lst, left_leaf[1])
        tree_root = LinkedBinaryTree.Node(op, left_leaf[0], right_leaf[0])
        return (tree_root, right_leaf[1])
    prefix_lst = prefix_exp_str.split()
    return LinkedBinaryTree(expression_helper(prefix_lst, 0)[0])


def prefix_to_postfix(prefix_exp_str):
    bin_tree = create_expression_tree(prefix_exp_str)
    postfix_exp_str = " ".join(str(node.data) for node in bin_tree.postorder())
    return postfix_exp_str
