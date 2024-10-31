# Main loop
def banking_game():
    accounts = {} # An empty dictionary that stores users name and history balance

    print("Welcome to the Banking Game!")
    print("1. Create Amount\n2. Deposite Money\n3. Withdrawn Money\n4. View Balance\n5. Transitory History\n6. Exit")
    while True:
        try:
            select = int(input("\nSelect an option (1-6): "))
            # Creates amount
            if select == 1:
                name = input("Enter your name: "). strip()
                if name.replace(" ",'').isalpha():
                    if name not in accounts:
                        accounts[name] = {'balance':0, 'history': []}
                        print("Account created successfully!")
                    else:
                        print("An account with the name exists already!")
                else:
                    print("Invalid input,please enter only alphabets")
                    name = input("Re-enter your name again: ")
            # Desposite amount 
            elif select == 2:
                name = input("Enter your account name: ").strip()
                if name in accounts:
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
            # Withdraw amount 
            elif select == 3:
                name = input("Enter your account name: ").strip()
                if name in accounts:
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
            # View amount 
            elif select == 4:
                name = input("Enter your account name: ").strip()
                if name in accounts:
                    print(f"Current balance for {name} is : ${accounts[name]['balance']}")
                else:
                    print("Account not found,please create account")
            # Transactory history 
            elif select == 5:
                print("\n--- Transaction History ---")
                name = input("Enter your account name: ").strip()
                if name in accounts:
                    if accounts[name]['history']:
                        print(f"Transactory History for {name} is:")
                        for transaction in accounts[name]['history']:
                            print(transaction)
                    else:
                        print("No transaction found!")
                else:
                    print("Account not found,please create your account first")
            # Exiting the gam3
            elif select == 6:
                print("Exiting the banking game!")
                break
        except ValueError:
            print("Invalid input.Try again!")
banking_game()

