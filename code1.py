import random
from tkinter import *
root = Tk()
root.geometry("500x500")
game = ["PAPER", "ROCK", "SCISSORS"]
p=[]
c=[]
i=0

    def IsScissors():
        computer = random.choice(game)
        if computer=="SCISSORS":
            l1=Label(root, text="THROW TIED", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        elif computer=="ROCK":
            l1=Label(root, text="COMPUTER WINS", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        else:
            l1=Label(root, text="PLAYER WINS", font="verdana 20 bold", borderwidth=2, relief="solid",bg="white")
            l1.place(x=5, y=200, width=490)
        point = l1.cget("text")
        if point=="COMPUTER WINS":
            c.append("a")
        elif point=="PLAYER WINS":
            p.append("a")

    def IsRock():
        computer = random.choice(game)
        if computer=="ROCK":
            l1=Label(root, text="THROW TIED", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        elif computer=="PAPER":
            l1=Label(root, text="COMPUTER WINS", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        else:
            l1=Label(root, text="PLAYER WINS", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        point = l1.cget("text")
        if point=="COMPUTER WINS":
            c.append("a")
        elif point=="PLAYER WINS":
            p.append("a")

    def IsPaper():
        computer = random.choice(game)
        if computer=="PAPER":
            l1=Label(root, text="THROW TIED", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        elif computer=="SCISSORS":
            l1=Label(root, text="COMPUTER WINS", font="verdana 20 bold", borderwidth=2, relief="solid", bg="white")
            l1.place(x=5, y=200, width=490)
        else:
            l1=Label(root, text="PLAYER WINS", font="verdana 20 bold", borderwidth=2, relief="solid",bg="white")
            l1.place(x=5, y=200, width=490)
        point = l1.cget("text")
        if point=="COMPUTER WINS":
            c.append("a")
        elif point=="PLAYER WINS":
            p.append("a")

b1=Button(root, text="SCISSORS", font="verdana 16 bold", border=3, command=IsScissors)
b1.place(x=5, y=100, width=150)
b2=Button(root, text="PAPER", font="verdana 16 bold", border=3, command=IsPaper)
b2.place(x=175, y=100, width=150)
b3=Button(root, text="ROCK", font="verdana 16 bold", border=3, command=IsRock)
b3.place(x=345, y=100, width=150)

b4=Button(root, text="RESET GAME", font="verdana 16 bold", border=3, fg="white", bg="black")
b4.place(x=175, y=300, width=150)

root.mainloop()