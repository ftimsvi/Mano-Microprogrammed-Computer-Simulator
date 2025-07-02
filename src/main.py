from cProfile import label
from cgitb import text
from textwrap import fill
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import Style, Treeview
from turtle import width
import os.path

import MicroprogrammControl

root = tk.Tk()
root.geometry('1500x700')
root.title("Mano Simulator")


memoryFrame = Frame(root)
memoryScroll = Scrollbar(memoryFrame, width=40)
memoryTree = Treeview(root, yscrollcommand=memoryScroll.set)


registerFrame = Frame(root)
registerScroll = Scrollbar(registerFrame)
registerTreeview = Treeview(root, yscrollcommand=registerScroll.set)

#making text editors for microprogram and program
microLable = Label(root, text="Microprogram :")
microLable.place(x=40, y=10)

microEntry = Scrollbar(root, width=40)
microEntry.place(x=40, y=30, height=290)
microInfo = Text(root, yscrollcommand=microEntry.set, width=40)
microInfo.pack()
microInfo.place(x=40, y=30, height=290)
microEntry.config(command=microInfo.yview)

def saveButtonClicked():
    cur_inp = microInfo.get('1.0', tk.END)
    #f1 = open("MicroProgramm.txt", "w")
    #f1.write(cur_inp)
    #f1.close()
    save_path = './ManoSimulator'
    name_of_file = "MicroProgramm"
    completeName = os.path.join(save_path, name_of_file+".txt")         
    file1 = open(completeName, "w")
    file1.write(cur_inp)
    file1.close()
    MicroprogrammControl.MicroProgramm_Traversal()

microButton = Button(root, text="Save", padx=25, command=saveButtonClicked)
microButton.place(x=281, y=320)

def resetButtonClicked():
    open('MicroProgramm.txt', 'w').close()
    microInfo.delete("1.0","end")

resetButton = Button(root, text="Reset", padx=25, command=resetButtonClicked)
resetButton.place(x=194, y=320)

programLable = Label(root, text="Program :")
programLable.place(x=40, y=350)

programEntry = Scrollbar(root, width=40)
programEntry.place(x=40, y=370, height=290)
programInfo = Text(root, yscrollcommand=programEntry.set, width=40)
programInfo.pack()
programInfo.place(x=40, y=370, height=290)
programEntry.config(command=programInfo.yview)



def programButtonClicked():
    
    cur_inp2 = programInfo.get('1.0', tk.END)
    #f2 = open("PROGRAMM.txt", "w")
    #f2.write(cur_inp2)
    #f2.close()
    save_path2 = './ManoSimulator'
    name_of_file2 = "PROGRAMM"
    completeName2 = os.path.join(save_path2, name_of_file2+".txt")         
    file2 = open(completeName2, "w")
    file2.write(cur_inp2)
    file2.close()
    MicroprogrammControl.Memory_Traversal()
    MicroprogrammControl.Execute_programm()
    MicroprogrammControl.PrintReg()
    MicroprogrammControl.printMemory()

    counter = 0
    for state in MicroprogrammControl.RegisterState:
        print("AC :", bin(MicroprogrammControl.RegisterState[state][0])[2:])
        registerTreeview.insert(parent='', index='end', iid=counter, text="", values=(state, bin(MicroprogrammControl.RegisterState[state][0])[2:].zfill(16),
        bin(MicroprogrammControl.RegisterState[state][1])[2:].zfill(16), bin(MicroprogrammControl.RegisterState[state][2])[2:].zfill(16),
        bin(MicroprogrammControl.RegisterState[state][3])[2:].zfill(16), bin(MicroprogrammControl.RegisterState[state][4])[2:].zfill(16),
        bin(MicroprogrammControl.RegisterState[state][5])[2:].zfill(16)))
        counter += 1

    for count in range(2049):
        if count in MicroprogrammControl.Memory:
            memoryTree.insert(parent='', index='end', iid=count, text="", values=(count, hex(count), MicroprogrammControl.Memory[count][0:]))
        else:
            memoryTree.insert(parent='', index='end', iid=count, text="", values=(count, hex(count)))

