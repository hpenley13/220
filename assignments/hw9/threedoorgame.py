"""
Harrison Penley
threedoorgame.py

Problem: using the user-developed button class in button.py,
program a guessing game in which 3 doors are presented, one
of which was randomly chosen to be the correct door. Inform
the user if their guess was correct or incorrect and depict
green or red respectively.
"""


from graphics import Rectangle, Point, GraphWin, Text
from button import Button
from random import randint


def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setBackground("orange")
    door1 = Button(Rectangle(Point(110, 370), Point(190, 430)), Text(Point(150, 400), "Door 1"))
    door2 = Button(Rectangle(Point(210, 370), Point(290, 430)), Text(Point(250, 400), "Door 2"))
    door3 = Button(Rectangle(Point(310, 370), Point(390, 430)), Text(Point(350, 400), "Door 3"))
    greetingmessage = Text(Point(250, 200), "Guess which door is the secret one!")
    greetingmessage.draw(win)
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)
    num = randint(1, 3)
    if door1.is_clicked(win.getMouse()) and num == 1:
        door1.color_button("green")
        wintext = Text(Point(250, 250), "You've won! Click to Exit")
        wintext.draw(win)
        win.getMouse()
        win.close()
    elif door1.is_clicked(win.getMouse()) and num != 1:
        door1.color_button("red")
        losetext = Text(Point(250, 250), "You've lost, Click to Exit")
        losetext.draw(win)
        win.getMouse()
        win.close()
    if door2.is_clicked(win.getMouse()) and num == 2:
        door2.color_button("green")
        wintext = Text(Point(250, 250), "You've won! Click to Exit")
        wintext.draw(win)
        win.getMouse()
        win.close()
    elif door2.is_clicked(win.getMouse()) and num != 2:
        door2.color_button("red")
        losetext = Text(Point(250, 250), "You've lost, Click to Exit")
        losetext.draw(win)
        win.close()
    if door3.is_clicked(win.getMouse()) and num == 3:
        door3.color_button("green")
        wintext = Text(Point(250, 250), "You've won! Click to Exit")
        wintext.draw(win)
        win.getMouse()
        win.close()
    elif door3.is_clicked(win.getMouse()) and num != 3:
        door3.color_button("red")
        losetext = Text(Point(250, 250), "You've lost, Click to Exit")
        losetext.draw(win)
        win.close()




if __name__ == "__main__":
    main()


