"""
Name: Harrison Penley
lab10.py
"""


def build():
    return list(range(1, 10))


def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], board[n+1], board[n+2], sep="|")

        print(10 * "-")


def place(board, pos, piece):
    if piece == "x" or piece == "o":
        board[pos - 1] = piece


def legal(board, pos):
    if pos <= 9 and pos >= 0:
        return True
    return False


def iswon(board, piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            continue
        if board[i+6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True

    return False


def over(board):
    if iswon(board, "x"):
        return True
    elif iswon(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def play():
    board = build()
    while True:
        display(board)
        pos = eval(input("X's Turn, what position do you want?"))
        if legal(board, pos) == True:
            place(board, pos, "x")
            if over(board) == True:
                iswon(board, "x")
                iswon(board, "o")
                if iswon(board, "x") == True:
                    print("X Wins")
                    break
                elif iswon(board, "o") == True:
                    print("O Wins")
                    break
                else:
                    display(board)
                    print("This is a Tie.")
                    break
            else:
                display(board)
                pos = eval(input("O's Turn, what position do you want?"))
                if legal(board, pos) == True:
                    place(board, pos, "o")
                    if over(board) == True:
                        iswon(board, "x")
                        iswon(board, "o")
                        if iswon(board, "x") == True:
                            print("X Wins")
                            break
                        elif iswon(board, "o") == True:
                            print("O Wins")
                            break
                        else:
                            print("This is a Tie.")
                            break
                    else:
                        continue

    print("This Game is Over.")


def main():
    play()
    pass


main()
