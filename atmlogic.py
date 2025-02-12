balance = 45000.95
pin = 4321

print("Welcome to the Bank Of Python")
print("Please insert your card.")
input_pin = int(input("Enter your account PIN: "))

while True:
    if input_pin == pin:

        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")

        choice = input("Enter your choice: ")

        if choice == '1':

            print("Your current balance = "+ str(balance))

        elif choice == '2':

            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance = balance + amount
                print("Deposited amount = "+ str(amount))

                print("1. Check balance and Exit")
                print("2. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    print("Your current balance = "+ str(balance))
                    print("Thank you for banking with us.")
                    break
                elif choice == '2':
                    print("Thank you for banking with us.")
                    break

        elif choice == '3':

            amount = float(input("Enter amount to withdraw: "))

            if amount > 0 and amount <= balance:
                balance = balance - amount
                print(str(amount) + "withdrawn successfully.")

                print("1. Check balance and Exit")
                print("2. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    print("Your current balance = "+ str(balance))
                    print("Thank you for banking with us.")
                    break
                elif choice == '2':
                    print("Thank you for banking with us.")
                    break

            elif amount > balance:
                print("Insufficient funds. Please Try again")
            else:
                print("Invalid withdrawal amount. Please Try again")
                
        else:
            print("Invalid choice. . Please Try again")
    else:
        print("Invalid PIN")
        print("Thank you for banking with us.")
        break