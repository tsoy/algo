__author__ = 'sergey'


def getFibonaci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return getFibonaci(n-1) + getFibonaci(n-2)


def get_fibonnaci_non_rec(n):
    if n == 0 or n == 1:
        return 1

    i = 1
    j = 1

    for z in range(1, n):
        tmp = j
        j = i + j
        i = tmp

    return j


print(get_fibonnaci_non_rec(5))
