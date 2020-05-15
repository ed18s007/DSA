def longest_consecutive_subsequence(input_list):
	index_dict = dict()
	for index, element in enumerate(input_list):
		index_dict[element] = [index]
		if (element-1) in index_dict:
			index_dict[element].insert(0, index_dict[element - 1][0])
			index_dict[element - 1].append(index)
			
		if (element + 1) in index_dict:
			index_dict[element].append(index_dict[element + 1][0])
			index_dict[element + 1].insert(0, index)

	print("ind",index_dict)

longest_consecutive_subsequence([5, 4, 7, 6, 10, 1, 3, 55, 2])