import time
class Solution:
	def longestCommonPrefix(self, strs) -> str:
		if strs:
			test_str = min(strs, key = len)
			strs.remove(test_str)
			while test_str:
				valid = True
				for element in strs:
					if not element.startswith(test_str):
						valid = False
						test_str = test_str[:-1]
						break
				if valid:
					return test_str
		return ''

a = Solution()
start = time.time()
sol = a.longestCommonPrefix(["flower","flow","flight"])
print("sol:%s"%sol)
sol = a.longestCommonPrefix(["dog","racecar","car"])
print("sol:%s"%sol)
sol = a.longestCommonPrefix(['hello','hell','hek'])
print("sol:%s"%sol)
sol = a.longestCommonPrefix([])
print("sol:%s"%sol)
sol = a.longestCommonPrefix([])
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
