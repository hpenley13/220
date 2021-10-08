"""
Harrison Penley
greeting.py

Problem: use the graphics library to draw a heart on the window.

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

import time
from graphics import GraphWin, Circle, Text, Polygon, Rectangle, Point

def main():
    win = GraphWin("Greetings Window", 500, 500)
    win.setCoords(0, 0, 10, 10)
    greetingmessage = Text(Point(5, 8), "Happy Valentine's Day!! <3")
    win.getMouse()
    greetingmessage.draw(win)
    circle1 = Circle(Point(6.15, 6), 1.01)
    circle2 = Circle(Point(7.85, 6), 1.01)
    circle1.draw(win)
    circle2.draw(win)
    triangle = Polygon(Point(5, 6), Point(9, 6), Point(7, 3))
    triangle.draw(win)
    cover = Rectangle(Point(6.25, 5.25), Point(7.4, 4.65))
    cover.draw(win)
    circle1.setFill("red")
    circle2.setFill("red")
    triangle.setFill("red")
    circle1.setOutline("red")
    circle2.setOutline("red")
    triangle.setOutline("red")
    cover.setFill("red")
    cover.setOutline("red")

    arrowbody = Rectangle(Point(1, 5), Point(3, 4.85))
    arrowhead = Polygon(Point(3, 4.8), Point(3, 5.05), Point(3.25, 4.925))
    arrowbody.draw(win)
    arrowhead.draw(win)
    arrowbody.setFill("gray")
    arrowhead.setFill("gray")
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)
    time.sleep(0.1)
    arrowbody.move(0.33, 0)
    arrowhead.move(0.33, 0)

    cover = Rectangle(Point(6.25, 5.25), Point(7.4, 4.65))
    cover.draw(win)
    cover.setFill("red")
    cover.setOutline("red")

    byebye = Text(Point(5, 2), "Click anywhere to Exit")
    byebye.draw(win)
    win.getMouse()

if __name__ == "__main__":
    main()
