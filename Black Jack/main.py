import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.populate()
        self.shuffle()

    def populate(self):
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            self.populate()
            self.shuffle()
        return self.cards.pop()


deck = Deck()
player_hand = []
dealer_hand = []
player_money = 100
player_bet = 1

def new_game():
    global player_hand, dealer_hand, player_bet
    if player_money <= 0:
        messagebox.showinfo("Game Over", "You have no money left!")
        return
    player_hand = [deck.draw_card(), deck.draw_card()]
    dealer_hand = [deck.draw_card(), deck.draw_card()]
    player_label.config(text=f"Player: {[str(card) for card in player_hand]}")
    dealer_label.config(text=f"Dealer: {str(dealer_hand[0])}")
    player_bet = 1  # Reset bet to minimum
    bet_label.config(text=f"Bet: ${player_bet}")

def draw_card():
    if player_money <= 0:
        messagebox.showinfo("Game Over", "You have no money left!")
        return
    player_hand.append(deck.draw_card())
    player_label.config(text=f"Player: {[str(card) for card in player_hand]}")

def evaluate():
    global player_money, player_bet
    if player_money <= 0:
        messagebox.showinfo("Game Over", "You have no money left!")
        return
    player_value = calculate_value(player_hand)
    dealer_value = calculate_value(dealer_hand)
    if player_value > 21:
        player_money -= player_bet
    elif dealer_value > 21 or player_value > dealer_value:
        player_money += player_bet
    elif player_value < dealer_value:
        player_money -= player_bet
    money_label.config(text=f"Money: ${player_money}")
    dealer_label.config(text=f"Dealer: {[str(card) for card in dealer_hand]}")
    new_game()

def calculate_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card.value in ["Jack", "Queen", "King"]:
            value += 10
        elif card.value == "Ace":
            value += 11
            aces += 1
        else:
            value += int(card.value)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


root = tk.Tk()
root.title("Blackjack Game")
root.geometry("800x200")

# Create main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


instruction_label = ttk.Label(main_frame, text="Welcome to Blackjack! Press 'New Game' to start.", wraplength=300)
player_label = ttk.Label(main_frame, text="Player:")
dealer_label = ttk.Label(main_frame, text="Dealer:")
money_label = ttk.Label(main_frame, text=f"Money: ${player_money}")
bet_label = ttk.Label(main_frame, text=f"Bet: ${player_bet}")
new_game_button = ttk.Button(main_frame, text="New Game", command=new_game)
draw_card_button = ttk.Button(main_frame, text="Draw Card", command=draw_card)
evaluate_button = ttk.Button(main_frame, text="Evaluate", command=evaluate)


instruction_label.grid(row=0, column=0, columnspan=2)
player_label.grid(row=1, column=0, sticky=tk.W)
dealer_label.grid(row=1, column=1, sticky=tk.W)
new_game_button.grid(row=2, column=0, sticky=tk.W)
draw_card_button.grid(row=2, column=1, sticky=tk.W)
evaluate_button.grid(row=4, column=1, sticky=tk.E)
money_label.grid(row=3, column=0, sticky=tk.W)
bet_label.grid(row=3, column=1, sticky=tk.W)

root.mainloop()
