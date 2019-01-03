# -*- coding: utf-8 -*-

import random
import tkinter as tk
from PIL import Image, ImageTk

class GuiTic:
    def __init__(self, root):
        menubar = tk.Menu(root)
        fmenu = tk.Menu(root)
        fmenu.add_command(label='人机对战（玩家先）', command=self.ticplay)
        fmenu.add_command(label='人机对战（电脑先）', command=self.ticplay)
        fmenu.add_command(label='人人对战', command=self.ticplay)
        vmenu = tk.Menu(root)
        vmenu.add_command(label='重玩', command=self.ticplay)
        vmenu.add_command(label='悔棋')
        menubar.add_cascade(label='模式', menu=fmenu)
        menubar.add_cascade(label='游戏', menu=vmenu)
        root['menu'] = menubar
        root.title('井字棋')


        ButtonTic = []
        for i in range(3):
            for j in range(3):
                self.bt = tk.Button(root, command=self.loadpicture, state=tk.ACTIVE)
                ButtonTic.append(self.bt)
                self.bt.grid(row=i, column=j, ipadx=10, ipady=10, padx=10, pady=10)

        img1 = Image.open('enemy.png')
        img2 = Image.open('plane.png')
        self.XXX = ImageTk.PhotoImage(img1)
        self.OOO = ImageTk.PhotoImage(img2)

    def loadpicture(self):
        self.bt['image'] = self.XXX
        self.bt['state'] = tk.DISABLED
        print ('aaa')
        print ('bbb')
        return False

    def ticplay(self):
        print('aaa')




# guitic.loadpicture()

root = tk.Tk()
guitic = GuiTic(root)
root.mainloop()