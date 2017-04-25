class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


def get_length(ll):
	# length == 1
	if ll.next == None:
		return 1
	
	length_ll = 0
	current_node = ll
	current_node2 = ll.next
	
	# Checks whether the linked list is circular
	while current_node != None and current_node != current_node2:
		current_node = current_node.next
		if current_node2 != None:
			current_node2 = current_node2.next
		if current_node2 != None:
			current_node2 = current_node2.next
		length_ll += 1
	
	# Return -1 if the linked list is circular
	if current_node == None:
		return length_ll
	else:
		return -1


def question5(ll, m):
	# Make sure ll is a Node
	if type(ll) != Node:
		return "Error: ll not a Node!"
	
	# Make sure m is an integer
	if type(m) != int:
		return "Error: m not an integer!"
	
	# Get the length of ll
	length_ll = get_length(ll)
	
	# Make sure ll is not circular
	if length_ll == -1:
		return "Error: circular linked list!"
	
	# Make sure m is less than or equal to the length of ll
	if length_ll < m:
		return "Error: m greater than the length of ll!"
	
	# Traverse to the last mth element
	current_node = ll
	for i in xrange(length_ll - m):
		current_node = current_node.next
	
	return current_node.data


"""
Test Case

n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n4.next = n5
n3.next = n4
n2.next = n3
n1.next = n2

print question5(123, 111) -> Error: ll not a Node
print question5(n1, 6) -> Error: m greater than the length of ll
print question5(n1, 3) -> 3
"""