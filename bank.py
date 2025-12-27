print("Welcome to our bank")

bank_account={
    "name":"max",
    "pin":"123",
    "balance_amount": "1293847564"
}
userpin=(input("enter your pin:"))

if userpin == bank_account["pin"]:
    while True:
      print("\nHow can i help you!")
      print("1.check balance")
      print("2.Deposit money")
      print("3.withdraw money")
      print("4.change PIN")
      print("5.Exit")
      choice = input("Enter your choice(1-5): ")
      if choice == "1":
          print("your balance is:",bank_account["balance_amount"])
      elif choice == "2":
          amount = input("enter amount to deposit:")
          if amount.isdigit():
           bank_account["balance_amount"] = str(int(bank_account["balance_amount"])+int(amount))
           print("Amount deposited.New balance is:",bank_account["balance_amount"])

          else:
             print("invalid amount.")
          
          
      elif choice =="3":
         amount = input("enter amount to withdraw: ")
         if amount.isdigit() and int(amount)<= int(bank_account["balance_amount"]):
              bank_account["bank_amount"]=str(int(bank_account["balance_amount"])-int(amount))
              print("please collect your cash.remaining balance is:",bank_account["balance_amount"])
         else:
            print("insufficient balance or invalid amount.")
      elif choice=="4":
         old_pin =input("enter old PIN")
         if old_pin == userpin:
            print("new_pin") 
         else:
            print("incorrect PIN!")
            break
         new_pin = input("enter new PIN:")
         bank_account["pin"] = new_pin
         print("PIN successfully changed.")
      elif choice == "5":
         print("Thank you for using our service!")
         break
      else:
         print("invalid choice. please select between 1 to 5.")
     
else:
    print("incorrect PIN!")
    


    