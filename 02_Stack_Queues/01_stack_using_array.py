class Stack(object):
	def __init__(self, initial_size=10):
		self.arr = [0 for _ in range(initial_size)]
		self.next_index = 0
		self.num_elements = 0

	def push(self, element):
		if self.next_index == len(self.arr):
			print("Out of Space. Increasing array capacity!")
			self._handle_stack_capacity_full()
		self.arr[self.next_index] = element
		self.next_index += 1
		self.num_elements += 1

	def _handle_stack_capacity_full(self):
		old_arr = self.arr
		self.arr = [0 for  _ in range(2*len(old_arr))]
		for index, element in enumerate(old_arr):
			self.arr[index] = element

	def size(self):
		return self.next_index 

	def is_empty(self):
		return self.next_index==0 

	def pop(self):
		if self.is_empty:
			return None
		else:
			self.next_index -= 1
			self.num_elements -= 1
			return self.arr[self.next_index]


foo = Stack()
foo.push(1)
foo.push(2)
print(foo.arr) 
print(foo.pop())
print(foo.arr) 