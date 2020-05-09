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

def minimum_bracket_reversals(input_string):
	extra_movements = 0
	if input_string[0] == '}':
		input_string = '{' + input_string[1:]
		extra_movements += 1
	if input_string[len(input_string)-1] == '{':
		input_string = input_string[:len(input_string) - 1] + '}'
		extra_movements += 1

	prev_char = '-'

	if len(input_string) % 2 != 0 :
		return -1

	else:
		stack = Stack()
		for char in input_string:
			if prev_char + char == '{}' :
				_ = stack.pop()
				prev_char = stack.top()

				if stack.size() == 0:
					prev_char = '-'
			else:
				stack.push(char)
				prev_char = char 

	return int(stack.size()/2) + extra_movements

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    print(output, expected_output)
    
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case_1 = ["}}}}", 2]
test_function(test_case_1)

# test_case_2 = ["}}{{", 2]          
# test_function(test_case_2)

# test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
# test_function(test_case_1)

# test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
# test_function(test_case_2)

# test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
# test_function(test_case_3)
