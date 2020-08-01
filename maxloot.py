# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    tup = []
    n = len(weights)
    for i in range(0, n):
        u = prices[i]/weights[i]
        li = [u, prices[i], weights[i]]
        tup.append(li)
    tup.sort(key=lambda x: x[0])
    # print(tup)
    W = capacity
    v = 0
    j = -1
    for i in range(0, n):
        if W == 0:
            return v
        wi = tup[j][2]
        # print(wi)
        a = min(wi, W)
        v = v + a * tup[j][0]
        W = W - a
        tup[j][2] = wi-a
        j += -1

    return v


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
