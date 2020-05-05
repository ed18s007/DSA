def nth_row_pascal(input_row: int) -> list:
	row = int(11**input_row)
	out = []
	num = row
	while num%10 != 0:
		out.append(num%10)
		num =int(num/10)
	print("out",out)
	return out

def test_function(test_case):
	n = test_case[0]
	solution = test_case[1]
	output = nth_row_pascal(n)
	print("Pass") if solution == output else print("Fail")

n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)