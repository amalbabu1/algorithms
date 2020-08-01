

def isOperator(op):
    return (op == '+' or op == '*' or op == '-')


def find_maximum_value(exp):
    num = []
    opr = []
    tmp = ""

    for i in range(len(exp)):
        if (isOperator(exp[i])):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp = ""
        else:
            tmp += exp[i]

    num.append(int(tmp))

    llen = len(num)
    minVal = [[0 for i in range(llen)] for i in range(llen)]
    maxVal = [[0 for i in range(llen)] for i in range(llen)]

    for i in range(llen):
        for j in range(llen):
            if (i == j):
                minVal[i][j] = maxVal[i][j] = num[i]

    for L in range(1, llen):
        for i in range(0, llen - L):
            j = i + L
            minv = 1000
            maxv = -1000
            for k in range(i, j):

                if(opr[k] == '+'):
                    a = (maxVal[i][k])+(maxVal[k+1][j])
                    b = (maxVal[i][k])+(minVal[k+1][j])
                    c = (minVal[i][k])+(maxVal[k+1][j])
                    d = (minVal[i][k])+(minVal[k+1][j])
                    minv = min(minv, a, b, c, d)
                    maxv = max(maxv, a, b, c, d)

                elif(opr[k] == '*'):

                    a = (maxVal[i][k])*(maxVal[k+1][j])
                    b = (maxVal[i][k])*(minVal[k+1][j])
                    c = (minVal[i][k])*(maxVal[k+1][j])
                    d = (minVal[i][k])*(minVal[k+1][j])
                    minv = min(minv, a, b, c, d)
                    maxv = max(maxv, a, b, c, d)

                elif(opr[k] == '-'):

                    a = (maxVal[i][k])-(maxVal[k+1][j])
                    b = (maxVal[i][k])-(minVal[k+1][j])
                    c = (minVal[i][k])-(maxVal[k+1][j])
                    d = (minVal[i][k])-(minVal[k+1][j])
                    minv = min(minv, a, b, c, d)
                    maxv = max(maxv, a, b, c, d)

            # print("------------------------", a, b, c, d)

            minVal[i][j] = minv
            maxVal[i][j] = maxv

    print(maxVal[0][llen - 1])


if __name__ == "__main__":
    expression1 = input()
    find_maximum_value(expression1)
