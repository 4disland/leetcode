class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1],[1,1]]
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return ret
        else:
            for i in range(numRows-2):
                last_item = ret[-1]
                new_item = [last_item[j]+last_item[j+1] for j in range(len(last_item)-1)]
                new_item = [1]+new_item+[1]
                ret.append(new_item)
        return ret

print(Solution().generate(4))