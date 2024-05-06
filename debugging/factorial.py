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
    print(f"The factorial of {sys.argv[1]} is: {f}")
else:
    print("Please provide an argument.")
