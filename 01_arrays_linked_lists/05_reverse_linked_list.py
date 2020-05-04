class Node(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = Node(value)

	def to_list(self):
		out = []
		node = self.head
		while node:
			out.append(node.value)
			node = node.next
		return out

	def __iter__(self):
		current_node = self.head
		while current_node:
			yield current_node.value
			current_node = current_node.next

	def __repr__(self):
		return str([v for v in self])

def insert_at_head(linked_list, value):
	current_node = linked_list.head
	linked_list.head = Node(value)
	linked_list.head.next = current_node
	return linked_list

def reverse(linked_list):
	ll_node = linked_list.head
	reversed_ll = LinkedList()
	while ll_node:
		value = ll_node.value
		reversed_ll = insert_at_head(reversed_ll, value)
		ll_node = ll_node.next
	return reversed_ll

llist = LinkedList()

for value in [2,4,6,8,0,2]:
	llist.append(value)

flipped = reverse(llist)

print(list(flipped))
is_correct = list(flipped) == list([2,0,8,6,4,2]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")

