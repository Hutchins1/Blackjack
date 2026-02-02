from tkinter import *
import re

root = Tk()
root.title("Login Page")
root.geometry("800x600+20+20")
money_count = 500
"FRAMES"

frame_game = Frame(root,width = 800,height=6000, bg = "teal")
frame_game.place(x=0, y=0, width = 800,height=6000)

frame_bet = Frame(root,width = 800,height=6000, bg = "black")
frame_bet.place(x=10, y=10, width = 290,height=580)

frame_start = Frame(root,width = 800,height=6000, bg = "teal")
frame_start.place(x=0, y=0, width = 800,height=6000)

"BUTTON COMMANDS"

def start_command():
    global frame_game
    frame_game.tkraise()
    frame_bet.tkraise()

"FRAME START"
title= Label(frame_start, bg = "white", fg = "black", text = "BLACKJACK",font = ("Times New Roman",48) )
title.place(x=100, y = 150, width = 600, height = 100)


start = Button(frame_start, bg="white", fg="teal", text = "START", font = ("Times New Roman",18), command = start_command)
start.place(x=200, y=300,width = 400, height = 100)
"FRAME BET"
bet_title= Label(frame_bet, bg = "white", fg = "black", text = "PLACE A BET",font = ("Times New Roman",24) )
bet_title.place(x=10, y = 10, width = 270, height = 100)

moneybet_title= Label(frame_bet, bg = "white", fg = "black", text = f"You have {money_count}$",font = ("Times New Roman",24) )
moneybet_title.place(x=10, y = 150, width = 270, height = 100)

bet_entry = Entry(frame_bet, fg='grey')
bet_entry.place(x = 10, y = 290, width = 270, height = 100)
"FRAMEGAME"
hit = Button(frame_game, bg="white", fg="teal", text = "HIT", font = ("Times New Roman",18))
hit.place(x=10,y=450,width = 140, height = 140)

stand = Button(frame_game, bg="white", fg="teal", text = "STAND", font = ("Times New Roman",18))
stand.place(x=160, y=450,width = 140, height = 140)


money = Label(frame_game, bg = "white", fg = "black", text = "Username: ",font = ("Times New Roman",24) )
money.place(x=200, y = 200, width = 200, height = 35)


root.mainloop()