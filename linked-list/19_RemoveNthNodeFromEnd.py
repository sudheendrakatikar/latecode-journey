# Runtime   16 ms    92.26%
# Memory    13.3 MB  68.98%

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution(object):
  def removeNthFromEnd(self, head, n):
    start = head
    for i in range(0, n):
      start = start.next
    if start == None:
      return head.next
    tail = head
    previous = None
    while start != None:
      start = start.next
      previous = tail
      tail = tail.next
    previous.next = tail.next
    return head

node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
n = 2
result = Solution.removeNthFromEnd(Solution, node1, n)
while result != None:
  print(result.val)
  result = result.next