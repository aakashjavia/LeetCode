import time
class Solution:
	def intToRoman(self, num: int) -> str:
		d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
			50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
		sol = []
		for element in d:
			sol += [d[element]*(num//element)]
			num = num%element
		
		return ''.join(sol)

a = Solution()
start = time.time()
sol = a.intToRoman(3)
print("sol:%s"%sol)
sol = a.intToRoman(4)
print("sol:%s"%sol)
sol = a.intToRoman(9)
print("sol:%s"%sol)
sol = a.intToRoman(58)
print("sol:%s"%sol)
sol = a.intToRoman(1994)
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
