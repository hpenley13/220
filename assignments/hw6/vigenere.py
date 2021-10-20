"""
Harrison Penley
vigenere.py

problem: create a graphical UI that allows for the inputs necessary to encrypt a vigenere cypher.

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import GraphWin, Text, Point, Entry

def code(message, keyword):
    c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = str(message)
    message = message.upper()
    message = message.replace(" ", "")
    keyword = str(keyword)
    keyword = keyword.upper()
    acc = 0
    stringacc = ""
    for i in range(len(message)):
        m1 = c.find(message[i])
        k1 = c.find(keyword[acc])
        if m1 + k1 > 25:
            total = m1 + k1 - 26
        else:
            total = m1 + k1
        stringacc = stringacc + c[total]
        acc = acc + 1
        if acc > len(keyword) - 1:
            acc = 0

    return stringacc


def main():
    win = GraphWin("Vigenere Cypher", 500, 500)
    win.setCoords(0, 0, 10, 10)
    message_text = Text(Point(5, 9), "Message to Encode:")
    message_text.draw(win)
    message = Entry(Point(5, 8), 35)
    message.draw(win)
    keyword_text = Text(Point(5, 6), "Keyword:")
    keyword_text.draw(win)
    keyword = Entry(Point(5, 5), 25)
    keyword.draw(win)
    instruction = Text(Point(5, 4), "Click anywhere to encode.")
    instruction.draw(win)
    win.getMouse()
    result_text = Text(Point(5, 3), "Resulting Message Will Appear Here:")
    result_text.draw(win)
    result = Text(Point(5, 2), code(message.getText(), keyword.getText()))
    result.draw(win)
    finish = Text(Point(5, 1), "Click anywhere to close once the results are shown.")
    finish.draw(win)
    win.getMouse()
    #for i in range(len(message_string)):
        #c = message_string[i]
        #key = keyword_string[i]
        #key = ord(key) - 97
        #c = ord(c) + key
        #acc = acc + chr(c)
    #return acc
    #result_text = Text(Point(5, 3), "Resulting Message:")
    #result_text.draw(win)
    #result = Text(Point(5, 2), acc)
    #result.draw(win)
    #finish = Text(Point(5, 1), "Click anywhere to close.")
    #finish.draw(win)

if __name__ == "__main__":
    main()