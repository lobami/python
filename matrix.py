def matrixElementsSum(matrix):
    dis = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                break
            dis += matrix[j][i]
    return dis