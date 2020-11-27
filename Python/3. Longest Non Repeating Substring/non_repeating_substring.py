import time
class Solution:
	def lengthOfLongestSubstring(self, s):
		start = 0
		max_length = 0
		charset = {}
		
		for i in range(len(s)):
			if s[i] in charset and start <= charset[s[i]]:
				start = charset[s[i]] + 1
			else:
				max_length = max(max_length, i - start + 1)

			charset[s[i]] = i

		return max_length


a = Solution()
start = time.time()
sol = a.lengthOfLongestSubstring("abcabcbb")
print("sol:%s"%sol)
sol = a.lengthOfLongestSubstring("bbbbb")
print("sol:%s"%sol)
sol = a.lengthOfLongestSubstring("pwwkew")
print("sol:%s"%sol)
sol = a.lengthOfLongestSubstring("")
print("sol:%s"%sol)
sol = a.lengthOfLongestSubstring("aab")
print("sol:%s"%sol)
sol = a.lengthOfLongestSubstring("dvdf")
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))

