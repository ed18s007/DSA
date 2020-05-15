def hash_function(string):
	hash_code = 0
	for character in string:
		hash_code += ord(character) 
	return hash_code

hash_code_1 = hash_function("abcd")
print(hash_code_1)

class Linked_list_node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

class HashMap:
	def __init__(self, initial_size = 10):
		self.bucket_array = [None for _ in range(initial_size)]
		self.p = 31 #or 37
		self.num_entries = 0
		self.load_factor = 0.7

	def put(self, key, value):
		bucket_index = self.get_bucket_index(key)
		new_node = Linked_list_node(key, value)
		head = self.bucket_array[bucket_index]

		while head is not None:
			if head.key == key:
				head.value = value
				return
			head = head.next

		head = self.bucket_array[bucket_index]
		new_node.next = head
		self.bucket_array[bucket_index] = new_node
		self.num_entries += 1

		current_load_factor = self.num_entries/ len(self.bucket_array)
		if current_load_factor > self.load_factor:
			self.num_entries = 0
			self._rehash()

	def get(self, key):
		bucket_index = self.get_hash_code(key)
		head = self.bucket_array[bucket_index]
		while head is not None:
			if head.key == key:
				return head.value
			head = head.next
		return None 

	def get_bucket_index(self, key):
		bucket_index = self.get_hash_code(key)
		return bucket_index

	def get_hash_code(self, key):
		key = str(key)
		num_buckets = len(self.bucket_array)
		current_coefficient = 1
		hash_code = 0
		for character in key:
			hash_code += ord(character)*current_coefficient
			hash_code = hash_code % num_buckets
			current_coefficient *= self.p 
			current_coefficient = current_coefficient % num_buckets

		return hash_code #% num_buckets

	def size(self):
		return self.num_entries

	def _rehash(self):
		old_num_buckets = len(self.bucket_array)
		old_bucket_array = self.bucket_array
		num_buckets = 2* old_num_buckets
		self.bucket_array = [None for _ in range(num_buckets)]

		for head in old_bucket_array:
			while  head is not None:
				key = head.key
				value = head.value
				self.put(key, value)
				head = head.next

	def delete(self, key):
		bucket_index = self.get_bucket_index(key)
		head = self.bucket_array[bucket_index]

		previous = None
		while head is not None:
			if head.key == key:
				if previous is None:
					self.bucket_array[get_bucket_index] = head.next
				else:
					previous.next = head.next
				self.num_entries -= 1
				return 
			else:
				previous = head
				head = head.next

hash_map = HashMap()
bucket_index = hash_map.get_bucket_index("355")
print(bucket_index)

bucket_index = hash_map.get_bucket_index("1095")
print(bucket_index)
print("bef")
hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))

hash_map.delete("one")

print(hash_map.get("one"))
print(hash_map.size())