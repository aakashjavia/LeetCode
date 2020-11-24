import time
class Solution:
	def convert(self, s: str, numRows: int) -> str:
		output = ""
		output_dict = dict()
		row = 1
		forward = True
		if numRows == 1:
			return s
		for i in range(len(s)):
			output_dict[row] = output_dict.get(row,'')+s[i]
			if not row%numRows:
				forward = False
			if row == 1:
				forward = True
			if forward:
				row += 1
			else:
				row -= 1
		for row in output_dict:
			output += output_dict[row]
		return output
	
a = Solution()
start = time.time()
sol = a.convert("PAYPALISHIRING",3)
print("sol:%s. Correct?%s"%(sol,sol=="PAHNAPLSIIGYIR"))
sol = a.convert("PAYPALISHIRING",4)
print("sol:%s. Correct?:%s"%(sol,sol=="PINALSIGYAHRPI"))
sol = a.convert("a",1)
print("sol:%s\t Correct?:%s"%(sol,sol=="a"))

# sol = a.convert("a",1)
# print("sol:%s"%sol)
# sol = a.convert("ac",2)
# print("sol:%s"%sol)
# sol = a.longestPalindrome("aab")
# print("sol:%s"%sol)
# sol = a.longestPalindrome("dvdf")
# print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))