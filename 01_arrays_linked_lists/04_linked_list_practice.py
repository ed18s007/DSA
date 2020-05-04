class Node(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def prepend(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			current_node = Node(value)
			current_node.next = self.head
			self.head = current_node

	def prepend_2(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			previous_node = self.head
			self.head = Node(value)
			self.head.next = previous_node

	def append(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = Node(value)

	def search(self, value):
		if self.head is None:
			return None
		else:
			current_node = self.head
			while current_node.next:
				if current_node.value == value:
					return current_node
				current_node = current_node.next

	def remove(self, value):
		previous_node = None
		current_node = self.head
		while current_node:
			if current_node.value == value:
				if previous_node == None:
					self.head = current_node.next
					break
				else:
					previous_node.next = current_node.next
					break
			previous_node = current_node
			current_node = current_node.next

	def pop(self):
		current_node = self.head.value
		self.head = self.head.next
		return current_node

	def insert(self, value, pos):
		current_node = self.head
		if pos == 0:
			self.head = Node(value)
			self.head.next = current_node
		elif pos>= self.size():
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			new_node = Node(value)
			current_node.next = new_node
		else:
			while pos>0:
				pos -= 1
				previous_node = current_node
				current_node = current_node.next
			new_node = Node(value)
			previous_node.next = new_node
			new_node.next = current_node

	def size(self):
		""" Return the size or length of the linked list. """
		position_tail = self.head
		length = 0

		while position_tail is not None:
			position_tail = position_tail.next
			length += 1

		return length

	def to_list(self):
		out = []
		node = self.head
		while node:
			out.append(node.value)
			node = node.next
		return out


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
# assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"