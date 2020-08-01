
def Knapsack(W, i):
    val = [[0 for i in range(W+1)] for i in range(c+1)]
    for i in range(1, c+1):
        for w in range(1, W+1):
            (val[i][w]) = (val[i-1][w])
            for wi in input_weights:
                if wi <= w:
                    vall = (val[i-1][w-wi])+wi
                    if(val[i][w] < vall):
                        val[i][w] = vall
    for i in val:
        print(i)
    return val[-1][-1]


if __name__ == "__main__":
    input_weights = (1, 4, 8)
    c = len(input_weights)
    input_capacity = 10
    print(Knapsack(input_capacity, c))

    """val[w][i] = val[w][i-1]
            a = []
            for wi in input_weights:
                if wi <= w:
                    val = (val[w-wi][i-1]+wi)
                    print(val)
                    # a.append(val)
            # val[w][i] = min(a)"""
