"""
Name: Harrison Penley
lab13.py
"""


from graphics import Rectangle, Point


def is_in_binary(search_val, values):
    mid = values[len(values) // 2]
    while search_val != mid and len(values) != 1:
        if mid > search_val:
            values = values[:mid]
        else:
            values = values[mid + 1:]
        mid = values[len(values) // 2]
    if search_val == mid:
        return True
    else:
        return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < values[i]:
                lowest = values[j]
                pos = j
        values[i], values[j] = values[j], values[i]


def get_area(rect):
    p1 = rect.getP1
    p2 = rect.getP2
    w = abs(p1.getX - p2.getX)
    h = abs(p1.getY - p2.getY)
    return w * h


def rect_sort(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]
    print(areas)


def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    for i in range(len(data)):
        if int(data[i]) > 830:
            print("current second is", i + 1)
            print("alert! the trading has exceeded 830!")
        elif int(data[i]) > 500:
            print("current second is", i + 1)
            print("alert! the trading has exceeded 500!")


def main():
    print(is_in_binary(3, [1, 2, 3, 4, 5, 6]))
    x = [3, 4, 1, 6]
    selection_sort(x)
    print(x)
    y = [Rectangle(Point(0, 0), Point(20, 20)), Rectangle(Point(0, 0), Point(5, 5)),
         Rectangle(Point(0, 0), Point(15, 15))]
    rect_sort(y)
    trade_alert("trades.txt")

    pass


main()
