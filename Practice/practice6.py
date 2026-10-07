def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = find_max(25, 17, 40)
print("Maximum =", result)