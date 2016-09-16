class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def com(n, i):
            if i == 0:
                return 1
            elif i == 1:
                return n
            elif i <= n/2:
                a = reduce(lambda x,y:x*y, (i for i in range(n-i+1, n+1)))
                b = reduce(lambda x,y:x*y, (i for i in range(1,i+1)))
                return a/b
            else:
                return com(n,n-i)
        return [com(rowIndex, i) for i in range(rowIndex+1)]
        