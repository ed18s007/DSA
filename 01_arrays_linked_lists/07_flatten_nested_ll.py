class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return str(self.value)

class LinkedList:
	def __init__(self, head):
		self.head = head

	def append(self, value):
		if self.head is None:
			self.head = Node(value)
			return 
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
		current_node.next = Node(value)

	def flatten_deep(self):
		value_list = []
		current_node = self.head

		while current_node.next is not None:
			value_list.append(current_node.value)
			current_node = current_node.next
		value_list.append(current_node.value)
		return value_list

def merge(list1, list2):
	merged_list = []
	leng = len(list1) + len(list2)
	left, right = 0,0 
	for i in range(leng):
		if list1[left] <= list2[right]:
			merged_list.append(list1[left])
			left += 1
		else:
			merged_list.append(list2[right])
			right += 1
	return merged_list

class NestedLinkedList(LinkedList):
	def flatten(self):
		values = []
		for element in self.flatten_deep():
			values.append(element.flatten_deep())
		values = [item for sublist in values for item in sublist]
		values.sort()
		return values


linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

solution = nested_linked_list.flatten()
assert solution == [1,2,3,4,5]