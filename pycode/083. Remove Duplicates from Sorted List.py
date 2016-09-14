# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = head
        while head:
            cur = head
            while head.next and head.next.val == head.val:
                head = head.next
            cur.next = head.next
            head = head.next
        return ret