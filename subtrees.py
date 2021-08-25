# Laske suurin ero vasemman ja oikean alipuun solmujen määrässä jossain binääripuun solmussa

from collections import namedtuple

isoin_ero = []
def count(node):
    
    if not node:
        return 0
    left_value = count(node.left)
    right_value = count(node.right)
    
    erotus= (abs(left_value-right_value))
    isoin_ero.append(erotus)
    
    solmu = 1 + left_value + right_value
   
    return (solmu)
    
def diff(node):
    count(node)
    return max(isoin_ero)
    
if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree =Node(left=None, right=Node(left=Node(left=None, right=None), right=Node(left=None, right=None)))
    print(diff(tree)) # 3