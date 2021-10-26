# Project No.: Project 4
# Author: Zane Rickert
# This program lets a user edit an existing file that has entries of users 
# in a bank. They can withdrawal, deposit, or close accounts. The updated
# information is put in a new output file. 

def main():
    # Gets filename prefix, and assigns txt of old and new file
    filename_prefix = input("Enter a file prefix: ")
    filename_old = filename_prefix + '_old.txt'
    filename_new = filename_prefix + '_new.txt'

    # Attempts to open both files
    try:
        with open(filename_old, 'r') as f_old, open(filename_new, 'w') as f_new:
            while True:
                account_closed = False
                # Gets each line from the original file one at a time to work with
                line = f_old.readline().strip()

                # Gets the id number, and returns if it is EOF
                number = get_number(line)
                if number == 999999:
                    print("End of file")
                    f_new.write("999999\n")
                    return

                # Get the balance and name if line is valid entry
                balance_dollars = get_balance(line) 
                balance_cents = int(balance_dollars * 100) 
                name = get_name(line)
                print(f"Verifying input: {number} {balance_dollars} {name}")

                # Goes through all possible actions the user wants for account
                # When user types a, break out of loop to read next user
                while True:
                    command = get_command()
                    if command == 'a':
                        balance_dollars = balance_cents / 100
                        print(f"New balance: {number} {balance_dollars} {name}")
                        break

                    elif command == 'c':
                        account_closed = close_account(balance_cents)

                    elif command == 'd':
                        balance_cents = deposit(balance_cents)

                    else:
                        balance_cents = withdrawal(balance_cents)

                # if the person did not say to close the acount, write the new values
                if not account_closed:
                    f_new.write(f'{number} {balance_dollars:10.2f} {name}\n')

    # If either file fails to open quit the program.
    except IOError:
        print(f"The file name {filename_old} does not exist")
        return

def close_account(balance):
    # Checks if the account is empty before closing
    if balance > 0:
        print("Account not closed because money is still in it.")
        return False

    print("Account is closed")
    return True 

def deposit(balance):
    while True:
        # asks user for valid deposit amount, repeats until valid amount submitted
        try:
            deposit_amount = int(float(input("Enter a deposit amount: ")) * 100)
        except ValueError:
            print("Invaled Value")
            continue
        if deposit_amount < 0:
            print("You cannot deposit a negative amount.")
            continue
        if deposit_amount + balance > 999_999_999:
            print("You cannot have more than 9999999.99 in your account.")    
            continue

        return balance + deposit_amount

def withdrawal(balance):
    while True:
        # asks user for valid withdrawal amount, repeats until valid amount is submitted
        try:
            withdrawal_amount = int(float(input("Enter withdrawal amount: ")) * 100)
        except ValueError:
            print("Invalid Value")
            continue
        if withdrawal_amount < 0:
            print("You cannot withdrawal a negative number.")
            continue
        if withdrawal_amount > balance:
            print("You cannot afford this withdrawal")
            continue

        return balance - withdrawal_amount
        
def get_number(line):
    # Gets the first 6 characters of line, this is always the ID
    return int(line[0:6])

def get_balance(line):
    # Digits index 6 through 17 are the balance
    return float(line[6:17])

def get_name(line):
    # The rest of the digits are the name
    return line[18::] 

def get_command():
    # Re propmt the user until the command is a valid command
    while True:
        command = input("Enter a command (a,c,d,w): ")
        if command.lower() not in ['a','c','d','w']:
            print(f"Entered an invalid command {command}")
            continue

        return command.lower()

if __name__ == '__main__':
    main()
