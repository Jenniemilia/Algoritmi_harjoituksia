from collections import namedtuple

#montako solmua on annetussa binääripuussa tietyllä tasolla
# muokkaa jälkimmäistä parametrikutsua?

def count(node, level):
    
    if not node:
        return 0
    if level == 1:
        return 1
    else:
        laske = count(node.left, level-1) + count(node.right, level-1)
    
    return laske
            
if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0