import time
class ListNode:
	# Definition for singly-linked list.
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1, l2):
		sol = ListNode(0)
		last = sol
		carry = 0
		it_l1 = ListNode(l1.val,l1.next)
		it_l2 = ListNode(l2.val,l2.next)

		while it_l1 or it_l2 or carry:
			tot = (it_l1 and it_l1.val or 0) + (it_l2 and it_l2.val or 0) + carry
			digit = tot%10
			carry = tot//10
			last.next = ListNode(digit)
			last = last.next
			it_l1 = it_l1.next if it_l1 else None
			it_l2 = it_l2.next if it_l2 else None
		return sol.next

	def format_llist(self,llist):
		array = []
		while llist:
			array.append(llist.val)
			llist=llist.next
		return array

a = Solution()
start = time.time()
# l1 = ListNode(2,ListNode(4,ListNode(3,None)))
# l2 = ListNode(5,ListNode(6,ListNode(4,None)))
# sol = a.addTwoNumbers(l1,l2)
# print('sol---%s'%a.format_llist(sol))

# sol = a.addTwoNumbers(ListNode(0,None),ListNode(0,None))
# print('sol---%s'%a.format_llist(sol))

answer = a.addTwoNumbers(
	ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,None))))))),
	ListNode(9,ListNode(9,ListNode(9,ListNode(9,None))))
)
print('answer---%s'%a.format_llist(answer))
# sol = a.addTwoNumbers(
# 	ListNode(1,ListNode(2,ListNode(3,None))),
# 	ListNode(3,ListNode(2,ListNode(1,None)))
# )
# print('sol---%s'%a.format_llist(sol))

print('total time:--%s'%(time.time()-start))