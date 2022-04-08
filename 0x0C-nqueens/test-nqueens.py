#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2022"""
import os

print("TEST ERRORS\n---------")
comando = './0-nqueens.py'
print("TEST 1:\n", comando)
print("EXPECTED:\nUsage: nqueens N")
print("OUTPUT:")
os.system(comando)

comando = './0-nqueens.py a'
print("TEST 1:\n", comando)
print("EXPECTED:\nN must be a number")
print("OUTPUT:")
os.system(comando)

comando = './0-nqueens.py 3'
print("TEST 1:\n", comando)
print("EXPECTED:\nN must be at least 4")
print("OUTPUT:")
os.system(comando)

print("TEST SUCCESS\n---------")
comando = './0-nqueens.py 4'
print("TEST 1:\n", comando)
salida = "[[0, 1], [1, 3], [2, 0], [3, 2]]\n[[0, 2], [1, 0], [2, 3], [3, 1]]"
print("EXPECTED:\n" + salida)
print("OUTPUT:")
os.system(comando)

comando = './0-nqueens.py 6'
print("TEST 1:\n", comando)
salida = "[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]\n[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]\n[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]\n[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]"
print("EXPECTED:\n" + salida)
print("OUTPUT:")
os.system(comando)