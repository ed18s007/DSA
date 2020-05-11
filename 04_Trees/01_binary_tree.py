class Node(object):
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def has_left_child(self):
		return self.left is not None

	def has_right_child(self):
		return self.right is not None

	def set_left_child(self, node):
		self.left = node

	def get_left_child(self):
		return self.left

	def set_right_child(self, node):
		self.right = node

	def get_right_child(self):
		return self.right 

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"""
node 0: {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
""")

class Tree:
	def __init__(self, value = None):
		self.root = Node(value)

	def get_root(self):
		return self.root