balance = 5000
pin = "1234"
def pin_validation():
    count = 5
    for attempt in range(count):
        chk_pin = input("Enter the PIN : ")

        if pin==chk_pin:
            print("Pin validation Successful")
            return True
        elif chk_pin == pin[::-1]:
            print("Dont Panic. Police will come soon")
            return False
        else:
            if count - (attempt + 1) > 0:
                print(f"Invalid PIN ! You only have {count - (attempt + 1)} attempt/s left")
            else:
                print("Your Account is locked. Please contact the Bank to Unlock")
    return False
def atm_menu():
    global balance
    locked_account = False
    while True:
        if locked_account:
            break
        try:
            print("""
            1.Check Balance
            2.Deposit Money
            3.Withdraw Money
            4.exit
            """)
            option = int(input("Enter the Option # : "))
            if option == 1:
                if pin_validation():
                    print(f"Your Account Balance is: {balance}")
                else:
                    locked_account = True
            elif option == 2:
                 try:
                    deposit = int(input("Enter the deposit amount: "))
                    if deposit > 0:
                        balance += deposit
                        print(f"Your Transaction is Successful. New balance {balance}")
                    else:
                        print("Deposit should be Positive")
                 except ValueError:
                     print("Invalid Input. Please Enter a Valid Number...!")
            elif option == 3:
                if pin_validation():
                    try:
                        withdraw = int(input("Enter the Withdraw amount: "))
                        if withdraw > balance:
                            print("Transaction Failed: Insufficient Funds.")
                        elif withdraw <= 0:
                            print("Withdrawal amount must be positive.")
                        else:
                            balance -= withdraw
                            print(f"\nWithdrawal Successful. New Balance: ${balance}")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    locked_account = True
            elif option == 4:
                print("Exiting... , \n Thank you for banking with us....!")
                break
            else:
                print("Try Again")
        except ValueError:
            print("Invalid input for option. Please Enter a number")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

atm_menu()