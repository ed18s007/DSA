wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
print("wakeup_times\n",wakeup_times)

def bubble_sort_1(input_list):
	for i in range(len(input_list)):
		swap = 0
		for j in range(len(input_list)-1):
			if input_list[j] > input_list[j + 1]:
				swap += 1
				input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
		if swap == 0:
			return input_list
	return input_list

print(bubble_sort_1(wakeup_times))

def bubble_sort_2(input_list):
	l = len(input_list)
	for i in range(len(input_list)):
		for j in range(l-1):
			if input_list[j] > input_list[j + 1]:
				input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
		l -= 1
	return input_list

print(bubble_sort_1(wakeup_times))

def is_time_bigger(input_list):
	l = len(input_list)
	for i in range(len(input_list)):
		for j in range(l-1):
			if input_list[j][0] < input_list[j+1][0]:
				input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
				continue
			if (input_list[j][0] == input_list[j+1][0]) and (input_list[j][1] < input_list[j+1][1]):
				input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
		l -= 1
	return input_list

sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
print("before")
print(sleep_times)
print("after")
print(is_time_bigger(sleep_times))
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")

print ([(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)])
