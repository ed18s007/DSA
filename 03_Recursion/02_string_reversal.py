def string_reversal(inp_str):
	if inp_str == "":
		return ""
	elif len(inp_str)==1:
		return inp_str[0]
	else:
		idx = len(inp_str)-1
		return inp_str[idx] + string_reversal(inp_str[:idx])

print(string_reversal(""))
print(string_reversal("abcde"))
print(string_reversal("uvwxyz"))

def is_palindrome(inp_str):
	if len(inp_str) == 0 or len(inp_str) == 1:
		return True
	else:
		if inp_str[0] == inp_str[len(inp_str)-1]:
			return is_palindrome(inp_str[1:len(inp_str)-1])
		else:
			return False

print(is_palindrome(""))
print(is_palindrome("a"))
print(is_palindrome("madam"))
print(is_palindrome("abba"))
print(is_palindrome("Udacity"))