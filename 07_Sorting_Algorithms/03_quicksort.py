def quicksort(input_list):
	if len(input_list) <=1:
		return input_list

	elif len(input_list) == 2:
		if input_list[0] <= input_list[1]:
			return input_list
		else:
			return input_list[::-1]

	pivot_idx = len(input_list) - 1
	swap_idx = 0
	while swap_idx < pivot_idx:
		if input_list[swap_idx] > input_list[pivot_idx]:
			input_list[swap_idx], input_list[pivot_idx - 1], input_list[pivot_idx] = input_list[pivot_idx - 1], input_list[pivot_idx], input_list[swap_idx]
			pivot_idx -= 1
		else:
			swap_idx += 1

	return quicksort(input_list[:pivot_idx]) + quicksort(input_list[pivot_idx:])

wakeup_times = [8,3,1,7,0,10,2]
print(wakeup_times)
print(quicksort(wakeup_times))
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
print("wakeup_times\n",wakeup_times)
print(quicksort(wakeup_times))
