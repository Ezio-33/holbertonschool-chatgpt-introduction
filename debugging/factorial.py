#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return -1
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        sys.exit(1)

    n = int(sys.argv[1])
    result = factorial(n)
    if result == -1:
        print("Le nombre doit être supérieur ou égal à zéro.")
    else:
        print(f"Le facteuriel de {n} est {result}.")