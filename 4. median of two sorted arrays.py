def findMedianSortedArrays(num1, num2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = []
    total_len = len(num1) + len(num2)
    i_stop = 0
    if total_len % 2 == 0:
        i_stop = total_len//2+1
    else:
        i_stop = (total_len+1)//2

    
    idx1, idx2 = (0, 0)
    for i in range(i_stop):
        if idx1 == len(num1):
            merged.append(num2[idx2])
            idx2 += 1
        elif idx2 == len(num2):
            merged.append(num1[idx1])
            idx1 += 1
        else:
            if num1[idx1] < num2[idx2]:
                merged.append(num1[idx1])
                idx1 += 1
            else:
                merged.append(num2[idx2])
                idx2 += 1
    if total_len % 2 == 1:
        return merged[-1]
    else:
        return (merged[-1] + merged[-2]) / 2.0 # NOTICE

    # python2 treats / as truncated divison, while python3 treats / as normal division.


print(findMedianSortedArrays([1,2], [3,4]))
