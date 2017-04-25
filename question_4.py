"""
Explanation

We will traverse through the tree using the top-down approach and with the BST
properties, the least common ancestor between two nodes will be the first node we
meet with the value between n1 and n2. We will go left if the current node is greater
than both n1 and n2, right if the current node is less than both n1 and n2, else
the node is the least common ancestor.
 
Worse case is O(log(n))
Time complexity is O(log(n))
Space complexity is O(1)
"""


class Tree_Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BST_search(r, n):
    # Search if n is in the tree
    current_node = r
    while current_node.left is not None or current_node.right is not None:
        # Go left if current node is greater than n
        if current_node.data > n:
            # Make sure left node exist
            if current_node.left is not None:
                current_node = current_node.left
            else:
                return False
        # Go right if current node is less than n
        elif current_node.data < n:
            # Make sure right node exist
            if current_node.right is not None:
                current_node = current_node.right
            else:
                return False
        # Current node is n, return True
        else:
            return True
    # Check if n is in the lowest level
    if current_node.data == n:
        return True
    else:
        return False


def question4(r, n1, n2):
    # Make sure r is a tree node
    if not isinstance(r, Tree_Node):
        return "Error: r not Tree_Node"

    # Make sure n1 and n2 are integers
    if not isinstance(n1, int):
        return "Error: n1 not integer"
    if not isinstance(n2, int):
        return "Error: n2 not integer"

    # Make sure n1 and n2 in the tree
    if not BST_search(r, n1):
        return "Error: n1 not in the tree"
    if not BST_search(r, n2):
        return "Error: n2 not in the tree"

    current_node = r
    while current_node.left is not None or current_node.right is not None:
        # If both vales are less than the current node, we go to the left
        if current_node.data > n1 and current_node.data > n2:
            current_node = current_node.left
        # If both vales are greater than the current node, we go to the right
        elif current_node.data < n1 and current_node.data < n2:
            current_node = current_node.right
        # We find the answer, return it
        else:
            return current_node.data
    # n1 equal to n2 at the lowest level
    return current_node.data


"""
Test Cases

n1, n3, n5, n7 = Tree_Node(1), Tree_Node(3), Tree_Node(5), Tree_Node(7)
n9, n11, n13, n15 = Tree_Node(9), Tree_Node(11), Tree_Node(13), Tree_Node(15)
n2, n6, n10, n14 = Tree_Node(2), Tree_Node(6), Tree_Node(10), Tree_Node(14)
n2.left, n2.right = n1, n3
n6.left, n6.right = n5, n7
n10.left, n10.right = n9, n11
n14.left, n14.right = n13, n15
n4, n12 = Tree_Node(4), Tree_Node(12)
n4.left, n4.right = n2, n6
n12.left, n12.right = n10, n14
r = Tree_Node(8)
r.left, r.right = n4, n12

print question4(123, 111, 111) --> Error: r not Tree_Node
print question4(r, -1, 5) --> Error: n1 not in the tree
print question4(r, 8, 1) -> 8
"""
