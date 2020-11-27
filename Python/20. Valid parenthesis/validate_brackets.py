import time
class Solution:
	def isValid(self, s: str) -> bool:
		check = {
			'{':'}',
			'[':']',
			'(':')'
		}
		if len(s)%2:
			return False
		stack = []
		for i in s:
			if i not in check:
				if not stack:
					return False
				if check[stack.pop()] != i:
					return False
			else:
				stack += [i]
		if stack:
			return False
		else:
			return True

a = Solution()
start = time.time()
sol = a.isValid("()")
print("sol:%s"%sol)
sol = a.isValid("()[]{}")
print("sol:%s"%sol)
sol = a.isValid("(]")
print("sol:%s"%sol)
sol = a.isValid("([)]")
print("sol:%s"%sol)
sol = a.isValid("{[]}")
print("sol:%s"%sol)
sol = a.isValid("[[")
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
