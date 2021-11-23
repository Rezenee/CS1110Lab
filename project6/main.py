import random
def main():
    dict1 = {} 

    filename = input("Please enter a file name: ")

    dict1 = get_dic(filename)

    print(f'{len(dict1)} entries found.')
    name = input('Please enter your full name: ')
    date = input('Please enter the date: ')
    print('')
    
    # Data validation for number of words
    while True:
        try:
            word_count = int(input('How many words would you like to be quized on? '))
        except ValueError:
            print('Please enter a valid number.')
            continue
        if not 0 < word_count <= len(dict1):
            print(f'Please enter a valid number between 1 and {len(dict1)}')
            continue
        break

    # Get random list of english words wordCount number of times
    quiz_dict = {}
    
    print('')
    for key in random.sample(list(dict1.keys()), word_count):
        quiz_dict[key] = [dict1[key], False]

    # Quiz the user on the words in the list
    for english_word in quiz_dict:
        spanish_word_count = len(dict1[english_word])
        spanish_inputs = []
        print(f'English word: {english_word}')
        print(f'Enter {spanish_word_count} equivalent Spanish word(s).')
        for i in range(spanish_word_count):
            spanish_inputs.append(input(f'Word [{i + 1}]:'))

        if check_quiz_words(dict1, english_word, spanish_inputs):
            quiz_dict[english_word][1] = True

        print('---')

    
    correct = 0
    for key in quiz_dict:
        if quiz_dict[key][1]:
            correct += 1

    print(f'{correct} out of {word_count} correct.')
    output_file = input("Enter an output file (or press enter to quit): ")

    print('\nBye!')
    if output_file != '':
        make_quizFile(name, date, quiz_dict)

    print(dict1)
# Receives a filename as input and returns a dictionary with key being English word
# and item being list of spanish words
def get_dic(filename):
    dict1 = {}
    try:
        with open(filename) as f:
            for line in f:
                key, value = line.strip().split(':')
                values = value.split(',')
                dict1[key] = [word.strip() for word in values]
    except FileNotFoundError:
        print('Invalid File')
        quit()

    return dict1

# Exports quiz information into external file
def make_quizFile(user_name, date, quiz_dict):
    with open('quiz.txt', 'w') as f:
        f.write(f'Name: {user_name}\n')
        f.write(f'Date: {date}\n')
        correct = 0
        total = len(quiz_dict)
        for key, value in quiz_dict.items():
            if value[1]:
                correct += 1
            words = ', '.join(str(word) for word in value[0])
            f.write(f'{key}:{words}\n')

        f.write(f'Score: {correct} out of {total} correct\n')
            
    
# Returns true or false depending on wether or not the user answered the question correctly
def check_quiz_words(source_dictionary, eng_word, spa_words):
    if source_dictionary[eng_word] == spa_words:
        print("Correct!")
        return True
    
    print("Incorrect.")
    return False

if __name__ == '__main__':
    main()
