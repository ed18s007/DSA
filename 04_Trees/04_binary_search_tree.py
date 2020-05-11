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


class Tree:
	def __init__(self):
		self.root = None

	def set_root(self, value):
		self.root = Node(value)

	def get_root(self):
		return self.root

	def compare(self, node, new_node):
		"""
		0 new_node = node
		-1 new_node < node
		1 new_node > node
		"""
		if new_node.get_value() == node.get_value():
			return 0 
		elif new_node.get_value() < node.get_value():
			return -1 
		else:
			return 1

	def insert_with_loop(self, new_value):
		current_node = self.root

		if current_node is None:
			self.set_root(value= new_value)

		else:
			new_node = Node(new_value)
			node_inserted = False

			while not node_inserted:
				comparison = self.compare(current_node, new_node)

				if comparison == 0:
					current_node.set_value(new_node)
					node_inserted = True

				elif comparison < 0:
					if current_node.has_left_child():
						current_node = current_node.get_left_child()
					else:
						current_node.set_left_child(new_node)
						node_inserted = True

				else:
					if current_node.has_right_child():
						current_node = current_node.get_right_child()
					else:
						current_node.set_right_child(new_node)
						node_inserted = True

	def insert_with_recursion(self, value):
		current_node = self.root 

		if current_node is None:
			self.set_root(value=value)

		else:
			self._insert_with_recursion_rec(current_node, value)

	def _insert_with_recursion_rec(self, current_node, value):
		new_node = Node(value)
		comparison = self.compare(current_node, new_node)

		if comparison ==0:
			current_node.set_value(new_node)
		elif comparison <0:
			if current_node.has_left_child():
				self._insert_with_recursion_rec(current_node.get_left_child(), value)
			else:
				current_node.set_left_child(new_node)
		else:
			if current_node.has_right_child():
				self._insert_with_recursion_rec(current_node.get_right_child(), value)
			else:
				current_node.set_right_child(new_node)

	def search(self, value):
		node = self.root

		if node is None:
			return None

		else:
			return self._search_rec(node, value)

	def _search_rec(self, node, value):
		new_node = Node(value)
		comparison = self.compare(node, new_node)

		if comparison == 0:
			return True
		elif comparison < 0:  # Left side
			if node.has_left_child():
				return self._search_rec(node=node.get_left_child(), value=value)
			else:
				return False
		else:
			if node.has_right_child():
				return self._search_rec(node=node.get_left_child(), value=value)
			else:
				return False

	def __repr__(self):
		level = 0
		q = Queue()
		visit_order = list()
		node = self.get_root()
		q.enq((node, level))
		while (len(q) > 0):
			node, level = q.deq()
			if node == None:
				visit_order.append(("<empty>", level))
				continue
			visit_order.append((node, level))
			if node.has_left_child():
				q.enq((node.get_left_child(), level + 1))
			else:
				q.enq((None, level + 1))

			if node.has_right_child():
				q.enq((node.get_right_child(), level + 1))
			else:
				q.enq((None, level + 1))

		s = "Tree\n"
		previous_level = -1
		for i in range(len(visit_order)):
			node, level = visit_order[i]
			if level == previous_level:
				s += " | " + str(node)
			else:
				s += "\n" + str(node)
				previous_level = level

		return s

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)

# print(tree.search(6))

# print(f"""
# search for 8: {tree.search(8)}
# search for 2: {tree.search(2)}
# """)