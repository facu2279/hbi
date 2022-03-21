#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2022"""


from sys import argv
from sys import exit as salida

def test(res, pos):
    """  """
    for i in res:
        if i[1] == pos[1]:
            return False
        if (i[0] + i[1]) == (pos[0] + pos[1]):
            return False
        if (i[0] - i[1]) == (pos[0] - pos[1]):
            return False
    return True

def iterar(res, n, row):
    """ recusive """
    if (row == n):
        print(res)
    else:
        for col in range(n):
            pos = [row, col]
            if test(res, pos):
                res.append(pos)
                iterar(res, n, row + 1)
                res.remove(pos)

def salir(msg):
    print(msg)
    exit(1)

def main():
    """ main """
    if len(argv) != 2:
        salir("Usage: nqueens N")
    num = argv[1]
    if not num.isdigit():
        salir("N must be a number")
    num = int(num)
    if num < 4:
        salir('N must be at least 4')
    res = []
    iterar(res, num, 0)

if _name_ == '_main_':
    """ inicio """
    main()