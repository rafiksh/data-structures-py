def sorted_matrix_search(matrix, num):
    col_index = len(matrix[0]) - 1
    for row_index in range(len(matrix)):
        while num <= matrix[row_index][col_index]:
            if matrix[row_index][col_index] == num:
                return row_index, col_index
            col_index -= 1
    return False


if __name__ == '__main__':
    print(sorted_matrix_search([[1, 2, 5, 8],
                                [6, 30, 50, 100],
                                [21, 35, 100, 110]], 35))
