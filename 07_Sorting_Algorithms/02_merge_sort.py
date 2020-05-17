def mergesort(input_list):
	if len(input_list) <= 1:
		return input_list
	else:
		ln = int(len(input_list)/2)
		left_ls = mergesort(input_list[:ln])
		right_ls = mergesort(input_list[ln:])
		return merge(left_ls, right_ls)

def merge(inp_ls_1, inp_ls_2):
	len1, len2 = len(inp_ls_1), len(inp_ls_2)
	if len1 == 0:
		return inp_ls_2
	if len2 == 0:
		return inp_ls_1
	merged_list = []
	idx_1, idx_2 = 0, 0
	for i in range(len1 + len2):
		if inp_ls_1[idx_1] < inp_ls_2[idx_2]:
			merged_list.append(inp_ls_1[idx_1])
			idx_1 += 1
			if idx_1 == len1:
				merged_list.extend(inp_ls_2[idx_2:])
				return merged_list
		else:
			merged_list.append(inp_ls_2[idx_2])
			idx_2 += 1
			if idx_2 == len2:
				merged_list.extend(inp_ls_1[idx_1:])
				return merged_list
	return merged_list

print(mergesort([1,5,2,7,4]))

test_list_1 = [8, 3, 1, 97, 98, 99, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99, 1,5,2,7,4]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))