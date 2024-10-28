# Global Variable
MIN_DEPOSIT = 30
MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10

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

# Place the running functions inside main() for easier calling/access
def main():
    balance = deposit()
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
    print(f"You are betting RM{bet} on {lines} line(s). The total bet is RM{total_bet}")

main()