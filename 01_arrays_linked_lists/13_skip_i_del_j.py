class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def skip_i_del_j(head, i, j):
	current_node = head
	skip_node = head
	if current_node is None:
		return
	while current_node:
		for x in range(i-1):
			if current_node.next:
				current_node = current_node.next
				skip_node = skip_node.next
		for y in range(j):
			if skip_node.next:
				skip_node = skip_node.next
		if skip_node.next:
			current_node.next = skip_node.next
			current_node = current_node.next
			skip_node = current_node
		else:
			current_node.next = None
			return head
	return head

def create_linked_list(arr):
	if len(arr)==0:
		return None
	head = Node(arr[0])
	tail = head
	for value in arr[1:]:
		tail.next = Node(value)
		tail = tail.next
	return head

def print_linked_list(head):
	while head:
		print(head.value, end=' ')
		head = head.next
	print()

def to_list(head):
	soln = []
	while head:
		soln.append(head.value)
		head = head.next
	return soln

def test_function(test_case):
	head = test_case[0]
	i = test_case[1]
	j = test_case[2]
	solution = test_case[3]

	temp = skip_i_del_j(head, i, j)
	soln_list = to_list(temp)
	print(soln_list)
	print(solution)
	try:
		for index in range(len(solution)):
			if soln_list[index] != solution[index]:
				print("Fail")
				return
		print("Pass")
	except Exception as e:
		print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)
