def find_sum_of_values(root):
    if root is None:
        return 0
    else:
        return root.val + find_sum_of_values(root.left) + find_sum_of_values(root.right)
