import time
class Solution:
	def longestPalindrome(self, s):
		res = ""
		for i in range(len(s)):
			odd = self.check(s, i, i)
			if len(odd) > len(res):
				res = odd
			even = self.check(s, i, i+1)
			if len(even) > len(res):
				res = even
		return res
	
	def check(self, string, left, right):
		while left >= 0 and right < len(string) and string[left] == string[right]:
			left -= 1; right += 1
		return string[left+1:right]

a = Solution()
start = time.time()
sol = a.longestPalindrome("babad")
print("sol:%s"%sol)
sol = a.longestPalindrome("cbbd")
print("sol:%s"%sol)
sol = a.longestPalindrome("a")
print("sol:%s"%sol)
sol = a.longestPalindrome("ac")
print("sol:%s"%sol)
# sol = a.longestPalindrome("aab")
# print("sol:%s"%sol)
# sol = a.longestPalindrome("dvdf")
# print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))