class Solution:
	def twoSum(self, nums, target):
		lookup={}
		
		for index, x in enumerate (nums):
			if target-x in lookup:
				return [lookup[target-x], index]
			lookup[x]=index
		raise Exception('No pair found.')

a = Solution()
print(a.twoSum(nums = [2,7,11,15], target = 9))
print(a.twoSum(nums = [3,2,4], target = 6))
print(a.twoSum(nums = [3,3], target = 6))
