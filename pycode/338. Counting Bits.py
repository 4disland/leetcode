class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def deltaBits(num):
            cnt = 1
            mask = 1
            while num & mask:
                cnt -= 1
                mask <<= 1
            return cnt
        ret = [0]
        for i in range(1, num+1):
            ret.append(ret[-1]+deltaBits(i-1))
        return ret
                