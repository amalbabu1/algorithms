# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1]
                                for i in range(len(stops) - 1)) and stops[-1] < d

    # d - destination
    # m-milege
    stops.insert(0, 0)
    stops.append(d)
    # print(stops)
    current = 0
    last = 0
    no_refil = 0
    n = len(stops)
    while current < n-1:
        last = current
        while ((current < n-1) and ((stops[current+1]-stops[last]) <= m)):
            current += 1
        if current == last:
            return -1
        if current < n-1:
            no_refil += 1
    return no_refil


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = [200, 375, 550, 750]
    input_stops = list(map(int, input().split()))
    #assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
