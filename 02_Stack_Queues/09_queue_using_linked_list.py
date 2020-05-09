class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Queue(object):
	def __init__(self):
		self.head = None
		self.num_elements = 0
		self.tail = None

	def enqueue(self, element):
		if self.head is None:
			self.head = Node(element)
			self.tail = self.head
			self.num_elements += 1
		else:
			self.tail.next = Node(element)
			self.tail = self.tail.next
			self.num_elements += 1

	def size(self):
		return self.num_elements

	def is_empty(self):
		return self.num_elements == 0

	def dequeue(self):
		if self.head is None:
			return None
		else:
			value = self.head.value
			self.head = self.head.next
			self.num_elements -= 1
			return value

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")