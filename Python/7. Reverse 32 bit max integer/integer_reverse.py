import time
class Solution:
	def reverse(self, x: int) -> int:
		sign = -1 if x < 0 else 1
		string = str(abs(x))
		sol = int(string[::-1])*sign
		if (sol > 2**31) or (sol < -(2**31)-1):
			return 0
		return sol

a = Solution()
start = time.time()
sol = a.reverse(123)
print("sol:%s"%sol)
sol = a.reverse(-123)
print("sol:%s"%sol)
sol = a.reverse(120)
print("sol:%s"%sol)
sol = a.reverse(0)
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))