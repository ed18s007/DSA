def count_inversions(items):
    if len(items) <= 1:
        return items, 0

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    inversions_left = 0
    inversions_right = 0

    left, inversions_left = count_inversions(left)
    right, inversions_right = count_inversions(right)

    merged, inversions = merge(left, right)

    return merged, inversions_left + inversions_right + inversions

def merge(left, right):
    merged = []
    inversions = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            inversions += 1
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged, inversions
"""
def count_inversions(input_list):
	if len(input_list) <=1:
		return input_list, 0
	mid = len(input_list)//2
	left = input_list[:mid]
	right = input_list[mid:]

	left_inv, right_inv = 0,0
	left, left_inv = count_inversions(left)
	right, right_inv = count_inversions(right)

	merged, inv = merge(left, right)
	return merge, left_inv + right_inv + inv
	
def merge(left_ls, right_ls):
	if len(left_ls) == 0:
		return right_ls, 0
	if len(right_ls) == 0:
		return left_ls, 0
	idx_1, idx_2 , inv = 0, 0, 0
	merged_ls = []
	for i in range(len(left_ls) + len(right_ls)):
		if left_ls[idx_1] < right_ls[idx_2]:
			merged_ls.append(left_ls[idx_1])
			idx_1 += 1
			if idx_1 == len(left_ls) :
				merged_ls.extend(right_ls[idx_2:])
				return merged_ls, inv
			inv += 1
		else:
			merged_ls.append(right_ls[idx_2])
			idx_2 += 1
			if idx_2 == len(right_ls) :
				merged_ls.extend(left_ls[idx_1:])
				return merged_ls, inv
	return merged_ls, inv
"""
arr = [2, 5, 1, 3, 4]
print(count_inversions(arr))
