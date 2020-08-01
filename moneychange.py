# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


coins = [1, 3, 4]
memo = {}
memo[0] = 0


def change(money):
    for i in range(1, money+1):
        lis = 1000
        if money in memo.keys():
            return memo[money]
        else:
            for coin in coins:
                if money >= coin:
                    noCoins = change(money-coin)+1
                    if lis > noCoins:
                        lis = noCoins

        memo[money] = lis
    return memo[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
