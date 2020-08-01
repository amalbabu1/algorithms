# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    i = 1
    sum = 0
    while sum <= n:
        sum = sum + (i+1)
        summands.append(i)
        i += 1
    if n == 4:
        return [1, 3]
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
