#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2022"""


from sys import argv, exit

<<<<<<< HEAD
def test(res, pos):
    """  """
=======

def test(res, pos):
    """ test """
>>>>>>> a270bea3dab26a7f166465453086ac54409f5c99
    for i in res:
        if i[1] == pos[1]:
            return False
        if (i[0] + i[1]) == (pos[0] + pos[1]):
            return False
        if (i[0] - i[1]) == (pos[0] - pos[1]):
            return False
    return True

<<<<<<< HEAD
def iterar(res, n, row):
    """ recusive """
=======

def iterar(res, n, row):
    """ iterar """
>>>>>>> a270bea3dab26a7f166465453086ac54409f5c99
    if (row == n):
        print(res)
    else:
        for col in range(n):
            pos = [row, col]
            if test(res, pos):
                res.append(pos)
                iterar(res, n, row + 1)
                res.remove(pos)

<<<<<<< HEAD
def salir(msg):
    print(msg)
    exit(1)

def main():
    """ main """
=======

def salir(msg):
    """ salir """
    print(msg)
    exit(1)


def inicio():
    """ inicio """
>>>>>>> a270bea3dab26a7f166465453086ac54409f5c99
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

<<<<<<< HEAD
if __name__ == '__main__':
    """ inicio """
    main()
=======

if __name__ == '__main__':
    """ inicio """
    inicio()
>>>>>>> a270bea3dab26a7f166465453086ac54409f5c99
