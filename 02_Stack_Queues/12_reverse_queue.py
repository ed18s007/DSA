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

def reverse_queue(queue):
	reversed_queue = Queue()
	remaining_num_elements = queue.num_elements

	while remaining_num_elements>0:
		tail_head = queue.head
		i_counter = 1

		while i_counter < remaining_num_elements:
			tail_head = tail_head.next
			i_counter += 1

		reversed_queue.enqueue(tail_head.value)
		remaining_num_elements -= 1
	return reversed_queue

def test_function(test_case):
    queue = Queue()
    
    for num in test_case:
        queue.enqueue(num)
    queue = reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)    

test_case_2 = [1]
test_function(test_case_2)
