#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """ a fun rotate 2d matrix 90 degree"""
    matrix_len = len(matrix)
    copy_matrix = [[ matrix[x][y] for y in range(matrix_len)] for x in range(matrix_len)]
    for x in range(matrix_len):
        for y in range(matrix_len):
            matrix[y][matrix_len-1-x] = copy_matrix[x][y]
