class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = len(nums)-nums.count(val)
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return c