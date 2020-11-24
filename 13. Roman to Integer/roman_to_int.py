import time
class Solution:
	def romanToInt(self, s: str) -> int:
		d = {
			'M':1000,
			'D':500,
			'C':100,
			'L':50,
			'X':10,
			'V':5,
			'I':1
			}
		sol = 0
		for i in range(len(s)-1):
			if d[s[i]] < d[s[i+1]]:
				sol -= d[s[i]]
			else:
				sol += d[s[i]]
		
		return sol + d[s[-1]]

a = Solution()
start = time.time()
sol = a.romanToInt("III")
print("sol:%s"%sol)
sol = a.romanToInt("IV")
print("sol:%s"%sol)
sol = a.romanToInt("IX")
print("sol:%s"%sol)
sol = a.romanToInt("LVIII")
print("sol:%s"%sol)
sol = a.romanToInt("MCMXCIV")
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
