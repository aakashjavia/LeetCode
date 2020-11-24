import time
class Solution:
	def findMedianSortedArrays(self, nums1, nums2) -> float:
		print('nums1---%s'%nums1)
		print('nums2---%s'%nums2)
		median = 0
		if nums1 and nums2:
			if nums1[0] > nums2[0]:
				final_array = [nums2[0],nums1[0]]
				n1_last_pos = 1
				n2_last_pos = 0
			else:
				final_array = [nums1[0],nums2[0]]
				n1_last_pos = 0
				n2_last_pos = 1
			len_nums1 = len(nums1)
			len_nums2 = len(nums2)
			
			for i in range(1,max(len_nums1,len_nums2)):
				if len_nums1 > i:
					insert_pos = n1_last_pos+1 if final_array[n1_last_pos] > final_array[n2_last_pos] else n2_last_pos+1
					print('inserting from 1---%s'%nums1[i])
					
					final_array.insert(insert_pos,nums1[i])
					n1_last_pos = insert_pos
				if len_nums2 > i:
					insert_pos = n1_last_pos+1 if final_array[n1_last_pos] > final_array[n2_last_pos] else n2_last_pos+1
					print('inserting from 2---%s'%nums2[i])
					final_array.insert(insert_pos,nums2[i])
					n2_last_pos = insert_pos
			print('final_array---%s'%final_array)
			
		elif (nums1 and not nums2) or (nums2 and not nums1):
			final_array = nums1 or nums2


		final_length = len(final_array)
		if final_length%2:
			median_pos = final_length//2
			median = float(final_array[median_pos])
		else:
			median_pos1 = final_length//2
			median_pos2 = final_length//2+1
			median = float((final_array[median_pos1]+final_array[median_pos2])/2)
		return median

a = Solution()
start = time.time()
sol = a.findMedianSortedArrays([1,3,5,6,17],[2,4,7,8,10,14,24,36])
print('sol---%s'%sol)
sol = a.findMedianSortedArrays([1,3],[2])
print('sol---%s'%sol)
sol = a.findMedianSortedArrays([1,2],[3,4])
print('sol---%s'%sol)
sol = a.findMedianSortedArrays([0,0],[0,0])
print('sol---%s'%sol)
sol = a.findMedianSortedArrays([],[1])
print('sol---%s'%sol)
sol = a.findMedianSortedArrays([2],[])
print('sol---%s'%sol)
print('total time:--%s'%(time.time()-start))