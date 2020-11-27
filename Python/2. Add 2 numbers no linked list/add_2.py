import time
class Solution:
	def addTwoNumbers(self, l1, l2):
		sol = []
		len_l1, len_l2 = len(l1),len(l2)
		biggest = len_l1 if len_l1 > len_l2 else len_l2
		sum = 0
		for i in range(biggest):
			sum += ((l1 and l1.pop()*(10**(len_l1-i-1)) or 0) + (l2 and l2.pop()*(10**(len_l2-i-1)) or 0))
		sol = list(map(int, str(sum)))
		sol.reverse()
		return sol

a = Solution()
start = time.time()
sol = a.addTwoNumbers([2,4,3],[5,6,4])
print('sol---%s'%sol)
sol = a.addTwoNumbers([0],[0])
print('sol---%s'%sol)
sol = a.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
print('sol---%s'%sol)
sol = a.addTwoNumbers([1,2,3],[3,2,1])
print('sol---%s'%sol)
print('total time:--%s'%(time.time()-start))