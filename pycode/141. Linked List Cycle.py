# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = slow.next if slow else None
        while True:
            slow = slow.next if head else None
            fast = fast.next.next if fast and fast.next else None
            if fast == None:
                return False
            if slow == fast:
                return True