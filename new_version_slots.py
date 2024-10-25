import random

# Define symbols and their corresponding values
symbols = {
    "🍒": 2,
    "🍋": 3,
    "🍊": 4,
    "🍇": 5,
    "🔔": 6,
    "💎": 10
}


def spin_reel():
    """Spin a single reel and return a random symbol."""
    return random.choice(list(symbols.keys()))



def spin_machine():
    """Spin all three reels of the slot machine."""
    return [spin_reel() for _ in range(3)]


def calculate_winnings(result, bet):
    """Calculate winnings based on the result and bet amount."""
    if len(set(result)) == 1:  # All symbols are the same
        return bet * symbols[result[0]]
    elif len(set(result)) == 2:  # Two symbols are the same
        return bet * 2
    else:
        return 0


def play_game():
    """Main game loop."""
    balance = 1000

    print("Welcome to the Fruit Slot Machine!")
    print("Symbols and their multipliers:")
    for symbol, value in symbols.items():
        print(f"{symbol}: x{value}")

    while True:
        print(f"\nYour current balance: ${balance}")
        bet = int(input("Enter your bet amount (or 0 to quit): "))

        if bet == 0:
            print(f"Thanks for playing! You're leaving with ${balance}")
            break

        if bet > balance:
            print("You don't have enough money for that bet.")
            continue

        balance -= bet
        result = spin_machine()
        print("Result:", " ".join(result))

        winnings = calculate_winnings(result, bet)
        balance += winnings

        if winnings > 0:
            print(f"Congratulations! You won ${winnings}!")
        else:
            print("Sorry, you didn't win this time.")


if __name__ == "__main__":
    play_game()