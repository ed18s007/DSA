# 1. `enqueue`  - adds data to the back of the queue
# 2. `dequeue`  - removes data from the front of the queue
# 3. `front`    - returns the element at the front of the queue
# 4. `size`     - returns the number of elements present in the queue
# 5. `is_empty` - returns `True` if there are no elements in the queue, and `False` otherwise
# 6. `_handle_full_capacity` - increases the capacity of the array, for cases in which the queue would otherwise overflow

# Also, if the queue is empty, `dequeue` and `front` operations should return `None`.

class Queue:
	def __init__(self, queue_size : int= 10):
		self.arr = [0 for _ in range(queue_size)]
		self.front_index = -1
		self.next_index = 0
		self.queue_size = 0

	def enqueue(self, value):
		if self.queue_size == len(self.arr):
			self._handle_queue_capacity_full()
		self.arr[self.next_index] = value
		self.queue_size += 1
		self.next_index = (self.next_index + 1) % len(self.arr)
		if self.front_index == -1:
			self.front_index = 0

	def size(self):
		return self.queue_size

	def is_empty(self):
		return self.queue_size == 0

	def front(self):
		if self.front_index == -1:
			return None
		else:
			return self.arr[self.front_index]

	def dequeue(self):
		if self.is_empty():
			self.front_index = -1
			self.next_index = 0
			return None
		else:
			value = self.arr[self.front_index]
			self.front_index = (self.front_index + 1) %len(self.arr)
			self.queue_size -= 1
			return value

    # TODO: Add the _handle_queue_capacity_full method
	def _handle_queue_capacity_full(self):
		old_arr = self.arr
		self.arr = [0 for _ in range(2 * len(old_arr))]

		index = 0

		# copy all elements from front of queue (front-index) until end
		for i in range(self.front_index, len(old_arr)):
			self.arr[index] = old_arr[i]
			index += 1

		# case: when front-index is ahead of next index
		for i in range(0, self.front_index):
			self.arr[index] = old_arr[i]
			index += 1

		# reset pointers
		self.front_index = 0
		self.next_index = index

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