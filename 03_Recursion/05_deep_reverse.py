# def deep_reverse(inp_list):
# 	print(inp_list)
# 	if len(inp_list) == 0:
# 		return None
# 	elif len(inp_list) == 1:
# 		if type(inp_list[0])  is not list :
# 			return inp_list
# 		else:
# 			return [deep_reverse(inp_list[0])]
# 	else:
# 		if type(inp_list[len(inp_list) - 1]) is not list :
# 			return [inp_list[len(inp_list) - 1]]+ deep_reverse(inp_list[:len(inp_list)-2])
# 		else:
# 			return [deep_reverse(inp_list[len(inp_list) - 1])] + deep_reverse(inp_list[:len(inp_list)-2])

def deep_reverse(arr):
	if type(arr) is not list:
		return arr
	else:
		results = []
		arr = arr[::-1]
		for element in arr:
			results.append(deep_reverse(element))
		return results

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)