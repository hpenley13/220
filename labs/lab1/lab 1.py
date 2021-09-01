"""
Name: Harrison Penley

Problem: this calculates the area of a rectangle,
the volume of a rectangle, the percentage of shots made,
how much you paid for x pounds of coffee, and converts
kilometers to miles.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


calc_rec_area()


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


calc_volume()


def shooting_percentage():
    shots = eval(input("Enter how many shots you took: "))
    shotsmade = eval(input("Enter how many shots you made: "))
    percentage = (shotsmade / shots) * 100
    print("Shot Percentage =", percentage)


shooting_percentage()



def coffee():
    pounds = eval(input("how many pounds of coffee did you buy: "))
    total = 10.50 * pounds + .86 * pounds + 1.50
    print("total cost =", total)


coffee()


def kilometers_to_miles():
    miles = eval(input("how many miles will you travel: "))
    conversion = miles * 1.61
    print(miles,"miles is equal to",conversion,"kilometers")


kilometers_to_miles()

