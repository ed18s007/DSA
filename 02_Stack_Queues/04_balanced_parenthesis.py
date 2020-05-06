class Stack:
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def is_empty(self):
		return self.size() == 0

	def push(self, element):
		self.items.append(element)

	def pop(self):
		if self.is_empty():
			return None
		else:
			return self.items.pop()

def equation_checker(equation):
	foo = Stack()
	for char in equation:
		if char == "(":
			foo.push(char)
		elif char == ")":
			if foo.pop() == None:
				return False
	return foo.is_empty()

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
