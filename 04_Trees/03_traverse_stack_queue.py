from collections import deque 
import copy 

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def set_value(self, value):
		self.value = value

	def get_value(self):
		return self.value

	def set_left_child(self, left):
		self.left = left 

	def set_right_child(self, right):
		self.right = right 

	def get_left_child(self):
		return self.left 

	def get_right_child(self):
		return self.right

	def has_left_child(self):
		return self.left is not None

	def has_right_child(self):
		return self.right is not None

	def __repr__(self):
		return f"Node({self.get_value()})"

	def __str__(self):
		return f"Node({self.get_value()})"

class Tree:
	def __init__(self, value=None):
		self.root = Node(value)

	def get_root(self):
		return self.root

class Stack:
	def __init__(self):
		self.list = []

	def push(self, value):
		self.list.append(value)

	def pop(self):
		return self.list.pop()

	def top(self):
		if len(self.list)>0:
			return self.list[-1]
		else:
			return None

	def is_empty(self):
		return len(self.list)==0

	def __repr__(self):
		if len(self.list) > 0:
			s = "<top of stack> \n___________\n"
			s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
			s += "\n_________________\n<bottom of stack>"
			return s
		else:
			return "<stack is empty>"

class State(object):
	def __init__(self, node):
		self.node = node 
		self.visited_left = False
		self.visited_right = False

	def get_node(self):
		return self.node 

	def get_visited_left(self):
		return self.visited_left

	def get_visited_right(self):
		return self.visited_right

	def set_visited_left(self):
		self.visited_left = True

	def set_visited_right(self):
		self.visited_right = True

	def __repr__(self):
		s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
	"""
		return s 

def pre_order_with_stack(tree, debug_mode=False):
	visit_order = []
	stack = Stack()
	node = tree.get_root()
	visit_order.append(node.get_value())
	state = State(node)
	stack.push(state)
	stack.push(state)
	count = 0
	while (node):
		if debug_mode:
			print(f"""
loop count: {count}
current node: {node}
stack: {stack}
""")
		count += 1
		if node.has_left_child() and not state.get_visited_left():
			state.set_visited_left()
			node = node.get_left_child()
			visit_order.append(node.get_value())
			state = State(node)
			stack.push(state)

		elif node.has_right_child() and not state.get_visited_right():
			state.set_visited_right()
			node = node.get_right_child()
			visit_order.append(node.get_value())
			state = State(node)
			stack.push(state)

		else:
			stack.pop()
			if not stack.is_empty():
				state = stack.top()
				node = state.get_node()
			else:
				node = None
	if debug_mode:
		print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
	""")
	return visit_order

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
print(pre_order_with_stack(tree, debug_mode=False))


class Queue(object):
	def __init__(self):
		self.q = deque()

	def enq(self, value):
		self.q.appendleft(value)

	def deq(self):
		if len(self.q) > 0:
			return self.q.pop()
		else:
			return None

	def __len__(self):
		return len(self.q)

	def __repr__(self):
		if len(self.q) > 0:
			s = "<enque here \n_____________\n"
			s += "\n____________\n".join(str(item) for item in self.q)
			s += "\n_____________\n <deque here>"
			return s 
		else:
			return "<queue is empty>"

def bfs(tree):
	q = Queue()
	visit_order = list()
	node = tree.get_root()
	q.enq(node)
	while(len(q) > 0):
		node = q.deq()
		visit_order.append(node)
		if node.has_left_child():
			q.enq(node.get_left_child())
		if node.has_right_child():
			q.enq(node.get_right_child())

	return visit_order

print(bfs(tree))