def get_combinations(num):
	if num == 2:
		return "abc"
	elif num == 3:
		return "def"
	elif num==4:
		return "ghi"
	elif num==5:
		return "jkl"
	elif num==6:
		return "mno"
	elif num==7:
		return "pqrs"
	elif num == 8:
		return "tuv"
	elif num == 9:
		return "wxyz"
	else:
		return ""

def keypad(num): 
	if num == 0 :
		return [""]

	elif num/10 <1:
		return [char for char in get_combinations(num)]
	
	else:
		input_level = get_combinations(num%10)
		input_prev = keypad(num//10)

		result = []

		for a_i in input_level :
			for b_i in input_prev:
				result.append( b_i + a_i )

		return result

def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")

# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)

# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)

# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)

# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)

input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)