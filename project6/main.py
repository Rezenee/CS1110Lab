import random
def main():
    dict1 = {} 
    try:
        file = input('Enter the name of the words file: ')
        with open(file + '.txt') as f:
            for line in f:
                key, value = line.strip().split(':')
                values = value.split(',')
                dict1[key] = values
            
    except FileNotFoundError:
        print('Invalid File')

    print(dict1)
    print(f'The number of english words in the dictionary {len(dict1)}')
#    name = input('Enter your full name: ')
#    date = input('Enter the date of this quiz: ')
    
    # Data validation for number of words
    while True:
        try:
            wordCount = int(input('How many words would you like to be quized on: '))
        except ValueError:
            continue
        if not 0 < wordCount <= len(dict1):
            print(f'Enter an amount of words between 1 and {len(dict1)}')
            continue
        break

    words = []
    for i in range(wordCount):
        words.append((dict1.pop(random.choice(list(dict1.keys() )))))

    print(words)
    
    
if __name__ == '__main__':
    main()
