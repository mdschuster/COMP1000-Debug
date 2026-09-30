# Savings Goal Tracker

def main():
    name = input("What's your name? ")
    balance = float(input("Starting balance: $"))
    deposit = float(input("Weekly deposit: $"))
    goal = float(input("Savings goal: $"))

    weeks = 1

    if deposit <= 0:
        print("Your weekly deposit has to be more than $0.")
    else:
        while balance <= goal:
            balance + deposit
            weeks = weeks + 1

        print()
        print(f"{name}, you'll reach your goal in {weeks} weeks.")
        print(f"Final balance: ${balance:.2f}")

        if weeks > 52:
            print("That's a year or more. Hang in there!")
        elif weeks <= 4:
            print("You'll be there in no time!")
        else:
            print("Keep it up!")

if __name__ == "__main__":
    main()