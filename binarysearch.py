# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    left, right = 0, len(keys)
    while left + 1 < right:
        ave = (left + right) // 2
        if keys[ave] <= query:
            left = ave
        else:
            right = ave
    if keys[left] != query:
        return -1
    else:
        return left


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
