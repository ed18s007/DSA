class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def swap_nodes(head, left_index, right_index):
    # Values to swap
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            left_data = node.value

        if position == right_index:
            right_data = node.value
        position += 1
        node = node.next
    
    # Swapping values
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            node.value = right_data

        if position == right_index:
            node.value = left_data
        position += 1
        node = node.next

    return head
def test_function(test_case):
	head = test_case[0]
	print_linked_list(head)
	left_index = test_case[1]
	right_index = test_case[2]
	updated_head = swap_nodes(head, left_index, right_index)
	print_linked_list(updated_head)


# helper functions for testing purpose
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
    while head:
        print(head.value, end=" ")
        head = head.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2 
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)


arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)