# Runtime   44 ms    99.46%
# Memory    13.6 MB  39.13%

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		head = None
		previous = None
		carry = 0
		while l1 != None:
			if l2 != None:
				val = l1.val + l2.val + carry
				if val >= 10:
					val = val % 10
					carry = 1
				else:
					carry = 0
				if head == None:
					head = ListNode(val, None)
					previous = head
				else:
					node = ListNode(val, None)
					previous.next = node
					previous = node
				l1 = l1.next
				l2 = l2.next
			else:
				while l1 != None:
					if l1.val+carry >= 10:
						node = ListNode((l1.val+carry) % 10, None)
						carry = 1
					else:
						node = ListNode(l1.val+carry, None)
						carry = 0
					previous.next = node
					previous = node
					l1 = l1.next
		if l2 != None:
			while l2 != None:
				if l2.val+carry >= 10:
					node = ListNode((l2.val+carry) % 10, None)
					carry = 1
				else:
					node = ListNode(l2.val+carry, None)
					carry = 0
				previous.next = node
				previous = node
				l2 = l2.next
		if carry == 1:
			node = ListNode(1, None)
			previous.next = node
		return head

node3 = ListNode(9, None)
node2 = ListNode(9, node3)
l1 = ListNode(9, node2)

node4 = ListNode(9, None)
node3 = ListNode(9, node4)
node2 = ListNode(9, node3)
l2 = ListNode(9, node2)

sum = Solution.addTwoNumbers(Solution, l1, l2)
while sum != None:
	print(sum.val)
	sum = sum.next