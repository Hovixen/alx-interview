#!/usr/bin/python3
""" Rotating 2d matix in 90 degrees """


def rotate_2d_matrix(matrix):
    """ function uses the reverse and transpose method
        to rotate a 2d matrix 90 degrees
    """

    a = len(matrix)
    # for clockwise, handle the transpose first before the reverse
    for m in range(a):
        for n in range(m, a):
            matrix[m][n], matrix[n][m] = matrix[n][m], matrix[m][n]

    for i in range(a):
        matrix[i].reverse()
