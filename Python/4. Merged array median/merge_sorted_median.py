import time
class Solution:
	def findMedianSortedArrays(self, nums1, nums2) -> float:
		median = 0
		len_nums1 = len(nums1)
		len_nums2 = len(nums2)
		if not (len_nums1 + len_nums2)%2:
			median_pos2 = (len_nums1 + len_nums2)//2
			median_pos1 = median_pos2-1
		else:
			median_pos2 = median_pos1 = (len_nums1 + len_nums2)//2
		if nums1 and nums2:
			if len_nums1 > len_nums2:
				final_array = nums1
				other_array = nums2
			else:
				final_array = nums2
				other_array = nums1
			pointer = 0
			max_length = max(len_nums1,len_nums2)
			for e in other_array:
				for i in range(pointer,max_length):
					insert = i
					if final_array[i] >= e:
						final_array.insert(insert,e)
						break
				pointer = insert
				if pointer > (median_pos1+5):
					break

		elif (nums1 and not nums2) or (nums2 and not nums1):
			final_array = nums1 or nums2
		print('final_array:: %s'%final_array)
		
		median = (final_array[median_pos1]+final_array[median_pos2])/2
		return median

a = Solution()
start = time.time()
# sol = a.findMedianSortedArrays([1,3,5,6,17],[2,4,7,8,10,14,24,36])
# print('sol---%s'%sol)
# sol = a.findMedianSortedArrays([1,3],[2])
# print('sol---%s'%sol)
sol = a.findMedianSortedArrays([3],[-2,-1])
print('sol---%s'%sol)
# sol = a.findMedianSortedArrays([1,3],[2,7])
# print('sol---%s'%sol)
# sol = a.findMedianSortedArrays([1,2],[3,4])
# print('sol---%s'%sol)
# sol = a.findMedianSortedArrays([0,0],[0,0])
# print('sol---%s'%sol)
# sol = a.findMedianSortedArrays([],[1])
# print('sol---%s'%sol)
# sol = a.findMedianSortedArrays([2],[])
# print('sol---%s'%sol)
print('total time:--%s'%(time.time()-start))