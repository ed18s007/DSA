def power_of_2(n):
	if n==0:
		return 1
	else:
		return 2 * power_of_2(n-1)

print(power_of_2(5))
# print(power_of_2(1000))

def sum_integers(n):
	if n==0:
		return 0
	else:
		return n + sum_integers(n-1)

print(sum_integers(3), sum_integers(4), sum_integers(5))

def sum_array(arr):
	if len(arr) == 1:
		return arr[0]
	else:
		return arr[0] + sum_array(arr[1:])
arr = [1,2,3,4]
print(sum_array(arr))

def sum_arr_index(arr, index):
	if len(arr) -1 == index:
		return arr[index]
	else:
		return arr[index] + sum_arr_index(arr, index+1)

print(sum_arr_index(arr,0))

def sum_arr_iter(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	return sum

print(sum_arr_iter(arr))

def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(5), factorial(0), factorial(100))