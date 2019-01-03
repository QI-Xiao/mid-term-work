# -*- coding: utf-8 -*-

import random
import tkinter as tk
from PIL import Image, ImageTk

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('X or O?')
        letter = input().upper() # upper, 字符串小写变大写
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playLetter = 'O'
    else:
        playLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    if isSpaceFree(board, 5)
        return 5

    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True
#
# class App:
#     def __init__(self, root):
#         frame = tk.Frame(root)
#         frame.pack()
#         self.hi_there = tk.Button(frame, text='打招呼', fg='blue', command=self.say_hi)
#         self.hi_there.pack(side=tk.LEFT)
#
#     def say_hi(self):
#         print('dajiahao')
#
#
# root = tk.Tk()
# app = App(root)
# root.mainloop()



photo = None
def loadpicture():
    global photo
    if b1['image'] == photo:
        print('aaa')
        # b1['image'] = photo2
    else:
        print('bbb')
        b1['image'] = photo

    # b1 = tk.Button(root, image = photo)


    #tk.Button(root, image='plane.png')

root = tk.Tk()
img1 = Image.open('enemy.png')
XXX = ImageTk.PhotoImage(img1)
img2 =Image.open('plane.png')
OOO = ImageTk.PhotoImage(img2)

b1 = tk.Button(root, command =loadpicture)
for i in range(3):
    for j in range(3):
        tk.Button(root, command=loadpicture).grid(row=i, column=j,ipadx=10, ipady=10,padx=10,pady=10)

# photo = PhotoImage(file='plane.png')

b1.grid(row=0, column=0)


#label = tk.Label(root, text='hello,world')
#label.pack()
#btn = tk.Button(root, text="Click", fg="red", bg="blue")
# root.grid(row=3, column=3)
#btn.pack()
#entry = tk.Entry(root)
#entry.pack()
root.title('井字棋')
root.mainloop()