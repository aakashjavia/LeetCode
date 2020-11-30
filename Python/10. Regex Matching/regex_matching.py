import time
# class Solution:
# 	def isMatch(self, s: str, p: str) -> bool:
# 		def check_dot(string,pattern):
# 			dot_index = pattern.find('.')
# 			if dot_index >= 0 and pattern[:dot_index] == string[:dot_index]:
# 				return check_dot(string[dot_index+1:],pattern[dot_index+1:])
# 			elif dot_index == -1:
# 				return string == pattern
# 			else:
# 				return False
		
# 		def check_star(string,pattern):
# 			if '*' in pattern:
# 				if pattern == '.*' and string:
# 					return True
# 				ast_pointer = pattern.find('*')-1
# 				p_pointer = 0
# 				s_pointer = ast_pointer
# 				ast_character = pattern[ast_pointer]
# 				pre_ast_pattern = pattern[:ast_pointer]
# 				after_ast = string[ast_pointer:]
# 				#first we check whatever is before the wildcard, including dots
# 				dot_check = check_dot(string[:ast_pointer],pre_ast_pattern)
# 				if not dot_check:
# 					return False
# 				#now we check the asterisk itself
# 				for char in after_ast:
# 					if char != ast_character:
# 						break
# 					s_pointer += 1
# 				return check_star(string[s_pointer:],pattern[ast_pointer+2:])
# 			elif '.' in pattern:
# 				return check_dot(string,pattern)
# 			else:
# 				return string == pattern

# 		return check_star(s,p)
called = 0
class Solution(object):
	def isMatch(self, s, p):
		global called
		called += 1
		if not p:
			return not s

		first_match = bool(s) and p[0] in [s[0], '.']
		if len(p) >= 2 and p[1] == '*':
			p2 = self.isMatch(s, p[2:])
			if not p2 and first_match:
				p3 = self.isMatch(s[1:], p)
			return (p2 or
					first_match and p3)
		else:
			return first_match and self.isMatch(s[1:], p[1:])

a = Solution()
start = time.time()
# sol = a.isMatch(s = "abcbaaaaaaaaccc", p = "abc.a*ccc")
# print("sol:%s"%sol)
# sol = a.isMatch(s = "abcabdhrda", p = "abc......a")
# print("sol:%s"%sol)
sol = a.isMatch(s = "aa", p = "a*")
print("sol:%s"%sol)
# sol = a.isMatch(s = "aaaaaa", p = "a*a")
# print("sol:%s"%sol)
# sol = a.isMatch(s = "ab", p = ".*.*.*")
# print("sol:%s"%sol)
# sol = a.isMatch(s = "a", p = ".")
# print("sol:%s"%sol)
# sol = a.isMatch(s = "aab", p = "c*a*b")
# print("sol:%s"%sol)
# sol = a.isMatch(s = "mississippi", p = "mis*is*p*.")
# print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
