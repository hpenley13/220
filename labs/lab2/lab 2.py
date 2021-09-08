"""
name: Harrison Penley
lab 2.py

Problem: this solves for the sums of three, creates a multiplication table, solves for the area of a triangle,
solves for the sum of squares, and solves for a power.
"""

import math

def sum_of_threes():
    bound = eval(input("what is your bound?: "))
    acc = 0
    for i in range(0, bound + 1, 3):
        acc = acc + i
    print(acc)


sum_of_threes()


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()


multiplication_table()


def triangle_area():
    a = eval(input("enter side a: "))
    b = eval(input("enter side b: "))
    c = eval(input("enter side c: "))
    s = (a + b + c)/2
    A_nosquare = s * (s - a) * (s - b) * (s - c)
    A = math.sqrt(A_nosquare)
    print(A,"is the area of this triangle")


triangle_area()


def sumSquares():
    lower = eval(input("what is the lower bound?: "))
    upper = eval(input("what is the upper bound?: "))
    acc = 0
    for i in range(lower, upper+1):
       acc = acc + i ** 2
    print(acc)


sumSquares()


def power():
    base = eval(input("what is the base?: "))
    exp = eval(input("what is the exponent?: "))
    acc = 1
    for i in range(exp):
        acc = acc * base
    print(base,"^",exp,"=",acc)


power()



