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
		return self.num_elements == 0

	def push(self, element):
		if self.head is None:
			self.head = Node(element)
		else:
			new_node = Node(element)
			new_node.next = self.head
			self.head = new_node
		self.num_elements += 1

	def pop(self):
		if self.is_empty():
			return None
		else:
			value = self.head.value
			self.head = self.head.next
			self.num_elements -= 1
			return value

	def top(self):
		if self.head is None:
			return None
		return self.head.value

def evaluate_post_fix(input_list):
	stack = Stack()

	for element in input_list:
		if element in ["+", "-", "*", "/"]:
			element_2 = stack.pop()
			element_1 = stack.pop()
			stack.push(str(int(eval(element_1+element+ element_2))))
		else:
			stack.push(element)
	return stack.pop()

def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    if int(output) == int(test_case[1]):
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)