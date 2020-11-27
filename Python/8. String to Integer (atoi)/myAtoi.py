import time
class Solution:
	def myAtoi(self, s: str) -> int:
		import string
		sol = 0
		input_str = s.strip().lower()
		sol_str = ''
		if input_str:
			sign = 1
			first_char = input_str[0]
			if first_char in ['-','+']:
				sign = -1 if first_char == '-' else 1
				input_str = input_str[1:]
			elif first_char.isnumeric():
				pass
			else:
				return 0
			for char in input_str:
				if char.isnumeric():
					sol_str += char
				else:
					break
			if sol_str:
				sol = int(sol_str)*sign
			else:
				return 0
		else:
			return 0

		if (sol >= 2**31):
			return 2**31-1
		elif (sol <= -(2**31)):
			return -(2**31)
		return sol

a = Solution()
start = time.time()
sol = a.myAtoi("2147483648")
print("sol:%s"%sol)
sol = a.myAtoi("-2147483649")
print("sol:%s"%sol)
sol = a.myAtoi("   -+42")
print("sol:%s"%sol)
sol = a.myAtoi("4193 WITH words")
print("sol:%s"%sol)
sol = a.myAtoi("words and 987")
print("sol:%s"%sol)
sol = a.myAtoi("-91283472332")
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))