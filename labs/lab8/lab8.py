"""
Name: Harrison Penley
lab8.py
"""

from encrypt import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    i = 1
    for line in infile:
        new_line = line.split()
        for word in new_line:
            outfile.write(str(i) + " " + word + "/n")
            i += 1


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write(" ".join(new_line) + "/n")


def calc_check_sum(isbn):
    acc = 0
    isbn = str(isbn)
    isbn = isbn.split()
    for i in range(len(isbn)):
        num = int(isbn[i] * (10 - i))
        acc = acc + num
    return acc % 11


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        outfile.write(line + "/n")


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line + "/n")


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    padfile = open(pad, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode_better(line, padfile.read())
        outfile.write(new_line + "/n")


def main():
    number_words("walrus.txt", "new_walrus.txt")
    hourly_wages("employees.txt", "new_wages.txt")
    calc_check_sum(1072946520)
    send_message("message.txt", "alex")
    send_safe_message("message.txt", "alex", "cheese")
    send_uncrackable_message("message.txt", "alex", "pad.txt")
    pass


main()
