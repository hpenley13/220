"""
Harrison Penley
Lab 3.py

This problem
"""


def average():
    hw = eval(input("how many graded assignments were there?: "))
    acc = 0
    for i in range(hw):
        grades = eval(input("enter your grade for HW" + str(i + 1)))
        acc = acc + grades / hw
    print(acc)


average()


def tip_jar():
    acc = 0
    for i in range(5):
        tip = eval(input("how much are you donating?: "))
        acc = acc + tip
    print(acc)


tip_jar()


def newton():
    x = eval(input("what number do we approximate the root of?: "))
    refine = eval(input("how many times would you like to improve the approximation?: "))
    approx = x / 2
    for i in range(refine):
        approx = ((approx + x / approx) / 2)
    print(approx)


newton()


def sequence():
    seq = eval(input("how many numbers in the sequence do you want to see?: "))

    for i in range(1, seq + 1):
        y = 1 + (i // 2 * 2)
        print(y)


sequence()


def pi():
    n = eval(input("how many terms are in the series to approximate pi?: "))
    acc = 1
    for i in range(n):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        acc = (num / denom) * acc
    print(acc * 2)


pi()