programButton = Button(root, text="Assemble", padx=25, command=programButtonClicked)
programButton.place(x=255, y=660)

def resetButtonClicked2():
    open('PROGRAMM.txt', 'w').close()
    programInfo.delete("1.0","end")

resetButton2 = Button(root, text="Reset", padx=25, command=resetButtonClicked2)
resetButton2.place(x=169, y=660)


#making a table for memory and its contents
memoryLable = Label(root, text="Memory Table :")
memoryLable.place(x=1160, y=8)

#memoryFrame = Frame(root)
memoryFrame.place(x=1000, y=10, height=500)

#memoryScroll = Scrollbar(memoryFrame, width=40)
memoryScroll.pack(fill=Y)
memoryScroll.place(x=1000, y=10, height=500)

#memoryTree = Treeview(root, yscrollcommand=memoryScroll.set)
memoryTree['columns'] = ("Decimal Address", "HEX Address", "Content")
memoryScroll.config(command=memoryTree.yview)

memoryTree.column("#0", width=0, stretch=NO)
memoryTree.column("Decimal Address", anchor=W, width=100)
memoryTree.column("HEX Address", anchor=CENTER, width=95)
memoryTree.column("Content", anchor=W, width=100)

memoryTree.heading("#0", text="", anchor=W)
memoryTree.heading("Decimal Address", text="Decimal Address", anchor=W)
memoryTree.heading("HEX Address", text="HEX Address", anchor=CENTER)
memoryTree.heading("Content", text="Content", anchor=W)

#for count in range(2049):
#    memoryTree.insert(parent='', index='end', iid=count, text="", values=(count, hex(count)))

memoryTree.pack(padx=40, pady=30, side=tk.RIGHT, fill=Y)


#making another table for showing the content of registers
registerLable = Label(root, text="Instruction Details :")
registerLable.place(x=424, y=10)

#registerFrame = Frame(root)
registerFrame.place(x=444, y=10, height=500)

#registerScroll = Scrollbar(registerFrame)
registerScroll.pack(fill=Y)
registerScroll.place(x=1000, y=10, height=500)

#registerTreeview = Treeview(root, yscrollcommand=registerScroll.set)
registerScroll.config(command=registerTreeview.yview)

registerTreeview['columns'] = ("Elements", "AC", "DR", "PC", "AR", "CAR", "SBR")
registerTreeview.column("#0", width=0, stretch=NO)
registerTreeview.column("Elements", anchor=W, width=90)
registerTreeview.column("AC", anchor=W, width=100)
registerTreeview.column("DR", anchor=W, width=105)
registerTreeview.column("PC", anchor=CENTER, width=100)
registerTreeview.column("AR", anchor=W, width=100)
registerTreeview.column("CAR", anchor=W, width=100)
registerTreeview.column("SBR", anchor=W, width=100)

registerTreeview.heading("#0", text="", anchor=W)
registerTreeview.heading("Elements", text="Clock", anchor=W)
registerTreeview.heading("AC", text="AC", anchor=W)
registerTreeview.heading("DR", text="DR", anchor=W)
registerTreeview.heading("PC", text="PC", anchor=CENTER)
registerTreeview.heading("AR", text="AR", anchor=W)
registerTreeview.heading("CAR", text="CAR", anchor=W)
registerTreeview.heading("SBR", text="SBR", anchor=W)



registerTreeview.place(relx=.515, rely=.21,anchor= CENTER)

#for count in range(4097):
#    memoryTree.insert(parent='', index='end', iid=count, text="", values=(count, hex(count)))

#registerTreeview.pack(fill=Y)


manoLable = Label(root, text="Mano Simulator", font=('Times', 52))
manoLable.place(x=550, y=570)


#making a reset push button to clear the data of treeviews
def treeResetButtonClicked():
    for item in registerTreeview.get_children():
        registerTreeview.delete(item)

    for item in memoryTree.get_children():
        memoryTree.delete(item)

treeResetButton = Button(root, text="Reset", padx=25, command=treeResetButtonClicked)
treeResetButton.place(x=1035, y=261)


root.mainloop()