def main():
    filename_prefix = input("Enter a file prefix: ")

    filename_old = filename_prefix + '_old.txt'

    try:
        with open(filename_old, 'r') as f_old:
            while True:
                line = f_old.readline().strip()
                while True:
                    # Gets the id number, and returns if it is EOF
                    number = get_number(line)
                    if number == 999999:
                        print("End of file")
                        return

                    # Get the balance and name if line is valid entry
                    balance = get_balance(line)
                    name = get_name(line)
                    print(f"Verifying input: {number} {balance} {name}")
                    command = get_command()
                    if command == 'a':
                        break

                    if command == 'c':
                        pass
                        
                    if command == 'd':
                        pass
                    if command == 'w':
                        pass

    except FileNotFoundError:
        print(f"The file name {filename_old} does not exist")
        return

def get_number(line):
    split = line.split()
    return int(split[0])

def get_balance(line):
    split = line.split()
    return float(split[1])

def get_name(line):
    split = line.split()
    sentences_strings = ' '.join(split[2:len(split)]) 
    return sentences_strings 

def get_command():
    while True:
        command = input("Enter a command (a,c,d,w): ").lower()
        if command not in ['a','c','d','w']:
            print("Invalid Command")
            continue
        return command
            
def withdrawal():
    while True:
        try:
            withdrawal_amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            continue
         
    
if __name__ == '__main__':
    main()
