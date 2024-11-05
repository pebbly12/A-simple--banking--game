# Main loop
def banking_game():
    accounts = {} # An empty dictionary that stores users name and history balance

    print("Welcome to the Banking Game!")
<<<<<<< HEAD
    print("1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. View Balance\n5. Transitory History\n6. Exit")
    while True:
        try:
            select = int(input("\nSelect an option (1-6): "))
            # Create amount
=======
    print("1. Create Amount\n2. Deposite Money\n3. Withdrawn Money\n4. View Balance\n5. Transitory History\n6. Exit")
    while True:
        try:
            select = int(input("\nSelect an option (1-6): "))
            # Creates amount
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
            if select == 1:
                name = input("Enter your name: "). strip()
                if name.replace(" ",'').isalpha():
                    if name not in accounts:
                        accounts[name] = {'balance':0, 'history': []}
                        print("Account created successfully!")
                    else:
                        print("An account with the name exists already!")
                else:
<<<<<<< HEAD
                    print("Invalid input. Please enter only alphabets")
                    name = input("Re-enter your name again: ")

=======
                    print("Invalid input,please enter only alphabets")
                    name = input("Re-enter your name again: ")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
            # Desposite amount 
            elif select == 2:
                name = input("Enter your account name: ").strip()
                if name in accounts:
<<<<<<< HEAD
                    amount = (input("Enter deposit amount: "))
                    if amount.isnumeric():
                        amount = int(amount)
                        accounts[name]['balance'] += amount
                        accounts[name]['history'].append(f"Deposited: ${amount}")
                        print(f"${amount} deposited. New balance ${accounts[name]['balance']}")
                    else:
                        print("Invalid input only numerals are required")
                else:
                    print("Account not found. Please create your account first")

=======
                    deposite = input("Enter deposite number: ")
                    if deposite.isnumeric():
                        deposite = int(deposite)
                        accounts[name]['balance'] += deposite
                        accounts[name]['history'].append(f"Deposited: ${deposite}")
                        print(f"${deposite} deposited. New balance ${accounts[name]['balance']}")
                    else:
                        print("Invalid input amount,only numerals are required")
                else:
                    print("Account not found,please create your account first")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
            # Withdraw amount 
            elif select == 3:
                name = input("Enter your account name: ").strip()
                if name in accounts:
<<<<<<< HEAD
                    amount = input("Enter withdrawal amount: ")
                    if amount.isnumeric():
                        amount = int(amount)
                        if accounts[name]['balance'] >= amount:
                            accounts[name]['balance'] -= amount
                            accounts[name]['history'].append(f"Withdraw: ${amount}")
                            print(f"${amount} withdrawn. New balance ${accounts[name]['balance']}")
                        else:
                            print("Insufficient balance")
                    else:
                        print("Invalid input only numerals are allowed")
                else:
                    print("Account not found. Please create an account first")

=======
                    withdraw = input("Enter withdrawal amount: ")
                    if withdraw.isnumeric():
                        withdraw = int(withdraw)
                        if accounts[name]['balance'] >= withdraw:
                            accounts[name]['balance'] -= withdraw
                            accounts[name]['history'].append(f"Withdraw: ${withdraw}")
                            print(f"${withdraw} withdrawn. New balance ${accounts[name]['balance']}")
                        else:
                            print("Insufficient balance")
                    else:
                        print("Invalid input,only numerals are allowed")
                else:
                    print("Account not found.Please create an account first")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
            # View amount 
            elif select == 4:
                name = input("Enter your account name: ").strip()
                if name in accounts:
<<<<<<< HEAD
                    print(f"Current balance for {name}: ${accounts[name]['balance']}")
                else:
                    print("Account not found,please create account")

=======
                    print(f"Current balance for {name} is : ${accounts[name]['balance']}")
                else:
                    print("Account not found,please create account")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
            # Transactory history 
            elif select == 5:
                print("\n--- Transaction History ---")
                name = input("Enter your account name: ").strip()
                if name in accounts:
                    if accounts[name]['history']:
<<<<<<< HEAD
                        print(f"Transactory History for {name}:")
=======
                        print(f"Transactory History for {name} is:")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
                        for transaction in accounts[name]['history']:
                            print(transaction)
                    else:
                        print("No transaction found!")
                else:
<<<<<<< HEAD
                    print("Account not found. Please create your account first")

=======
                    print("Account not found,please create your account first")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
            # Exiting the gam3
            elif select == 6:
                print("Exiting the banking game!")
                break
<<<<<<< HEAD

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
=======
        except ValueError:
            print("Invalid input.Try again!")
>>>>>>> 77d938a9dad82d7108e9e1482a3b8f00f64977b0
banking_game()

