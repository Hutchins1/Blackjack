from tkinter import *
import re

root = Tk()
root.title("Login Page")
root.geometry("800x600+20+20")
money_count = 500
bet = 0

if bet == 0:
    two_h = ["card_hearts_02.png", 2]
    two_d = ["card_diamonds_02.png", 2]
    two_c = ["card_clubs_02.png", 2]
    two_s = ["card_spades_02.png", 2]
    three_h = ["card_hearts_03.png", 3]
    three_d = ["card_diamonds_03.png", 3]
    three_c =  ["card_clubs_03.png", 3]
    three_s = ["card_spades_03.png", 3]
    four_h =  ["card_hearts_04.png", 4]
    four_d =  ["card_diamonds_04.png", 4]
    four_c = ["card_clubs_04.png", 4]
    four_s= ["card_spades_04.png", 4]
    five_h= ["card_hearts_05.png", 5]
    five_d= ["card_diamonds_05.png", 5]
    five_c= ["card_clubs_05.png", 5]
    five_s= ["card_spades_05.png", 5]
    six_h= ["card_hearts_06.png", 6]
    six_d= ["card_diamonds_06.png", 6]
    six_c= ["card_clubs_06.png", 6]
    six_s = ["card_spades_06.png", 6]
    seven_h = ["card_hearts_07.png", 7]
    seven_d = ["card_diamonds_07.png", 7]
    seven_c = ["card_clubs_07.png", 7]
    seven_s = ["card_spades_07.png", 7]
    eight_h = ["card_hearts_08.png", 8]
    eight_d = ["card_diamonds_08.png", 8]
    eight_c = ["card_clubs_08.png", 8]
    eight_s = ["card_spades_08.png", 8]
    nine_h = ["card_hearts_09.png", 9]
    nine_d = ["card_diamonds_09.png", 9]
    nine_c = ["card_clubs_09.png", 9]
    nine_s = ["card_spades_09.png", 9]
    ten_h = ["card_hearts_10.png", 10]
    ten_d = ["card_diamonds_10.png", 10]
    ten_c = ["card_clubs_10.png", 10]
    ten_s  = ["card_spades_10.png", 10]
    jack_h = ["card_hearts_J.png", 10]
    jack_d = ["card_diamonds_J.png", 10]
    jack_s = ["card_spades_J.png", 10]
    queen_h = ["card_hearts_Q.png", 10]
    queen_d = ["card_diamonds_Q.png", 10]
    queen_c = ["card_clubs_Q.png", 10]
    queen_s = ["card_spades_Q.png", 10]
    king_h = ["card_hearts_K.png", 10]
    king_d = ["card_diamonds_K.png", 10]
    king_c = ["card_clubs_K.png", 10]
    king_s = ["card_spades_K.png", 10]
    ace_h = ["card_hearts_A.png", 11]
    ace_d = ["card_diamonds_A.png", 11]
    ace_c = ["card_clubs_A.png", 11]
    ace_s = ["card_spades_A.png", 11]
    card_list = [two_h, two_d, two_c, two_s, three_h, three_d, three_c, three_s, four_h, four_d, four_c, four_s, five_h, five_d, five_c, five_s, six_h, six_d, six_c, six_s, seven_h, seven_d, seven_c, seven_s, eight_h, eight_d, eight_c, eight_s, nine_h, nine_d, nine_c, nine_s, ten_h, ten_d, ten_c, ten_s, jack_h, jack_d, jack_c, jack_s, queen_h, queen_d, queen_c, queen_s, king_h, king_d, king_c, king_s, ace_h, ace_d, ace_c, ace_s]
"FUNCTIONS"

def bet_place():
    global money_count
    global bet
    bet = bet_entry.get()
    bet = int(bet)
    
    if bet <= money_count:
        frame_game.tkraise()
        bet_amount.config(text = f"BET: ${bet}")
        money_count -= bet
        money.config(text = money_count)
        return bet

def card_choose(card_list):
    dealer_1 = dealer_1.randint(1, 52)
    dealer_2 = 




"BUTTON COMMANDS"

def start_command():
    frame_game.tkraise()
    frame_bet.tkraise()

"FRAMES"

frame_game = Frame(root,width = 800,height=6000, bg = "teal")
frame_game.place(x=0, y=0, width = 800,height=6000)

frame_bet = Frame(root,width = 800,height=6000, bg = "black")
frame_bet.place(x=10, y=10, width = 290,height=580)

frame_start = Frame(root,width = 800,height=6000, bg = "teal")
frame_start.place(x=0, y=0, width = 800,height=6000)


"FRAME START"
title= Label(frame_start, bg = "white", fg = "black", text = "BLACKJACK",font = ("Times New Roman",48) )
title.place(x=100, y = 150, width = 600, height = 100)


start = Button(frame_start, bg="white", fg="teal", text = "START", font = ("Times New Roman",18), command = start_command)
start.place(x=200, y=300,width = 400, height = 100)
"FRAME BET"

# Labels
bet_title= Label(frame_bet, bg = "white", fg = "black", text = "PLACE A BET",font = ("Times New Roman",24) )
bet_title.place(x=10, y = 10, width = 270, height = 100)

moneybet_title= Label(frame_bet, bg = "white", fg = "black", text = f"You have {money_count}$",font = ("Times New Roman",24) )
moneybet_title.place(x=10, y = 470, width = 270, height = 100)

# Entrys
bet_entry = Entry(frame_bet, fg='grey')
bet_entry.place(x = 10, y = 240, width = 270, height = 100)

# Buttons
bet_button = Button(frame_bet, bg="white", fg="teal", text = "PLACE BET", font = ("Times New Roman",18), command = bet_place)
bet_button.place(x=55, y=350,width = 180, height = 50)

"FRAMEGAME"
hit = Button(frame_game, bg="white", fg="teal", text = "HIT", font = ("Times New Roman",18))
hit.place(x=10,y=450,width = 140, height = 140)

stand = Button(frame_game, bg="white", fg="teal", text = "STAND", font = ("Times New Roman",18))
stand.place(x=160, y=450,width = 140, height = 140)


money = Label(frame_game, bg = "white", fg = "black", text = money_count ,font = ("Times New Roman",24) )
money.place(x=590, y = 10, width = 200, height = 50)

bet_amount = Label(frame_game, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
bet_amount.place(x=50, y = 405, width = 200, height = 35)



root.mainloop()