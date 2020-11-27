import time
class Solution:
	def isPalindrome(self, x: int) -> bool:
		original = int(x)
		reverse = 0
		if x < 0:
			return False
		if 0 < x < 10:
			return True
		while x > 0:
			reverse = (reverse*10)+(x%10)
			x = x//10
		return reverse == original

a = Solution()
start = time.time()
sol = a.isPalindrome(121)
print("sol:%s"%sol)
sol = a.isPalindrome(-121)
print("sol:%s"%sol)
sol = a.isPalindrome(10)
print("sol:%s"%sol)
sol = a.isPalindrome(5)
print("sol:%s"%sol)
sol = a.isPalindrome(-101)
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))