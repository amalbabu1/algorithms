# python3
import operator
digit = []
op = []
min_mat = [[]]
max_mat = [[]]


def isOperator(op):
    return (op == '+' or op == '*' or op == '*')


def MinandMax(i, j):
    minv = 1000
    maxv = -1000
    global op
    global min_mat
    global max_mat
    print(i, j)

    for k in range(i, j):
        a = (op[k])
        print(a)
        if a == "+":
            a = (max_mat[i][k])+(max_mat[k+1][j])
            b = (max_mat[i][k])+(min_mat[k+1][j])
            c = (min_mat[i][k])+(max_mat[k+1][j])
            d = (min_mat[i][k])+(min_mat[k+1][j])
            minv = min(minv, a, b, c, d)
            maxv = max(maxv, a, b, c, d)
        if a == "-":
            a = (max_mat[i][k])-(max_mat[k+1][j])
            b = (max_mat[i][k])-(min_mat[k+1][j])
            c = (min_mat[i][k])-(max_mat[k+1][j])
            d = (min_mat[i][k])-(min_mat[k+1][j])
            minv = min(minv, a, b, c, d)
            maxv = max(maxv, a, b, c, d)
        if a == "*":
            a = (max_mat[i][k])*(max_mat[k+1][j])
            b = (max_mat[i][k])*(min_mat[k+1][j])
            c = (min_mat[i][k])*(max_mat[k+1][j])
            d = (min_mat[i][k])*(min_mat[k+1][j])
            minv = min(minv, a, b, c, d)
            maxv = max(maxv, a, b, c, d)
    return minv, maxv


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    temp = ""
    for i in range(len(dataset)):
        if isOperator(dataset[i]):
            op.append(dataset[i])
        else:
            digit.append(int(temp))
            temp = ""temp += dataset[i]
    digit.append(int(temp))

    n = len(digit)
    min_mat = [[0]*(n) for i in range(n)]
    max_mat = [[0]*(n) for i in range(n)]

    for i in range(0, n):
        min_mat[i][i] = digit[i]
        max_mat[i][i] = digit[i]

    for s in range(2, n+1):
        for i in range(n-s+1):
            j = i+s-1
            # min_mat[i][j], max_mat[i][j] =
            MinandMax(i, j)
            #print(i, j)

    # for i in min_mat:
    #    print(i)
    # print("-----------------------------------------------------")
    # for i in max_mat:
    #    print(i)
    # return(i, n)


if __name__ == "__main__":
    dataset = "5-8+7*4-8+9"

    find_maximum_value(dataset)
