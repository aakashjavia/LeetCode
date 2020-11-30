import time
class Solution:
	def maximumWealth(self, accounts) -> int:
		# return max(map(sum, accounts))
		max_wealth = 0
		for customer in accounts:
			if sum(customer) > max_wealth:
				max_wealth = sum(customer)
		return max_wealth

a = Solution()
start = time.time()
sol = a.maximumWealth([[1,2,3],[3,2,1]])
print("sol:%s"%sol)
sol = a.maximumWealth([[1,5],[7,3],[3,5]])
print("sol:%s"%sol)
sol = a.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
