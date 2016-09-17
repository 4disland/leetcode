class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i+1
        return len(nums)+1

print(Solution().firstMissingPositive([3,4,-1,1]))