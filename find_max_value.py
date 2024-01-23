def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val
