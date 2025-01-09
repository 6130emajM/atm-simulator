# Initial setup
correct_pin = "1234"
balance = 1000.0

# Ask for the user's PIN
entered_pin = input("Enter your 4-digit PIN: ")
if entered_pin != correct_pin:
    print("Incorrect PIN. Access denied.")
    exit()

# Start the ATM menu loop
while True:
    print("\nWelcome to the ATM!")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice = input("Choose an option (1, 2, or 3): ")
    if choice == "1":
        # Show balance
        print(f"Your current balance is: ${balance:.2f}")

    elif choice == "2":
        # Withdraw money
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    elif choice == "3":
        # Exit the program
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")


            