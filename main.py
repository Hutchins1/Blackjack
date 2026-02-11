
import random
from PIL import Image, ImageTk
from tkinter import *
import re
import PIL.Image
print("Pillow Image module:", PIL.Image.__file__)

from PIL import Image
print("Imported Image module:", Image.__file__)


root = Tk()
root.title("Login Page")
root.geometry("800x600+20+20")
money_count = 500
bet = 0
player_cards_list = []
dealer_cards_list = []
hit_allowed = True
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
    jack_c = ["card_clubs_J.png", 10]
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
"FRAMES"
frame_cards = Frame(root,width = 800,height=6000, bg = "blue")    
frame_cards.place(x=310, y=10, width = 480,height=580)

frame_game = Frame(root,width = 800,height=6000, bg = "teal")
frame_game.place(x=0, y=0, width = 800,height=6000)

frame_bet = Frame(root,width = 800,height=6000, bg = "black")
frame_bet.place(x=10, y=10, width = 290,height=580)

frame_start = Frame(root,width = 800,height=6000, bg = "teal")
frame_start.place(x=0, y=0, width = 800,height=6000)

class Card():
    def __init__(self, x, y, what_card, card_list):
        super().__init__()
        self.x = x
        self.y = y
        self.score = what_card[1]
        self.filename = what_card[0]
        self.help = what_card
    def create_label(self):
        self.card = Label(frame_cards, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
        self.card.place(x = self.x, y = self.y, width = 125, height =175 )
    
    def place_label(self):
        self.card.place(x = self.x, y = self.y, width = 125, height =175 )

    def card_choose(self, back):
    # --- Resize helper ---
        def load_and_resize(self, back): #AI
            if back == False:
                img = Image.open("filesse/" + self.filename)
                img = img.resize((185, 185), Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            else:
                img = Image.open("filesse/card_back.png")
                img = img.resize((185, 185), Image.LANCZOS)
                return ImageTk.PhotoImage(img)

    # Load and resize images
        img = load_and_resize(self, back)
    # Display dealer cards
        self.card.config(image=img)
        self.card.image = img



"FUNCTIONS"

def bet_place():
    global money_count
    global bet
    bet = bet_entry.get()
    bet = int(bet)
    
    if bet <= money_count:
        frame_game.tkraise()
        frame_cards.tkraise()
        bet_amount.config(text = f"BET: ${bet}")
        money_count -= bet
        money.config(text = money_count)
        deal_cards(card_list,player_cards_list, dealer_cards_list)
        return bet


# def score_check(player_cards_list, dealer_cards_list):
#     player_score = 0
#     dealer_score = 0
#     for card in range(len(player_cards_list)):
#         player_score += player_cards_list[card].score
#     for card in range(len(dealer_cards_list)):
#         dealer_score += dealer_cards_list[card].score
#     print(dealer_score)
#     return dealer_score, player_score

def hit_player(card_list, player_cards_list):
    index = random.randint(0, len(card_list)-1)
    what_card = card_list.pop(index)
    player_cards_list.append(Card(100, 395, what_card, card_list))
    player_cards_list[-1].create_label()
    player_cards_list[-1].card_choose(False)
    for card in range(len(player_cards_list)):
        if len(player_cards_list) == 2:
            if card == 0:
                player_cards_list[card].x = 110
                player_cards_list[card].place_label()
            if card == 1:
                player_cards_list[card].x = 245
                player_cards_list[card].place_label()
        if len(player_cards_list) == 3:
            if card == 0:
                player_cards_list[card].x = 42.5
                player_cards_list[card].place_label()
            if card == 1:
                player_cards_list[card].x = 177.5
                player_cards_list[card].place_label()
            if card == 2:
                player_cards_list[card].x = 312.5
                player_cards_list[card].place_label()
        if len(player_cards_list) == 4:
            if card == 0:
                player_cards_list[card].x = 10
                player_cards_list[card].place_label()
            if card == 1:
                player_cards_list[card].x = 121.7
                player_cards_list[card].place_label()
            if card == 2:
                player_cards_list[card].x = 233.4
                player_cards_list[card].place_label()
            if card == 3:
                player_cards_list[card].x = 345.1
                player_cards_list[card].place_label()
        if len(player_cards_list) == 5:
            if card == 0:
                player_cards_list[card].x = 10
                player_cards_list[card].place_label()
            elif card == 1:
                player_cards_list[card].x = 93.75
                player_cards_list[card].place_label()
            elif card == 2:
                player_cards_list[card].x = 177.5
                player_cards_list[card].place_label()
            elif card == 3:
                player_cards_list[card].x = 261.25
                player_cards_list[card].place_label()
            elif card == 4:
                player_cards_list[card].x = 345
                player_cards_list[card].place_label()
        if len(player_cards_list) == 6:
            if card == 0:
                player_cards_list[card].x = 10
                player_cards_list[card].place_label()
            elif card == 1:
                player_cards_list[card].x = 77
                player_cards_list[card].place_label()
            elif card == 2:
                player_cards_list[card].x = 144
                player_cards_list[card].place_label()
            elif card == 3:
                player_cards_list[card].x = 211
                player_cards_list[card].place_label()
            elif card == 4:
                player_cards_list[card].x = 278
                player_cards_list[card].place_label()
            elif card == 5:
                player_cards_list[card].x = 345
                player_cards_list[card].place_label()
        if len(player_cards_list) == 7:
            if card == 0:
                player_cards_list[card].x = 10
                player_cards_list[card].place_label()
            elif card == 1:
                player_cards_list[card].x = 65.83
                player_cards_list[card].place_label()
            elif card == 2:
                player_cards_list[card].x = 121.66
                player_cards_list[card].place_label()
            elif card == 3:
                player_cards_list[card].x = 177.49
                player_cards_list[card].place_label()
            elif card == 4:
                player_cards_list[card].x = 233.32
                player_cards_list[card].place_label()
            elif card == 5:
                player_cards_list[card].x = 289.15
                player_cards_list[card].place_label()
            elif card == 6:
                player_cards_list[card].x = 345
                player_cards_list[card].place_label()
        if len(player_cards_list) == 8:
            if card == 0:
                player_cards_list[card].x = 10
                player_cards_list[card].place_label()
            elif card == 1:
                player_cards_list[card].x = 57.857
                player_cards_list[card].place_label()
            elif card == 2:
                player_cards_list[card].x = 105.714
                player_cards_list[card].place_label()
            elif card == 3:
                player_cards_list[card].x = 153.571
                player_cards_list[card].place_label()
            elif card == 4:
                player_cards_list[card].x = 201.428
                player_cards_list[card].place_label()
            elif card == 5:
                player_cards_list[card].x = 249.285
                player_cards_list[card].place_label()
            elif card == 6:
                player_cards_list[card].x = 297.142
                player_cards_list[card].place_label()
            elif card == 7:
                player_cards_list[card].x = 345
                player_cards_list[card].place_label()


def hit_dealer(card_list, dealer_cards_list):
    index = random.randint(0, len(card_list)-1)
    what_card = card_list.pop(index)
    dealer_cards_list.append(Card(100, 10,what_card, card_list))
    dealer_cards_list[-1].create_label()
    if len(dealer_cards_list) == 1:
        dealer_cards_list[-1].card_choose(False)
    elif len(dealer_cards_list) == 2:
        dealer_cards_list[-1].card_choose(True)
    else:
        dealer_cards_list[-1].card_choose(False)
    for card in range(len(dealer_cards_list)):
        if len(dealer_cards_list) == 2:
            if card == 0:
                dealer_cards_list[card].x = 110
                dealer_cards_list[card].place_label()
            if card == 1:
                dealer_cards_list[card].x = 245
                dealer_cards_list[card].place_label()
        if len(dealer_cards_list) == 3:
            if card == 0:
                dealer_cards_list[card].x = 42.5
                dealer_cards_list[card].place_label()
            if card == 1:
                dealer_cards_list[card].x = 177.5
                dealer_cards_list[card].place_label()
            if card == 2:
                dealer_cards_list[card].x = 312.5
                dealer_cards_list[card].place_label()
        if len(dealer_cards_list) == 4:
            if card == 0:
                dealer_cards_list[card].x = 10
                dealer_cards_list[card].place_label()
            if card == 1:
                dealer_cards_list[card].x = 121.7
                dealer_cards_list[card].place_label()
            if card == 2:
                dealer_cards_list[card].x = 233.4
                dealer_cards_list[card].place_label()
            if card == 3:
                dealer_cards_list[card].x = 345.1
                dealer_cards_list[card].place_label()
        if len(dealer_cards_list) == 5:
            if card == 0:
                dealer_cards_list[card].x = 10
                dealer_cards_list[card].place_label()
            elif card == 1:
                dealer_cards_list[card].x = 93.75
                dealer_cards_list[card].place_label()
            elif card == 2:
                dealer_cards_list[card].x = 177.5
                dealer_cards_list[card].place_label()
            elif card == 3:
                dealer_cards_list[card].x = 261.25
                dealer_cards_list[card].place_label()
            elif card == 4:
                dealer_cards_list[card].x = 345
                dealer_cards_list[card].place_label()
        if len(dealer_cards_list) == 6:
            if card == 0:
                dealer_cards_list[card].x = 10
                dealer_cards_list[card].place_label()
            elif card == 1:
                dealer_cards_list[card].x = 77
                dealer_cards_list[card].place_label()
            elif card == 2:
                dealer_cards_list[card].x = 144
                dealer_cards_list[card].place_label()
            elif card == 3:
                dealer_cards_list[card].x = 211
                dealer_cards_list[card].place_label()
            elif card == 4:
                dealer_cards_list[card].x = 278
                dealer_cards_list[card].place_label()
            elif card == 5:
                dealer_cards_list[card].x = 345
                dealer_cards_list[card].place_label()
        if len(dealer_cards_list) == 7:
            if card == 0:
                dealer_cards_list[card].x = 10
                dealer_cards_list[card].place_label()
            elif card == 1:
                dealer_cards_list[card].x = 65.83
                dealer_cards_list[card].place_label()
            elif card == 2:
                dealer_cards_list[card].x = 121.66
                dealer_cards_list[card].place_label()
            elif card == 3:
                dealer_cards_list[card].x = 177.49
                dealer_cards_list[card].place_label()
            elif card == 4:
                dealer_cards_list[card].x = 233.32
                dealer_cards_list[card].place_label()
            elif card == 5:
                dealer_cards_list[card].x = 289.15
                dealer_cards_list[card].place_label()
            elif card == 6:
                dealer_cards_list[card].x = 345
                dealer_cards_list[card].place_label()
        if len(dealer_cards_list) == 8:
            if card == 0:
                dealer_cards_list[card].x = 10
                dealer_cards_list[card].place_label()
            elif card == 1:
                dealer_cards_list[card].x = 57.857
                dealer_cards_list[card].place_label()
            elif card == 2:
                dealer_cards_list[card].x = 105.714
                dealer_cards_list[card].place_label()
            elif card == 3:
                dealer_cards_list[card].x = 153.571
                dealer_cards_list[card].place_label()
            elif card == 4:
                dealer_cards_list[card].x = 201.428
                dealer_cards_list[card].place_label()
            elif card == 5:
                dealer_cards_list[card].x = 249.285
                dealer_cards_list[card].place_label()
            elif card == 6:
                dealer_cards_list[card].x = 297.142
                dealer_cards_list[card].place_label()
            elif card == 7:
                dealer_cards_list[card].x = 345
                dealer_cards_list[card].place_label()
    

def hit_player_running(card_list, player_cards_list, hit_allowed):
    print(hit_allowed)
    if hit_allowed == True:
        player_score = 0
        hit_player(card_list, player_cards_list)
        for card in range(len(player_cards_list)):
            player_score += player_cards_list[card].score
            print(player_score)
            print(player_cards_list[card].help)
            print(player_cards_list[card].filename)
        if player_score > 21:
            for card2 in range(len(player_cards_list)):
                if player_cards_list[card2].help[1] == 11:
                    player_cards_list[card2].help[1] = 1
                    player_score -= 10
                    print(player_score)
            if player_score > 21:
                player_bust()

def player_bust():
    print("bust")


def stand_func(dealer_cards_list,player_cards_list):
    global hit_allowed
    global money_count
    global bet
    dealer_score = 0
    player_score = 0
    hit_allowed = False
    for card in range(len(dealer_cards_list)):
        dealer_cards_list[card].card_choose(False)
        dealer_score += dealer_cards_list[card].score
        print(dealer_score)
        print(dealer_cards_list[card].help)
        print(dealer_cards_list[card].filename)
    while dealer_score < 17:
        dealer_score = 0
        hit_dealer(card_list,dealer_cards_list)
        for card in range(len(dealer_cards_list)):
            dealer_cards_list[card].card_choose(False)
            dealer_score += dealer_cards_list[card].score
        
        if dealer_score > 17:
            for card2 in range(len(dealer_cards_list)):
                if dealer_cards_list[card2].help[1] == 11:
                    dealer_cards_list[card2].help[1] = 1
                    dealer_score -= 10
                    print(dealer_score)

    for card in range(len(player_cards_list)):
        player_score += player_cards_list[card].score
        print(player_score)
        print(player_cards_list[card].help)
        print(player_cards_list[card].filename)
    if dealer_score > 21:
        print("dealer_lose bust")
    if player_score > 21:
        print("player bust")
    elif player_score > dealer_score:
        money_count += (bet*2)
        money.config(text = money_count)
    elif player_score == dealer_score:
        money_count += bet
        money.config(text = money_count)

def new_game():
    global bet 
    global card_list
    global player_cards_list
    global dealer_cards_list 
    bet = 0 
    card_list = [two_h, two_d, two_c, two_s, three_h, three_d, three_c, three_s, four_h, four_d, four_c, four_s, five_h, five_d, five_c, five_s, six_h, six_d, six_c, six_s, seven_h, seven_d, seven_c, seven_s, eight_h, eight_d, eight_c, eight_s, nine_h, nine_d, nine_c, nine_s, ten_h, ten_d, ten_c, ten_s, jack_h, jack_d, jack_c, jack_s, queen_h, queen_d, queen_c, queen_s, king_h, king_d, king_c, king_s, ace_h, ace_d, ace_c, ace_s]
    player_cards_list = []
    dealer_cards_list = []
    frame_bet.tkraise()


def deal_cards(card_list,player_cards_list,dealer_cards_list):
    hit_player(card_list,player_cards_list)
    hit_player(card_list,player_cards_list)
    hit_dealer(card_list,dealer_cards_list)
    hit_dealer(card_list,dealer_cards_list)
#dealer_score, player_score = score_check(dealer_cards_list, player_cards_list)
#print(player_score)
#if dealer_score < 17:
#    hit_dealer(card_list,dealer_cards_list)
#hit_player(card_list,player_cards_list)
"BUTTON COMMANDS"

def start_command():
    frame_game.tkraise()
    frame_bet.tkraise()
    frame_cards.tkraise()





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

# Buttons
hit = Button(frame_game, bg="white", fg="teal", text = "HIT", font = ("Times New Roman",18), command = lambda: hit_player_running(card_list,player_cards_list, hit_allowed))
hit.place(x=10,y=450,width = 140, height = 140)

stand = Button(frame_game, bg="white", fg="teal", text = "STAND", font = ("Times New Roman",18), command = lambda: stand_func(dealer_cards_list, player_cards_list))
stand.place(x=160, y=450,width = 140, height = 140)

new_game_button = Button(frame_game, bg="white", fg="teal", text = "NEW GAME", font = ("Times New Roman",18), command = lambda: new_game())
new_game_button.place(x=10,y=300,width = 140, height = 140)

#Labels

money = Label(frame_game, bg = "white", fg = "black", text = money_count ,font = ("Times New Roman",24) )
money.place(x=10, y = 10, width = 200, height = 50)

bet_amount = Label(frame_game, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
bet_amount.place(x=50, y = 405, width = 200, height = 35)

# pcard1 = Label(frame_cards, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
# pcard1.place(x=110, y = 580-185, width = 125, height =175 )

# pcard2 = Label(frame_cards, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
# pcard2.place(x=110+135, y = 580-185, width = 125, height =175 )

# dcard1 = Label(frame_cards, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
# dcard1.place(x=110, y = 10, width = 125, height =175 )

# dcard2 = Label(frame_cards, bg = "white", fg = "black", text = bet,font = ("Times New Roman",12) )
# dcard2.place(x=110+135, y = 10, width = 125, height =175 )


# dealer_1, dealer_2, player_1, player_2 = card_choose(card_list)
# score_check(dealer_1, dealer_2, player_1, player_2) 

root.mainloop()