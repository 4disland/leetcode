class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        from collections import Counter
        from functools import reduce
        c1, c2 = Counter(nums1), Counter(nums2)
        inter = c1 & c2
        if not inter:
            return []
        return reduce(lambda x,y: x+y, [[k]*inter[k] for k in inter])

print(Solution().intersect([1,2,2,1], [2,2]))