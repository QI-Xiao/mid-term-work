# -*- coding: utf-8 -*-

import random
import tkinter as tk
from PIL import Image, ImageTk

class GuiTic:
    def __init__(self, root):
        self.bt = tk.Button(root, command=self.loadpicture, state=tk.NORMAL)
        img1 = Image.open('enemy.png')
        img2 = Image.open('plane.png')
        self.XXX = ImageTk.PhotoImage(img1)
        self.OOO = ImageTk.PhotoImage(img2)

    def loadpicture(self):
        self.bt['image'] = self.XXX
        self.bt['state'] = tk.DISABLED
        # print(ButtonTic.index())
        print ('aaa')
        print ('bbb')
        return False




    # def judgeblank(self):
    #     if self.loadpicture == False:
    #         ticplay.ButtonTic.index(self.bt) == None





def ticplay():
    global ButtonTic
    print('aaa')
    ButtonTic = []
    for i in range(3):
        for j in range(3):
            guitic = GuiTic(root)
            ButtonTic.append(guitic)
            guitic.bt.grid(row=i, column=j, ipadx=10, ipady=10, padx=10, pady=10)
    root.title('井字棋')

def whoGoesFirst:
    if


# guitic.loadpicture()

root = tk.Tk()

menubar = tk.Menu(root)
fmenu = tk.Menu(root)
fmenu.add_command(label='人机对战（玩家先）', command=ticplay)
fmenu.add_command(label='人机对战（电脑先）', command=ticplay)
fmenu.add_command(label='人人对战', command=ticplay)
vmenu = tk.Menu(root)
vmenu.add_command(label='重玩', command=ticplay)
vmenu.add_command(label='悔棋')
menubar.add_cascade(label='模式', menu=fmenu)
menubar.add_cascade(label='游戏', menu=vmenu)
root['menu'] = menubar

root.mainloop()

