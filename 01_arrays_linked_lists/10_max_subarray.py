def sum_list(input_list: list) -> int:
	result = 0
	for i in input_list:
		result += i
	return result

def sub_list_generator(input_list: list) -> list:
	list_of_lists = []
	list_max_position = len(input_list) + 1
	for initiial_position in range(list_max_position):
		for final_position in range(initiial_position + 1, list_max_position):
			list_of_lists.append(input_list[initiial_position:final_position])
	return list_of_lists

def max_sum_subarray(input_list: list) -> int:
	max_val = -float("inf")
	list_of_lists = sub_list_generator(input_list)
	for lst in list_of_lists:
		list_added = sum_list(lst)
		if list_added > max_val:
			max_val = list_added
	return max_val

def test_function(test_case):
	arr = test_case[0]
	solution = test_case[1]
	output = max_sum_subarray(arr)
	print("Pass") if output==solution else print("Fail")


arr = [1,2,3,-4,6]
solution = 8
test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)