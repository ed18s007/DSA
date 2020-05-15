def staircase(n):
	if n==0:
		return 1
	elif n < 0:
		return 0
	else:
		climb_ways = 0
		climb_ways += staircase(n-1)
		climb_ways += staircase(n-2)
		climb_ways += staircase(n-3)

		return climb_ways

def staircase_1(n):
	if n==1 or n==0:
		return 1
	elif n==2:
		return 2
	elif n==3:
		return 4
	return staircase_1(n-1) + staircase_1(n-2) + staircase_1(n-3)

def staircase_2(n):
	num_dict = dict({})
	return staircase_faster(n, num_dict)

def staircase_faster(n, num_dict):
	if n==0 or n==1:
		return 1
	elif n==2:
		return 2
	elif n==3:
		return 4
	else:
		if (n-1) in num_dict:
			first_output = num_dict[n-1]
		else:
			first_output = staircase_faster(n-1, num_dict)

		if (n-2) in num_dict:
			second_output = num_dict[n-2]
		else:
			second_output = staircase_faster(n-2, num_dict)

		if (n-3) in num_dict:
			third_output = num_dict[n-3]
		else:
			third_output = staircase_faster(n-3, num_dict)

		output = first_output + second_output + third_output
	num_dict[n] = output
	return output

print(staircase(0), staircase_1(0), staircase_2(0))
print(staircase(1), staircase_1(1), staircase_2(1))
print(staircase(2), staircase_1(2), staircase_2(2))
print(staircase(3), staircase_1(3), staircase_2(3))
print(staircase(4), staircase_1(4), staircase_2(4))
