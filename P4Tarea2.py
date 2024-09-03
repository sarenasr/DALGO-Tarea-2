ordered_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

def binary_search_matrix(matrix, value):
    low = 0
    high = len(matrix) -1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        low_row = 0
        high_row = len(matrix[mid]) - 1

        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2

            if matrix[mid][mid_row] < value:
                low_row = mid_row + 1
            elif matrix[mid][mid_row] > value:
                high_row = mid_row - 1
            else:
                return mid, mid_row
        if matrix[mid][mid_row] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binary_search_matrix(ordered_matrix, 9)) # (1, 1)