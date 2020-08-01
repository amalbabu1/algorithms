def fun(lis):
    if len(lis) == 1:
        return lis[0]
    else:
        return max(lis[0], fun(lis[1:]))


def fun1(lis):
    if len(lis) == 1:
        return lis[0]
    else:
        s = fun1(lis[1:])
        f = lis[0]
        if s > f:
            return s
        else:
            return f


lis = [3, 4, 8, 1]
a = fun1(lis)
print(a)
