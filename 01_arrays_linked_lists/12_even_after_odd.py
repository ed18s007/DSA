class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def create_linked_list(arr):
	if len(arr)==0:
		return None
	head = Node(arr[0])
	tail = head 
	for data in arr[1:]:
		tail.next = Node(data)
		tail = tail.next
	return head

def print_linked_list(head):
	current_node = head
	while current_node:
		print(current_node.value)
		current_node = current_node.next

def even_after_odd(head):
	even_linked_list = None
	odd_linked_list = None
	linked_list_end = False

	current_node = head
	while not linked_list_end:
		if current_node.value%2 == 0:
			if even_linked_list is None:
				even_linked_list = Node(current_node.value)
			else:
				even_tail = even_linked_list
				while even_tail.next:
					even_tail = even_tail.next
				even_tail.next = Node(current_node.value)
		else:
			if odd_linked_list is None:
				odd_linked_list = Node(current_node.value)
			else:
				odd_tail = odd_linked_list
				while odd_tail.next:
					odd_tail = odd_tail.next
				odd_tail.next = Node(current_node.value)

		linked_list_end = current_node.next is None
		current_node = current_node.next

	if odd_linked_list is None:
		return even_linked_list

	position_tail = odd_linked_list
	while position_tail.next:  # Moving to the end of the list
		position_tail = position_tail.next
	position_tail.next = even_linked_list

	return odd_linked_list

def test_function(test_case):
	head = test_case[0]
	solution = test_case[1]

	node_tracker = dict({})
	node_tracker['nodes'] = list()
	temp = head
	while temp:
		node_tracker['nodes'].append(temp)
		temp = temp.next

	head = even_after_odd(head)    
	print_linked_list(head)
	print(solution)


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

