# python3

from sys import stdin

# python3


def maximum_gold(capacity, weights):
    memo = [0]*capacity
    for i in range(1, capacity+1):
        lis = []
        for weight in weights:
            if i >= weight:
                lis.append((memo[i-weight]+weight))
                print(lis)
        memo[i] = (max(lis))
    return memo[-1]


if __name__ == '__main__':
    #input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    #assert len(input_weights) == n
    input_weights = (1, 4, 8)
    input_capacity = 10
    print(maximum_gold(input_capacity, input_weights))
