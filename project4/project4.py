def main():
    filename_prefix = input("Enter a file prefix: ")

    filename_old = filename_prefix + '_old.txt'
    filename_new = filename_prefix + '_new.txt'

    try:
        with open(filename_old, 'r') as f_old, open(filename_new, 'w') as f_new:
            while True:
                acount_closed = False
                line = f_old.readline().strip()

                # Gets the id number, and returns if it is EOF
                number = get_number(line)
                if number == 999999:
                    print("End of file")
                    f_new.write("999999\n")
                    return

                # Get the balance and name if line is valid entry
                balance = get_balance(line)
                name = get_name(line)
                print(f"Verifying input: {number} {balance} {name}")

                # Goes through all possible actions the user wants for each account
                while True:
                    command = get_command()
                    if command == 'a':
                        break

                    if command == 'c':
                        acount_closed = close_account(balance)
                        if acount_closed:
                            break

                    if command == 'd':
                        balance = deposit(balance)
                    if command == 'w':
                        balance = withdrawal(balance)

                # if the person did not say to close the acount, write the new values
                if not acount_closed:
                    f_new.write(f'{number} {balance:10.2f} {name}\n')

    except FileNotFoundError:
        print(f"The file name {filename_old} does not exist")
        return

def close_account(balance):
    if balance > 0:
        print("Account not closed because money is still in it.")
        return False
    return True 

def deposit(balance):
    while True:
        try:
            deposit_amount = float(input("Enter a deposit amount: "))
        except ValueError:
            print("Invaled Value")
            continue
        if deposit_amount < 0:
            print("You cannot deposit a negative amount.")
            continue
        if deposit_amount + balance > 9999999.99:
            print("You cannot have more than 9999999.99 in your account.")    
            continue
        return balance + deposit_amount

def withdrawal(balance):
    while True:
        try:
            withdrawal_amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid Value")
            continue
        if withdrawal_amount < 0:
            print("You cannot withdrawal a negative number.")
        if withdrawal_amount > balance:
            print("You cannot afford this withdrawal")
            continue
        print(f"New balance = {balance - withdrawal_amount}")
        return balance - withdrawal_amount
        
def get_number(line):
    return int(line[0:6])

def get_balance(line):
    return int(float(line[6:17]) * 100)

def get_name(line):
    return line[18::] 

def get_command():
    while True:
        command = input("Enter a command (a,c,d,w): ")
        if command.lower() not in ['a','c','d','w']:
            print(f"Entered an invalid command {command}")
            continue
        return command.lower()
            






























if __name__ == '__main__':
    main()
