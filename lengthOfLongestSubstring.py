def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 1:
        return 1
    ret = 0
    new_str = ''
    for i in s:
        if i not in new_str:
            new_str += i
            ret = len(new_str) if len(new_str) > ret else ret
        else:
            # simulate a deque, also can from collections import deque
            idx = new_str.find(i)
            new_str = new_str[idx+1:]+i
            ret = len(new_str) if len(new_str) > ret else ret       
    return ret

print(lengthOfLongestSubstring('abca'))