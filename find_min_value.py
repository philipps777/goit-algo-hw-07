def find_min_value(root):
    current = root
    while current.left:
        current = current.left
    return current.val
