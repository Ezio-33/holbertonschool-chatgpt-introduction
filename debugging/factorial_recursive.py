#!/usr/bin/python3
import sys

"""
Calcule la factorielle d'un nombre donné.

Paramètres:
- n (int): Le nombre pour lequel la factorielle doit être calculée.

Return:
- int: La factorielle du nombre donné.

Exemple:
>>> factorial(5)
120
"""


def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
