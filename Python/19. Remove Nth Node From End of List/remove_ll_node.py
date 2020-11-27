import time
class ListNode:
	# Definition for singly-linked list.
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		
		return head

a = Solution()
start = time.time()
l1 = ListNode(2,ListNode(4,ListNode(3,None)))
sol = a.removeNthFromEnd(l1,1)
print("sol:%s"%sol)
# l1 = ListNode(2,ListNode(4,ListNode(3,None)))
# sol = a.removeNthFromEnd(l1,3)
# print("sol:%s"%sol)
# l1 = ListNode(2,ListNode(4,ListNode(3,None)))
# sol = a.removeNthFromEnd(l1,3)
# print("sol:%s"%sol)
# l1 = ListNode(2,ListNode(4,ListNode(3,None)))
# sol = a.removeNthFromEnd(l1,3)
# print("sol:%s"%sol)
# l1 = ListNode(2,ListNode(4,ListNode(3,None)))
# sol = a.removeNthFromEnd(l1,3)
# print("sol:%s"%sol)
# l1 = ListNode(2,ListNode(4,ListNode(3,None)))
# sol = a.removeNthFromEnd(l1,3)
print("sol:%s"%sol)
print('total time:--%s'%(time.time()-start))
