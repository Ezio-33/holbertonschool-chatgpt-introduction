#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) > 1:
    f = factorial(int(sys.argv[1]))
    print(f"La factorielle de {sys.argv[1]} est: {f}")
else:
    print("Veuillez fournir un argument.")
