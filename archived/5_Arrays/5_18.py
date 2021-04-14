# Imports
import math
from copy import deepcopy


def spiral_order(matrix):
    """
    2D List -> List
    Given: a matrix
    Returns: the given matrix in spiral order
    """

    def boundary_points(depth):
        """
        Int -> List
        Given: an int to indicate the depth of the submatrix
        Returns: a list with the boundar elements of the submatrix
        """
        n = len(matrix)

        if depth == n // 2:
            return [matrix[depth][depth]]

        boundary_points = []
        boundary_points.extend(matrix[depth][depth : -1 - depth])
        boundary_points.extend(list(zip(*matrix))[-1 - depth][depth : -1 - depth])
        boundary_points.extend(matrix[-1 - depth][-1 - depth : depth : -1])
        boundary_points.extend(list(zip(*matrix))[depth][-1 - depth : depth : -1])
        return boundary_points

    result = []
    for i in range((len(matrix) + 1) // 2):
        result.extend(boundary_points(i))
    return result


def spiral_order_opt(matrix):
    """
    A better optimized version
    2D List -> List
    Given: a matrix
    Returns: the given matrix in spiral order
    """

    def not_in_range(index):
        """
        Int -> Boolean
        Given: a single coordinate of the matrix
        Returns: True iff the given coordinate is not in the matrix
        """
        return index < 0 or index > n - 1

    SHIFT = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = x = y = 0
    result = []
    n = len(matrix)

    for _ in range(n ** 2):
        result.append(matrix[x][y])
        matrix[x][y] = float("inf")
        new_x, new_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (
            not_in_range(new_x)
            or not_in_range(new_y)
            or matrix[new_x][new_y] == float("inf")
        ):
            direction = (direction + 1) & 3
            new_x, new_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = new_x, new_y
    return result


def make_matrix_from_spiral(spiral_order_nums):
    """
    List -> 2D Mmatrix
    Given: given a list of ints in spiral order
    Returns: a 2D matrix composed of the given list of ints
    """

    def not_int(num):
        """
        Int -> Boolean
        Given: a number
        Returns: True iff the given number is an integer
        """
        return not (num - int(num) == 0)

    def not_in_range(index):
        """
        Int -> Boolean
        Given: a single coordinate of the matrix
        Returns: True iff the given coordinate is not in the matrix
        """
        value = index < 0 or index >= n
        return value

    SHIFT = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = x = y = 0
    n = math.sqrt(len(spiral_order_nums))

    # Check if a matrix is possible in the first place
    if not_int(n):
        return []

    # Initialize result
    n = int(n)
    result = [[float("inf")] * n for i in range(n)]

    # Compute result
    for i in range(len(spiral_order_nums)):
        result[x][y] = spiral_order_nums[i]
        new_x, new_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (
            not_in_range(new_x)
            or not_in_range(new_y)
            or result[new_x][new_y] != float("inf")
        ):
            direction = (direction + 1) & 3
            new_x, new_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = new_x, new_y
    return result


if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    spiral_m1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    spiral_m2 = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    assert spiral_order(m1) == spiral_m1
    assert spiral_order(m2) == spiral_m2
    assert spiral_order_opt(deepcopy(m1)) == spiral_m1
    assert spiral_order_opt(deepcopy(m2)) == spiral_m2

    assert make_matrix_from_spiral(deepcopy(spiral_m1)) == m1
    assert make_matrix_from_spiral(deepcopy(spiral_m2)) == m2
