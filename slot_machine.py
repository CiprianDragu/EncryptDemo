#Simple Slot Machine
import random


#Creating functions

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🍬', '⭐',]
    return  [ random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet ):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🍬':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 2
        return 0


def slot_machine():
  balance =100

print ("*************************")
print ("Welcome to Slots!")
print ("Symbols:🍒 🍉 🍋 🍬 ⭐")
print ("*************************")
balance = 100.0  # Initialize balance

while balance > 0:
    print(f"Current balance: ${balance}")
    bet = input("Place your bet amount: ")

    try:
        bet = float(bet)
        if 0 < bet <= balance:
            balance -= bet

            row = spin_row()
            print("Spinning... \n")
            print_row(row)
            payout = get_payout(row, bet)



            print(f"You placed a bet of ${bet}. New balance: ${balance}")
        else:
            print(
                "Invalid bet amount. Please enter a value greater than 0 and less than or equal to your current balance.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__== '__slot_machine__':
    slot_machine()