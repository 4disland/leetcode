class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # also you can use moore voting algorithm
        
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]