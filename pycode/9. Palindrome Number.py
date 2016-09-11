def isPalindrome(x):

    if x < 0:
        return False
    reverse = 0
    x1 = x
    while x1 != 0:
        reverse = reverse*10 + x1%10
        x1 = x1//10
    return reverse == x
test = [1, 12, 11, 121, 12321, 1234]
print(map(isPalindrome, test))