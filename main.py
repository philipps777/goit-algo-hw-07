import networkx as nx
import matplotlib.pyplot as plt
from ddp_tree import Node, insert, plot_tree
from find_max_value import find_max_value
from find_min_value import find_min_value
from find_sum_of_values import find_sum_of_values


def main():
    root = Node(50)
    values_to_insert = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]

    for value in values_to_insert:
        insert(root, value)

    max_value = find_max_value(root)
    print(f"Найбільше значення в дереві: {max_value}")

    min_value = find_min_value(root)
    print("Найменше значення у дереві:", min_value)

    sum_of_values = find_sum_of_values(root)
    print("Сума всіх значень у дереві:", sum_of_values)

    G = nx.DiGraph()
    G.add_node(str(root.val))
    queue = [root]
    while queue:
        current = queue.pop(0)
        neighbors = [current.left, current.right]
        for neighbor in neighbors:
            if neighbor is not None:
                G.add_node(str(neighbor.val))
                G.add_edge(str(current.val), str(neighbor.val))
                queue.append(neighbor)

    pos = plot_tree(G, root)

    nx.draw(G, pos=pos, with_labels=True, arrows=False,
            node_size=700, node_color='skyblue', font_size=8)
    plt.show()


if __name__ == "__main__":
    main()
