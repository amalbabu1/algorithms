# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + \
            fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers)


def fibo(n):
    lis = [0, 1]
    if n == 0 or n == 1:
        pass
    for i in range(2, n+1):
        lis.append(lis[i-1] + lis[i-2])
    return lis[-1]


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    lis = fibo(n+2)-1
    return lis % 10


if __name__ == '__main__':
    input_n = int(input())
    # for input_n in range(1, 15):
    p = last_digit_of_the_sum_of_fibonacci_numbers(input_n)
    #q = last_digit_of_the_sum_of_fibonacci_numbers_naive(input_n)
    print(p)
