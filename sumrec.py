def sum(num):
    tmp = 0
    if num == 0:
        return 0
    else:
        return num % 10 + sum(num//10)


print(sum(1235))
