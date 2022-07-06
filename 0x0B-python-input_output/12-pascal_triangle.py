#!/usr/bin/python3
"""12-pascal_triangle Module"""


def pascal_triangle(n):
    """
    Pascal triangle of size n
    :param n: is the size of the triangle
    :return: list of list of integers representing the triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
