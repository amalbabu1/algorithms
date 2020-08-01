# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    elements.sort()
    l = len(elements)
    inc = 0
    for i in range(0, l-1):
        if elements[i] == elements[i+1]:
            inc += 1
            if inc >= (l//2):
                return 1
        else:
            inc = 0

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
