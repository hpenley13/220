"""
Name: Harrison Penley
lab5.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    dx1 = p1.getX() - p2.getX()
    dx2 = p2.getX() - p3.getX()
    dx3 = p3.getX() - p1.getX()
    dy1 = p1.getY() - p2.getY()
    dy2 = p2.getY() - p3.getY()
    dy3 = p3.getY() - p1.getY()
    side1 = math.sqrt((dx1 ** 2) + (dy1 ** 2))
    side2 = math.sqrt((dx2 ** 2) + (dy2 ** 2))
    side3 = math.sqrt((dx3 ** 2) + (dy3 ** 2))
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    # area = math.sqrt((p1.getX - p2.getX) * (p2.getX - p3.getX) * (p3.getX - p1.getX)
    triangle.draw(win)
    perimetertext = Text(Point(250, 25), perimeter)
    areatext = Text(Point(250, 45), area)
    perimetertext.draw(win)
    areatext.draw(win)


    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(210, 50), 5)
    green_box = Entry(Point(210, 70), 5)
    blue_box = Entry(Point(210, 90), 5)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)
    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        blue = int(blue_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = input("type out a string: ")
    l = len(s) - 1
    print(s[0])
    print(s[l])
    print(s[2:6])
    print(s[0]+s[l])
    print(s[0] * 3, s[1] * 3, s[2] * 3)
    for c in s:
        print(c)
    print(len(s))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + [values[0]]
    print(x)
    x = [values[0]] + [values[2]] + [float(values[-1])]
    print(x)
    x = values[0] + values[2] + float(values[-1])
    print(x)
    x = len(values)
    print(x)


def another_series():

    terms = eval(input("how many terms do you want?: "))
    acc = 0
    for i in range(terms):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc = acc + y
    print()
    print("sum =", acc,)



def main():
    #target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
