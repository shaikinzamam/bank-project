print("Welcome to our bank")

bank_account = {
    "name": "max",
    "pin": "123",
    "balance_amount": 1293847564
}

userpin = input("Enter your pin: ")

if userpin == bank_account["pin"]:
    while True:
        print("\nHow can I help you!")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Check balance
        if choice == "1":
            print("Your balance is:", bank_account["balance_amount"])

        # Deposit
        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            if amount.isdigit():
                bank_account["balance_amount"] += int(amount)
                print("Amount deposited. New balance:", bank_account["balance_amount"])
            else:
                print("Invalid amount!")

        # Withdraw
        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            if amount.isdigit() and int(amount) <= bank_account["balance_amount"]:
                bank_account["balance_amount"] -= int(amount)
                print("Please collect your cash. Remaining balance:", bank_account["balance_amount"])
            else:
                print("Insufficient balance or invalid amount.")

        # Change PIN
        elif choice == "4":
            old_pin = input("Enter old PIN: ")
            if old_pin == bank_account["pin"]:
                new_pin = input("Enter new PIN: ")
                bank_account["pin"] = new_pin
                print("PIN successfully changed!")
            else:
                print("Incorrect PIN!")

        # Exit App
        elif choice == "5":
            print("Thank you for using our service!")
            break

        else:
            print("Invalid choice! Please select between 1 to 5.")
else:
    print("Incorrect PIN!")
