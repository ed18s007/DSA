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

	def __repr__(self):
		return f"Node({self.get_value()})"

	def __str__(self):
		return f"Node({self.get_value()})"

class Tree:
	def __init__(self, value= None):
		self.root = Node(value)

	def get_root(self):
		return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("orange"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# Depth First pre-order traversal with Stack

class Stack:
	def __init__(self):
		self.list = list()

	def push(self, value):
		self.list.append(value)

	def pop(self):
		return self.list.pop()

	def top(self):
		if len(self.list) > 0:
			return self.list[-1]
		else:
			return None

	def is_empty(self):
		return len(self.list) == 0

	def __repr__(self):
		if len(self.list) > 0:
			s = "<top of stack>\n________\n"
			s += "\n_______\n".join([str(item) for item in self.list[::-1]])
			s += "\n_______\n<bottom of stack>"
			return s 
		else:
			return "<stack is empty>"


def pre_order(tree):
	visit_order = list()

	def traverse(node):
		if node:
			visit_order.append(node.get_value())

			traverse(node.get_left_child())

			traverse(node.get_right_child())
	traverse(tree.get_root())

	return visit_order

print(pre_order(tree))

def in_order(tree):
	visit_order = list()

	def traverse(node):
		if node:
			traverse(node.get_left_child())

			visit_order.append(node.get_value())

			traverse(node.get_right_child())	

	traverse(tree.get_root())

	return visit_order

print(in_order(tree))

def post_order(tree):
	visit_order = list()

	def traverse(node):
		if node:
			traverse(node.get_left_child())

			traverse(node.get_right_child())

			visit_order.append(node.get_value())

	traverse(tree.get_root())

	return visit_order

print(post_order(tree))

def bfs(tree):
	visit_order = list()
	visit_order.append(tree.get_root().value)

	def traverse(node):
		if node:
			if node.has_left_child():
				visit_order.append(node.get_left_child().get_value())

			if node.has_right_child():
				visit_order.append(node.get_right_child().get_value())
			
			if node.has_left_child():
				traverse(node.get_left_child())

			if node.has_right_child():
				traverse(node.get_right_child())

	traverse(tree.get_root())

	return visit_order



tree = Tree("1")
tree.get_root().set_left_child(Node("2"))
tree.get_root().set_right_child(Node("3"))
tree.get_root().get_left_child().set_left_child(Node("4"))
tree.get_root().get_left_child().set_right_child(Node("5"))

print(in_order(tree))
print(pre_order(tree))
print(post_order(tree))
print(bfs(tree))

# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1

# stack = Stack()
# stack.push("apple")
# stack.push("banana")
# stack.push("cherry")
# stack.push("dates")
# print(stack.pop())
# print("\n")
# print(stack)

