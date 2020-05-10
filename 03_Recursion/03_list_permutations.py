
import copy

def permute(l):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list
    """

    if len(l) <= 1:
        return [l]

    elif len(l) == 2:
        return [l, l[::-1]]

    else:
        output = []
        current_level = l[0]
        prev_level = permute(l[1:])

        for element in prev_level:  # For each answer from previous level
            for pos in range(len(element) + 1):  # For each possible position to put this level value
                temp_list = []
                temp_element = element.copy()
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list.append(current_level)
                    else:
                        temp_list.append(temp_element.pop())
                output.append(temp_list)
        return output
        
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")

def permutations(l):
	if len(l)<=1:
		return [l]

	elif len(l) == 2:
		return [l, l[::-1]]

	else:
		output = []
		current_level = l[0]
		prev_level = permutations(l[1:])

		for element in prev_level:
			for pos in range(len(element) + 1):
				temp_list = ''
				temp_element = element
				for i in range(len(element) + 1):
					if pos == i:
						temp_list += current_level
					else:
						temp_list += temp_element[0]
						temp_element = temp_element[1:]
				output.append(temp_list)
		return output

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)