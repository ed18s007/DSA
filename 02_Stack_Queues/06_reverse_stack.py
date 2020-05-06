class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.head = None
		self.num_elements = 0

	def size(self):
		return self.num_elements

	def is_empty(self):
		return self.num_elements==0

	def push(self, element):
		if self.head is None:
			self.head = Node(element)
		else:
			new_node = Node(element)
			new_node.next = self.head
			self.head = new_node
		self.num_elements += 1

	def pop(self):
		if self.head is None:
			return None 
		else:
			value = self.head.value
			self.head = self.head.next
			self.num_elements -= 1
		return value

	def top(self):
		if self.head is None:
			return None
		else:
			return self.head.value

	def to_list(self):
		stack_ls = []
		current_node = self.head
		while current_node:
			stack_ls.append(current_node.value)
			current_node = current_node.next
		return stack_ls

def reverse_stack(stack):
	inv_stack = Stack()
	while stack.top() is not None:
		inv_stack.push(stack.pop())
	return inv_stack

def test_function(test_case):
	stack = Stack()
	for num in test_case:
		stack.push(num)
	print(stack.to_list())

	rev_stack = reverse_stack(stack)
	print(rev_stack.to_list())

	# index = 0
	# while not stack.is_empty():
	# 	popped = stack.pop()
	# 	if popped != test_case[index]:
	# 		print("Fail")
	# 		return 
	# 	else:
	# 		index += 1
	# print("Pass")

test_case_1 = [1,2,3,4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)