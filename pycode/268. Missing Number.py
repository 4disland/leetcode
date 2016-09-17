class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = len(nums)
        for i in range(len(nums)):
            ret ^= i
            ret ^= nums[i]
        return ret
print(Solution().missingNumber([2,1,3]))