"""
Name: Harrison Penley
lab9.py
"""

from graphics import *
import math


def addten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareeach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumlist(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def tonumbers(strlist):
    for i in range(len(strlist)):
        strlist[i] = float(strlist[i])


def writesumofsquares():
    infile = input("what's the name of the input file: ")
    infile = open(infile, "r")
    outfile = open("output.txt", "w+")
    for line in infile:
        numlist = line.split()
        tonumbers(numlist)
        squareeach(numlist)
        s = sumlist(numlist)

        outfile.write("sum =" + str(s) + "\n")


def starter():
    weight = eval(input("what is the weight? "))
    wins = eval(input("how many games has he won? "))
    if weight > 150 and weight < 160 and wins >= 5:
        print("he is a starter.")
    elif weight > 199 or wins > 20:
        print("he is a starter")
    else:
        print("he won't be a starter.")


def leapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circleoverlap():
    win = GraphWin("circle overlap test", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) **2)
    circle1 = Circle(p1, radius1)
    circle1.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    if radius1 + radius2 > distance:
        display = Text(Point(200, 30), "the circles do overlap.")
        display.draw(win)
    else:
        display = Text(Point(200, 30), "the circles do not overlap.")
        display.draw(win)

    win.getMouse()
    win.close()


def main():
    x = [1, 2, 3]
    addten(x)
    print(x)
    squareeach(x)
    print(x)
    sumlist(x)
    print(x)
    tonumbers(x)
    print(x)
    writesumofsquares()
    starter()
    leapyear(2000)
    circleoverlap()
    # add other function calls here
    pass


main()
