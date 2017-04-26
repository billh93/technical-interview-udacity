"""
Explanation

We will traverse through the tree using the top-down approach and with the BST
properties, the least common ancestor between two nodes will be the first node we
meet with the value between n1 and n2. We will go left if the current node is greater
than both n1 and n2, right if the current node is less than both n1 and n2, else
the node is the least common ancestor.

Worse case is O(n)
Time complexity is O(n)
Space complexity is O(1)
"""

global head
head = None


class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# Function to insert a new node at the beginning
def push_right(node, new_data):
    new_node = Node(new_data)
    node.right = new_node
    return new_node


# Function to insert a new node at the beginning
def push_left(node, new_data):
    new_node = Node(new_data)
    node.left = new_node
    return new_node


# Function to find LCA of n1 and n2. The function assumes that both n1 and n2 are present in BST
def lca(head, n1, n2):
    # Base Case
    if head is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA lies in left
    if head.data > n1 and head.data > n2:
        return lca(head.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA lies in right
    if head.data < n1 and head.data < n2:
        return lca(head.right, n1, n2)

    return head.data


def question4(mat, root, n1, n2):
    global head
    # Make BST
    head = Node(root)
    head.left, head.right = None, None
    node_value = 0
    node_list = []

    if not isinstance(mat, list):
        return "Error: mat is not a tree node"
    # Makes sure n1 and n2 are integers
    if not isinstance(n1, int):
        return "Error: n1 is not an integer"
    if not isinstance(n2, int):
        return "Error: n2 is not an integer"

    for elem in mat[root]:
        if elem:
            if node_value > root:
                node_list.append(push_right(head, node_value))
            else:
                node_list.append(push_left(head, node_value))
        node_value += 1

    tmp_node = node_list.pop(0)
    while tmp_node is not None:
        node_value = 0
        for elem in mat[tmp_node.data]:
            if elem:
                if node_value > tmp_node.data:
                    node_list.append(push_right(tmp_node, node_value))
                else:
                    node_list.append(push_left(tmp_node, node_value))
            node_value += 1
        if node_list == []:
            break
        else:
            tmp_node = node_list.pop(0)
            
    return lca(head, n1, n2)


"""
Test Cases

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]], 6, "s", 3) --> Error: n1 is not an integer
print question4(3, 3, 1, 4) --> Error: mat is not a tree node
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]], 3, 1, 4) --> 3
"""
