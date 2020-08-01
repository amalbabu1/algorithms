# python3


def edit_distance(first_string, second_string):
    rows = len(first_string)
    cols = len(second_string)

    dist = [[0]*(rows+1) for i in range(cols+1)]

    for col in range(1, cols+1):
        for row in range(1, rows+1):
            if col == 0 or row == 0:
                dist[row][col] = 0
            elif first_string[row-1] == second_string[col-1]:
                dist[row][col] = dist[row-1][col-1]+1
            else:
                dist[row][col] = max(dist[row-1][col],
                                     dist[row][col-1])

    return dist[rows][cols]


if __name__ == '__main__':
    a = [2, 3, 9]
    b = [2, 9, 7, 8]
    print(edit_distance(a, b))
