import string
import math
import random
import os

os.system('cls')
def colandrow():
    dig = string.digits
    while True:
        no = 1
        col = input("select amount of columns (min 6)\n").strip()
        for i in col:
            if i.isdigit():
                no = 0
        if no != 1:
            break
    col = int(col)
    if col < 6:
        col = 6
    while True:
        no = 1
        row = input("select amount of rows (min 6)\n").strip()
        for i in row:
            if i.isdigit():
                no = 0
        if no != 1:
            break
    row = int(row)
    if row < 6:
        row = 6
    return (col, row)

while True:
    w = 0
    s = 0
    a = 0
    d = 1
    snakesize = 1
    board = {f"r{-1}":[]}
    columns, rows = colandrow()
    for i in range(rows):
        board[f"r{i}"] = []
        board[f"r{i}"].append(-2)
        for z in range(columns):
            board[f"r{i}"].append(0)
        board[f"r{i}"].append(-2)
        board[f"r{i}"].append(-3)
    board[f"r{rows}"] = []
    for i in range(columns):
        board[f"r{-1}"].append(-2)
        board[f"r{rows}"].append(-2)
    board[f"r{rows}"].extend([-2, -2, -3])
    board[f"r{-1}"].extend([-2, -2, -3])
    board[f"r{rows // 2}"][columns // 3] = 1
    board[f"r{rows // 2}"].reverse()
    board[f"r{rows // 2}"][(columns // 3) + 1] = -1
    board[f"r{rows // 2}"].reverse()
    wherer = rows // 2
    wherec = board[f"r{rows // 2}"].index(1)
    wfoodr = rows // 2
    wfoodc = board[f"r{rows // 2}"].index(-1)
    snake = {f"segment{snakesize}":[wherer, wherec]}
    snakekeys = list(snake.keys())
    print(snakekeys)
    print("controls are w (forward) a (left) s (backward) d (right)")
    for i in board:
        for sp in board[i]:
            if sp == 0:
                print("-", end=" ")
            elif sp == 1:
                print("O", end=" ")
            elif sp >= 2:
                print("#", end=" ")
            elif sp == -1:
                print("@", end=" ")
            elif sp == -2:
                print("X", end=" ")
            elif sp == -3:
                print("")
    while True:
        new = 0
        move = input().strip().lower()
        os.system('cls')
        if move == "w" and s == 0:
            w = 1
            a, d = 0, 0
        if move == "a" and d == 0:
            a = 1
            w, s = 0, 0
        if move == "s" and w == 0:
            s = 1
            a, d = 0, 0
        if move == "d" and a == 0:
            d = 1
            w, s = 0, 0
        print(w, a, s, d, snake, snakekeys)
        if w == 1:
            board[f"r{wherer - 1}"][wherec] = 1
            if (wherer - 1 == wfoodr) and (wherec == wfoodc):
                new = 1
            for i in range(snakesize):
                if snakesize - i == snakesize:
                    if new == 1 and snakesize == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                elif i + 1 - snakesize == 0:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
                    if new == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                        for sn in range(snakesize):
                            if snakesize - sn != 1:
                                snake[snakekeys[(snakesize - sn) - 1]] = [snake[snakekeys[(snakesize - sn) - 2]][0], snake[snakekeys[(snakesize - sn) - 2]][1]]
                else:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
            if new == 1:
                snakesize += 1
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = snakesize
            else:
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = 0
                for i in range(snakesize):
                    if snakesize - i != 1:
                        snake[snakekeys[(snakesize - i) - 1]] = [snake[snakekeys[(snakesize - i) - 2]][0], snake[snakekeys[(snakesize - i) - 2]][1]]
            snake[f"segment{1}"][0] = wherer - 1
            wherer = wherer - 1
        if a == 1:
            board[f"r{wherer}"][wherec - 1] = 1
            if (wherer == wfoodr) and (wherec - 1 == wfoodc):
                new = 1
            for i in range(snakesize):
                if snakesize - i == snakesize:
                    if new == 1 and snakesize == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                elif i + 1 - snakesize == 0:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
                    if new == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                        for sn in range(snakesize):
                            if snakesize - sn != 1:
                                snake[snakekeys[(snakesize - sn) - 1]] = [snake[snakekeys[(snakesize - sn) - 2]][0], snake[snakekeys[(snakesize - sn) - 2]][1]]
                else:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
            if new == 1:
                snakesize += 1
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = snakesize
            else:
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = 0
                for i in range(snakesize):
                    if snakesize - i != 1:
                        snake[snakekeys[(snakesize - i) - 1]] = [snake[snakekeys[(snakesize - i) - 2]][0], snake[snakekeys[(snakesize - i) - 2]][1]]
            snake[f"segment{1}"][1] = wherec - 1
            wherec = wherec - 1
        if s == 1:
            board[f"r{wherer + 1}"][wherec] = 1
            if (wherer + 1 == wfoodr) and (wherec == wfoodc):
                new = 1
            for i in range(snakesize):
                if snakesize - i == snakesize:
                    if new == 1 and snakesize == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                elif i + 1 - snakesize == 0:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
                    if new == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                        for sn in range(snakesize):
                            if snakesize - sn != 1:
                                snake[snakekeys[(snakesize - sn) - 1]] = [snake[snakekeys[(snakesize - sn) - 2]][0], snake[snakekeys[(snakesize - sn) - 2]][1]]
                else:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
            if new == 1:
                snakesize += 1
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = snakesize
            else:
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = 0
                for i in range(snakesize):
                    if snakesize - i != 1:
                        snake[snakekeys[(snakesize - i) - 1]] = [snake[snakekeys[(snakesize - i) - 2]][0], snake[snakekeys[(snakesize - i) - 2]][1]]
            snake[f"segment{1}"][0] = wherer + 1
            wherer = wherer + 1
        if d == 1:
            board[f"r{wherer}"][wherec + 1] = 1
            if (wherer == wfoodr) and (wherec + 1 == wfoodc):
                new = 1
            for i in range(snakesize):
                if snakesize - i == snakesize:
                    if new == 1 and snakesize == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                elif i + 1 - snakesize == 0:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
                    if new == 1:
                        snake[f"segment{i + 2}"] = [snake[snakekeys[i]][0], snake[snakekeys[i]][1]]
                        for sn in range(snakesize):
                            if snakesize - sn != 1:
                                snake[snakekeys[(snakesize - sn) - 1]] = [snake[snakekeys[(snakesize - sn) - 2]][0], snake[snakekeys[(snakesize - sn) - 2]][1]]
                else:
                    board[f"r{snake[snakekeys[i - 1]][0]}"][snake[snakekeys[i - 1]][1]] = i + 1
            if new == 1:
                snakesize += 1
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = snakesize
            else:
                board[f"r{snake[snakekeys[-1]][0]}"][snake[snakekeys[-1]][1]] = 0
                for i in range(snakesize):
                    if snakesize - i != 1:
                        snake[snakekeys[(snakesize - i) - 1]] = [snake[snakekeys[(snakesize - i) - 2]][0], snake[snakekeys[(snakesize - i) - 2]][1]]
            snake[f"segment{1}"][1] = wherec + 1
            wherec = wherec + 1
        snakekeys = list(snake.keys())
        if ((wherer == -1) or (wherer == rows)) or ((wherec == 0) or (wherec == columns + 1)):
            print("you died womp womp")
            break
        elif board[f"r{wherer}"][wherec] >= 2:
            print("you died womp womp")
            break
        if new == 1:
            while True:
                wfoodr = random.randint(0, rows)
                wfoodc = random.randint(1, columns)
                if board[f"r{wfoodr}"][wfoodc] == 0:
                    board[f"r{wfoodr}"][wfoodc] = -1
                    break
        print(w, a, s, d, snake, snakekeys)
        for i in board:
            for sp in board[i]:
                if sp == 0:
                    print("-", end=" ")
                elif sp == 1:
                    print("O", end=" ")
                elif sp >= 2:
                    print("#", end=" ")
                elif sp == -1:
                    print("@", end=" ")
                elif sp == -2:
                    print("X", end=" ")
                elif sp == -3:
                    print("")