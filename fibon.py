# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n
# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number(n):

    lis = [0, 1]
    if n == 0 or n == 1:
        return n
    for i in range(2, n+1):
        lis.append(lis[i-1] + lis[i-2])
    return lis[-1]


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    lis = [0, 1]
    lis.append(1)
    i = 3
    while(True):
        lis.append(((lis[i-1] + lis[i-2]) % m))
        i += 1
        if ((lis[-2] == 0) and (lis[-3] == 1)):
            break
    new_m = len(lis)-2
    n = n % new_m
    n = fibonacci_number(n)
    t1 = n % m
    return t1


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
