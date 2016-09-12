class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        a = sorted(nums)
        for i in range(len(a)-2):
            if a[i] == a[i-1] and i!=0:
                continue
            j, k = i+1, len(a)-1
            while j<k:
                s = a[i]+a[j]+a[k]
                if s == 0:
                    ret.append([a[i], a[j], a[k]])
                    j += 1
                    k -= 1
                    while j<k and a[j] == a[j-1]:
                        j+=1
                    while j<k and a[k] == a[k+1]:
                        k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        return ret

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))