from queue import Queue 

class BinaryTreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left =None 
		self.right = None

def diameter_of_binary_tree(root):
	if root is None:
		return 0

	else:
		return sum(_diameter_binary_rec(root))

def _diameter_binary_rec(root):
	current_node = root
	left_depth = 0
	right_depth = 0

	if root is None:
		return 0 

	if current_node.left is not None:
		left_depth = max(_diameter_binary_rec(current_node.left)) + 1

	if current_node.right is not None:
		right_depth = max(_diameter_binary_rec(current_node.right)) + 1

	return [left_depth, right_depth]

def convert_arr_to_binary_tree(arr):
	index = 0
	length = len(arr)

	if length <= 0 or arr[0] == -1:
		return None 

	root = BinaryTreeNode(arr[index])
	index += 1
	queue = Queue()
	queue.put(root)

	while not queue.empty():
		current_node = queue.get()
		left_child = arr[index]
		index += 1

		if left_child is not None:
			left_node = BinaryTreeNode(left_child)
			current_node.left = left_node
			queue.put(left_node)

		right_child = arr[index]
		index += 1

		if right_child is not None:
			right_node = BinaryTreeNode(right_child)
			current_node.right = right_node
			queue.put(right_node)
	return root 

def diameter_of_binary_tree(root):
	return diameter_of_binary_tree_func(root)[1]

def diameter_of_binary_tree_func(root):
	if root is None:
		return 0, 0

	left_height, left_diameter = diameter_of_binary_tree_func(root.left)
	right_height, right_diameter = diameter_of_binary_tree_func(root.right)

	current_height = max(left_height, right_height) + 1
	height_diameter = left_height + right_height
	current_diameter = max(left_diameter, right_diameter, height_diameter)

	return current_height, current_diameter

def test_function(test_case):
	arr = test_case[0]
	solution = test_case[1]
	root = convert_arr_to_binary_tree(arr)
	output = diameter_of_binary_tree(root)
	print(output)
	if output==solution:
		print("Pass")
	else:
		print("Fail")

arr = [1,2,3,4,5,None,None,None,None,None,None]
solution = 3
test_case = [arr, solution]
test_function(test_case)