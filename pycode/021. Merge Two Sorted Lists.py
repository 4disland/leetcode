# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = None
        cur = ret
        if not l1:
            return l2
        elif not l2:
            return l1
            
        while True:
            if not l1 and not l2:
                break
            elif l1 and not l2:
                cur.next = l1
                break
            elif l2 and not l1:
                cur.next = l2
                break
            if l1.val < l2.val:
                if not ret:
                    ret = l1
                    l1 = l1.next
                    cur = ret
                    continue
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                if not ret:
                    ret = l2
                    l2 = l2.next
                    cur = ret
                    continue
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        return ret