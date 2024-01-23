
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def plot_tree(G, node, pos=None, x=0, y=0, layer=1, width=2., vert_gap=0.4, xcenter=0.5):
    if pos is None:
        pos = {str(node.val): (xcenter, y)}
    else:
        pos[str(node.val)] = (xcenter, y)
    neighbors = [node.left, node.right]
    if neighbors[0] is not None:
        G.add_edge(str(node.val), str(neighbors[0].val))
        pos = plot_tree(G, neighbors[0], pos=pos,
                        x=x - width / 2 - width / 4, y=y - vert_gap, layer=layer + 1, width=width / 2, xcenter=x - width / 4)
    if neighbors[1] is not None:
        G.add_edge(str(node.val), str(neighbors[1].val))
        pos = plot_tree(G, neighbors[1], pos=pos,
                        x=x + width / 2 + width / 4, y=y - vert_gap, layer=layer + 1, width=width / 2, xcenter=x + width / 4)
    return pos
