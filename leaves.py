"""montako lehteä on annetussa binääripuussa"""

from collections import namedtuple

def count(node):
    if not node:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count(node.left) + count(node.right)
    

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None, Node(Node(None, None),Node(None, None)))
    print(count(tree)) # 2 print(count(tree)) # 2