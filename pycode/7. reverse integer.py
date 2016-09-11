def reverse(x):
    y = str(x)[::-1]
    if y[-1] == '-':
        y = -int(y[:-1])
    if abs(int(y)) >= 1<<31:
        return 0
    return int(y)
print(reverse(123))
print(reverse(-1234))