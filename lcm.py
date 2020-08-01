# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9
    while b != 0:
        a, b = b, a % b
        gcd(a, b)
    return a


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    gcd1 = gcd(a, b)
    lcm1 = (a*b)//gcd1
    return lcm1


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
    #print(lcm_naive(input_a, input_b))
