"""
Harrison Penley
button.py

Problem: Use this file to create a user-defined class of a Button
that will be used in the creation of the three door guessing game
in threedoorgame.py

I certify that this is entirely my own work.
"""


from graphics import Text, Point


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(Point(self.shape.getP1().getX() + 40,
                               self.shape.getP1().getY() + 35), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() \
                and self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY():
            return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
