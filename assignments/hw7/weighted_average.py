"""
Harrison Penley
weighted_average.py

Problem: create a program that can read from a text file

I certify that this program is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    avg = 0
    time = 0
    colon = 0
    for line in in_file:
        acc = 0
        acc2 = 0
        word = line.split()
        new_line = line.split(":")
        studentname = new_line[0]
        for i in range(len(word)):
            if word[i].find(":") > -1:
                colon = i
                word[i] = word[i].replace(":", "")
        for i in range(colon + 1, len(word), 2):
            acc = acc + int(word[i])
        if acc > 100:
            out_file.write(studentname + "'s average: Error: The weights are more than 100." + "\n")
        elif acc < 100:
            out_file.write(studentname + "'s average: Error: The weights are less than 100." + "\n")
        else:
            for i in range(colon + 1, len(word), 2):
                acc2 = acc2 + (int(word[i]) * int(word[i + 1]))
            studentsavg = acc2 / 100
            time += 1
            avg = (avg + studentsavg)
            out_file.write(studentname + "'s average: {:.1f}".format(studentsavg) + "\n")
    if time == 0:
        avg = 0
    else:
        avg = avg / time
    out_file.write("Class average: {:.1f}".format(avg))


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()