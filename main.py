import random

# Global Variable
MIN_DEPOSIT = 30
MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10

# Slots
ROWS = 3
COLS = 3

# A dictionary to identify the symbols in the slot machine
symbol_count = {
    "A": 4,
    "B": 8,
    "C": 8,
    "D": 8
}

symbol_value = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}

# Check for winning condition
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break # If breaks, it will not go to else
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,  winning_lines


# Slot machine mechanics
def get_machine_spin(rows, cols, symbols):
    all_symbols = []
    # .items will give the key and the value associated with the dictionary 
    for symbol, symbol_count in symbols.items():
        # annonymous _ variable for python
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    # For every column, generate the rows
    for _ in range(cols):
        # Each value chosen must be removed from the list so it wont be chosen again (eg. max 2 A's)
        column = []
        current_symbols = all_symbols[:] # Slicing the all_symbols so that current_symbols does not act as just a reference
        for _ in range(rows):
            value = random.choice(current_symbols)
            # Remove from current list
            current_symbols.remove(value)
            # Add to the column
            column.append(value)

        columns.append(column)

    return columns


# Printing the generated slot machine
def print_slot_machine(columns):
    # Transposing the matrix so that it is in the right position
    for row in range(len(columns[0])): # At least 1 column
        for i, column in enumerate(columns): # Enumerate will give the index and item
            # Formatting the slot machine display
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end = "")

        print()

# Get user input
def deposit():
    # Continuously give input until valid
    while True:
        amount = input(f"How much for this deposit? Minimum RM{MIN_DEPOSIT}: RM")

        # Validation check for valid digit (no negatives or non-digit characters)
        if amount.isdigit():
            amount = int(amount)

            # Break out of the while loop if it is a valid amount
            if amount >= MIN_DEPOSIT:
                break
            else:
                print(f"Amount must be greater than RM{MIN_DEPOSIT}.")

        # Tell users for a valid input
        else:
            print("Please enter a number!")

    return amount


# For the number of lines the user is betting on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on! [1-" + str(MAX_LINES) + "]? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a valid number")
    
    return lines

# Get the user bet amount for each line
def get_bet():
    while True:
        bet_amount = input(f"How much would you like to bet on each line? From RM{MIN_BET} - RM{MAX_BET}: RM")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount >= MIN_BET and bet_amount <= MAX_BET:
                break
            else:
                print(f"Please enter a valid amount to bet. Between RM{MIN_BET} - RM{MAX_BET}")
        else:
            print("Please enter a number!")

    return bet_amount

def display_rules():
    print(
        """
        ------------------------------------------
        Rules:
        This Game will ask you to deposit a certain amount of money! Using this money, you will bet on up to 3 lines
        
        How To Win:
        Betting on 1 line: The top row
        Betting on 2 lines: The top and middle row
        Betting on 3 lines: All rows!
        
        If the rows display the same symbols, you have successfully won the bet on that row!
        ------------------------------------------
        """)

    back_option = input("Press Any Key to RETURN")


def display():
    print(
        """
        ------------------------------------------\n
        Welcome to Sean's Simple Slot Machine Game

        """
        )
    print("Press 'P' to Play, 'I' for Instructions, or 'Q' to Quit")
    option = input()

    return option

# Game logic
def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough to bet that amount!")
            print(f"Current Balance: RM{balance}")
        else:
            break

    print(f"Your Current Bet: RM{bet}")
    print(f"Number of Lines: {lines}")
    print(f"You are betting RM{bet} on {lines} line(s). The total bet is RM{total_bet} \n")

    slots = get_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    print()
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won RM{winnings}!")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


# Place the running functions inside main() for easier calling/access
def main():
    option = display()
    match option.upper():
        case "P":
            balance = deposit()
            while True:
                print(f"Current Balance: RM{balance}")
                spin = input("Press Enter to PLAY (Q to quit).")
                if spin.upper() == "Q":
                    break
                balance += game(balance)
            
            print(f"You left with RM{balance}")
        
        case "I":
            display_rules()

        case "Q":
            print("Thank you for playing!")
            SystemExit(0)


main()