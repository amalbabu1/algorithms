# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    ten, money = money//10, money % 10
    five, one = money//5, money % 5
    return (ten+five+one)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
