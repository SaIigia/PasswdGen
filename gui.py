'''Gui Code module for Python3 Password Generator based on Tkinter package'''

import tkinter as tk, PasswdGen as pg
from tkinter import scrolledtext as st
from main import __version__

pg = pg.PasswdGen()

class Application(tk.Frame):
    def __init__(self, master, cArgs):
        super().__init__(master)
        self.master = master

        self.__l = tk.StringVar()
        self.__n = tk.StringVar()
        self.__uc = tk.BooleanVar()
        self.__lc = tk.BooleanVar()
        self.__dg = tk.BooleanVar()
        self.__sp = tk.BooleanVar()
        self.__uni = tk.BooleanVar()
        self.__nod = tk.BooleanVar()

        self.LoadFromArgs(cArgs)
        self.CreateWidgets()

    def CreateWidgets(self):

        # Frames
        self.frControls = tk.LabelFrame(self.master, text='Controls', font='Arial 10 bold italic')
        self.frControls.grid(row=0, column=0, columnspan=1, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        self.frParams = tk.LabelFrame(self.master, text='Parameters', font='Arial 10 bold italic')
        self.frParams.grid(row=0, column=1, columnspan=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)


        # Buttons
        self.btnGenerate = tk.Button(self.frControls, text='Generate', command=self.Generate)
        self.btnGenerate.grid(row=0, column=0, columnspan=1, sticky='W', padx=5, pady=5)

        self.btnClear = tk.Button(self.frControls, text='Clear', command=self.Clear)
        self.btnClear.grid(row=0, column=1, columnspan=1, sticky='W', padx=5, pady=5)

        self.btnQuit = tk.Button(self.frControls, text='Quit', command=self.master.destroy, fg='red')
        self.btnQuit.grid(row=1, column=0, columnspan=1, sticky='W', padx=5, pady=5)

        # Checkboxes
        self.cbLC = tk.Checkbutton(self.frParams, text='Lower case', variable=self.__lc, onvalue=True, offvalue=False)
        self.cbLC.grid(row=0, column=0, sticky='W')

        self.cbUC = tk.Checkbutton(self.frParams, text='Upper case', variable=self.__uc, onvalue=True, offvalue=False)
        self.cbUC.grid(row=1, column=0, sticky='W')

        self.cbDG = tk.Checkbutton(self.frParams, text='Digits', variable=self.__dg, onvalue=True, offvalue=False)
        self.cbDG.grid(row=2, column=0, sticky='W')

        self.cbSP = tk.Checkbutton(self.frParams, text='Special characters', variable=self.__sp, onvalue=True, offvalue=False)
        self.cbSP.grid(row=3, column=0, sticky='W')

        self.cbUNI = tk.Checkbutton(self.frParams, text='No simmilar-looking', variable=self.__uni, onvalue=True, offvalue=False)
        self.cbUNI.grid(row=4, column=0, sticky='W')

        # Scrolled Text boxes
        self.stbOut = st.ScrolledText(master=self.master, wrap=tk.WORD, width=60, height=20)
        self.stbOut.grid(row=1, column=0, columnspan=2, sticky='W', padx=5, pady=5)

        # Entry boxes
        self.entryL = tk.Entry(self.frParams, textvariable=self.__l)
        self.entryL.grid(row=6, column=0, sticky='W')

        self.entryN = tk.Entry(self.frParams, textvariable=self.__n)
        self.entryN.grid(row=8, column=0, sticky='W')


        # Labels
        tk.Label(self.frParams, text='Passwords length').grid(row=5)
        tk.Label(self.frParams, text='Number of passwords').grid(row=7)

    def Generate(self):
        pg.Generate(self.__l.get(), self.__n.get(), self.__uc.get(), self.__lc.get(), self.__dg.get(), self.__sp.get(), self.__uni.get(), self.__nod.get())
        self.stbOut.delete(1.0, tk.END)
        self.stbOut.insert(tk.INSERT, pg.PrintToString())


    def Clear(self):
        self.stbOut.delete(1.0, tk.END)
        pg.Clear()


    def LoadFromArgs(self, cArgs):
        self.__l.set(cArgs.l)
        self.__n.set(cArgs.n)
        self.__uc.set(cArgs.uc)
        self.__lc.set(cArgs.lc)
        self.__dg.set(cArgs.dg)
        self.__sp.set(cArgs.sp)
        self.__uni.set(cArgs.uni)
        self.__nod.set(cArgs.nod)