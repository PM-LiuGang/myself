# -*-coding:utf8 -*-

finish = False
flagnum = 1
flagch = '×'
x = 0
y = 0
print('\033[1;37;41m----------简易五子棋游戏（控制台版）-----------\033[0m')

# 基础棋盘
checkboard = []
for i in range(10):
    checkboard.append([])
    for j in range(10):
        checkboard[i].append('-')

print('\033[1;30;46m----------------------\033[0m')
print('  1 2 3 4 5 6 7 8 9 10')
for i in range(len(checkboard)):
    print(chr(i + ord('A')) + ' ', end='')
    for j in range(len(checkboard[i])):
        print(checkboard[i][j] + ' ', end='')
    print()
print('----------------------')


def msg():
    '''
    # 打印出最终的棋盘
    print('\033[1;37;41m----------------------\033[0m')
    print('  1 2 3 4 5 6 7 8 9 10')
    for i in range(len(checkboard)):
        print(chr(i + ord('A')) + ' ', end='')
        for j in range(len(checkboard[i])):
            print(checkboard[i][j] + ' ', end='')
        print()
    print('----------------------')
    '''

    if flagnum == 1:
        print('\033[32m × *** 棋胜利！***\033[0m')
    else:
        print('\033[32m √ *** 棋胜利! ***\033[0m')


while not finish:
    if flagnum == 1:
        flagch = '×'
        print('\033[1;37;45m请 × 输入棋子坐标(例如A1): \033[0m', end='')
    else:
        flagch = '√'
        print('\033[1;37;45m请 √ 输入棋子坐标(例如A1): \033[0m', end='')

    str = input('').upper()
    ch = str[0]
    x = ord(ch) - 65
    y = int(str[1:]) - 1

    if x < 0 or x > 9 or y < 0 or y > 9:
        print('\033[31m***你输入的坐标有误请重新输入！***\033[0m')
        continue

    if checkboard[x][y] == '-':
        if flagnum == 1:
            checkboard[x][y] = '×'
        else:
            checkboard[x][y] = '√'
    else:
        print('\033[31m*********你输入位置已经有其他棋子，请重新输入！ \033[0m')
        continue

    print('\033[1;30;46m----------------------\033[0m')
    print('  1 2 3 4 5 6 7 8 9 10')
    for i in range(len(checkboard)):
        print(chr(i + ord('A')) + ' ', end='')
        for j in range(len(checkboard[i])):
            if i == x and j == y:
                print(checkboard[x][y] + ' ', end='')
            else:
                print(checkboard[i][j] + ' ', end='')
        print()
    print('----------------------')

    # 判断棋子左侧
    if y - 4 >= 0:
        if (checkboard[x][y - 1] == flagch
                and checkboard[x][y - 2] == flagch
                and checkboard[x][y - 3] == flagch
                and checkboard[x][y - 4] == flagch):
            finish = True
            msg()

    # 判断棋子右侧
    if y + 4 <= 9:
        if (checkboard[x][y + 1] == flagch
                and checkboard[x][y + 2] == flagch
                and checkboard[x][y + 3] == flagch
                and checkboard[x][y + 4] == flagch):
            finish = True
            msg()

    # 判断棋子上方
    if (x - 4 >= 0):
        if (checkboard[x - 1][y] == flagch
                and checkboard[x - 2][y] == flagch
                and checkboard[x - 3][y] == flagch
                and checkboard[x - 4][y] == flagch):
            finish = True
            msg()

    # 判断棋子下方
    if (x + 4 <= 9):
        if (checkboard[x + 1][y] == flagch
                and checkboard[x + 2][y] == flagch
                and checkboard[x + 3][y] == flagch
                and checkboard[x + 4][y] == flagch):
            finish = True
            msg()

    # 判断棋子右上方向
    if (x - 4 >= 0 and y - 4 >= 0):
        if (checkboard[x - 1][y - 1] == flagch
                and checkboard[x - 2][y - 2] == flagch
                and checkboard[x - 3][y - 3] == flagch
                and checkboard[x - 4][y - 4] == flagch):
            finish = True
            msg()

    # 判断棋子右下方向
    if (x + 4 <= 9 and y - 4 >= 0):
        if (checkboard[x + 1][y - 1] == flagch
                and checkboard[x + 2][y - 2] == flagch
                and checkboard[x + 3][y - 3] == flagch
                and checkboard[x + 4][y - 4] == flagch):
            finish = True
            msg()

    # 判断棋子左上方向
    if (x - 4 >= 0 and y + 4 <= 9):
        if (checkboard[x - 1][y + 1] == flagch
                and checkboard[x - 2][y + 2] == flagch
                and checkboard[x - 3][y + 3] == flagch
                and checkboard[x - 4][y + 4] == flagch):
            finish = True
            msg()

    # 判断棋子左下方向
    if (x + 4 <= 9 and y + 4 <= 9):
        if (checkboard[x + 1][y + 1] == flagch
                and checkboard[x + 2][y + 2] == flagch
                and checkboard[x + 3][y + 3] == flagch
                and checkboard[x + 4][y + 4] == flagch):
            finish = True
            msg()

    flagnum *= -1