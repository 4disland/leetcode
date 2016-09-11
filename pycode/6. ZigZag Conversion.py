def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    from collections import defaultdict
    from functools import reduce
    d = defaultdict(list)
    idx = 0
    back = True
    for i in range(len(s)):
        d[idx].append(s[i])
        if idx == numRows - 1 or idx == 0:
            back = not back
        if back:
            idx -= 1
        else:
            idx += 1
    ret = ''
    # for i in d:
    #     ret += ''.join(d[i])
    if d:
        ret = ''.join(reduce(lambda x,y: x+y, d.values()))
    return ret
print(convert("", 3))
    
