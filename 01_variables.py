# 1.1.2


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


# swap(12, 28)


#  1.1.3

# print(2**3)

# 1.1.4


def power(a, b):
    s = a
    z = 1
    while b > 0:
        # for n in range(b, 1, -1):
        if 0 == b % 2:
            b /= 2
            s = s * s
        else:
            z = s * z
            b -= 1
    return z


print(power(3, 6))
print(power(2, 5))
