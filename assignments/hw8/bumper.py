"""
Harrison Penley
bumper.py

Problem: Create a graphics window that displays a randomly launched set of orbs that
deflect off of the walls and off of one another creating a random pattern.

I certify that this code is entirely my own work
"""

from time import sleep
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb



def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball1, ball2):
    ball1center = ball1.getCenter()
    ball2center = ball2.getCenter()
    ball1x = ball1center.getX()
    ball2x = ball2center.getX()
    ball1y = ball1center.getY()
    ball2y = ball2center.getY()
    ball1rad = ball1.getRadius()
    ball2rad = ball2.getRadius()
    distance = (((ball2x - ball1x)**2) + ((ball2y - ball1y)**2)) ** 1 / 2
    radius = ball1rad + ball2rad
    if distance <= radius:
        result = True
        get_random_color(ball1)
        get_random_color(ball2)
    else:
        result = False
    return result


def hit_vertical(ball, win):
    ballcenter = ball.getCenter()
    ballx = ballcenter.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    if ballx <= radius or ballx >= (width - radius):
        result = True
        get_random_color(ball)
    else:
        result = False
    return result


def hit_horizontal(ball, win):
    ballcenter = ball.getCenter()
    bally = ballcenter.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    if bally <= radius or bally >= (height - radius):
        result = True
        get_random_color(ball)
    else:
        result = False
    return result


def get_random_color(circle):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    circle.setFill(color_rgb(red, green, blue))


def main():
    win = GraphWin("bumper cars!", 500, 500)
    width = win.getWidth()
    height = win.getHeight()
    radius = 20
    ball1 = Circle(Point(radius + 30, height / 2), radius)
    ball2 = Circle(Point(width - (radius + 30), height / 2), radius)
    get_random_color(ball1)
    get_random_color(ball2)
    ball1.draw(win)
    ball2.draw(win)
    v1x = get_random(10)
    v1y = get_random(10)
    v2x = get_random(10)
    v2y = get_random(10)
    velocity = [[v1x, v1y], [v2x, v2y]]

    for _ in range(500):
        sleep(.04)
        if hit_vertical(ball1, win):
            velocity[0][0] = - velocity[0][0]
        if hit_vertical(ball2, win):
            velocity[1][0] = - velocity[1][0]
        if hit_horizontal(ball1, win):
            velocity[0][1] = - velocity[0][1]
        if hit_horizontal(ball2, win):
            velocity[1][1] = - velocity[1][1]
        if did_collide(ball1, ball2):
            velocity[0][0] = - velocity[0][0]
            velocity[1][0] = - velocity[1][0]
            velocity[0][1] = - velocity[0][1]
            velocity[1][1] = - velocity[1][1]

        ball1.move(velocity[0][0], velocity[0][1])
        ball2.move(velocity[1][0], velocity[1][1])


if __name__ == "__main__":
    main()
