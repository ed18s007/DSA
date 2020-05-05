def list_to_string(input_list : list) -> str:
	string = str()
	for i in input_list:
		string += str(i)
	return string

def string_add_one(string : str) -> str:
	number = int(string)
	number += 1
	return str(number)

def string_to_list(string: str) -> list:
	return [int(char) for char in string]

def add_one(inp_list: list) -> list :
	return string_to_list(string_add_one(list_to_string(inp_list)))

def test_function(test_case):
	arr = test_case[0]
	solution = test_case[1]

	output = add_one(arr)
	for index, element in enumerate(output):
		if element != solution[index]:
			print("Fail")
			return
	print("Pass")

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)
 
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)