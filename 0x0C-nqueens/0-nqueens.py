#!/usr/bin/python3
""" by Facundo Diaz """

import sys


def check(res, pos):
    """ checks with other queens """
    for q in res:
        if q[1] == pos[1]:
            return False
        if (q[0] + q[1]) == (pos[0] + pos[1]):
            return False
        if (q[0] - q[1]) == (pos[0] - pos[1]):
            return False
    return True


def backtracking(res, n, row):
    """ recusive """
    if (row == n):
        print(res)
    else:
        for col in range(n):
            pos = [row, col]
            if check(res, pos):
                res.append(pos)
                backtracking(res, n, row + 1)
                res.remove(pos)


def main(n):
    """ main """
    res = []
    backtracking(res, n, 0)

if _name_ == '_main_':
    """ aaa """
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    code = sys.argv[1]
    if not code.isdigit():
        print('N must be a number')
        sys.exit(1)
    code = int(code)
    if code < 4:
        print('N must be at least 4')
        sys.exit(1)

    main(code)