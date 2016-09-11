class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            newArea = (j-i)*min(height[i], height[j])
            maxArea = max(maxArea, newArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea

a = Solution()
print(a.maxArea([1,2,1]))

# This is O(n) algorithm
# See https://discuss.leetcode.com/topic/3462/yet-another-way-to-see-what-happens-in-the-o-n-algorithm