import random
def main():
    # This dictionary will be used for the final output holding all the needed 
    # information for a output file
    quiz_dict = {}

    print("Welcome to the vocabulary quiz program.\n")
    filename = input("Please enter a file name: ")

    # call get_dic, return the dictionary into source_dictionary.
    source_dictionary = get_dic(filename)

    print(f'{len(source_dictionary)} entries found.')
    name = input('Please enter your full name: ')
    date = input('Please enter the date: ')
    print('')
    
    # Data validation for number of words
    while True:
        try:
            word_count = int(input('How many words would you like to be quizzed on? '))
        # If they do not enter a int
        except ValueError:
            print('Please enter a valid number.')
            continue
        # If the enter an int, but it is not a number of words
        if not 0 < word_count <= len(source_dictionary):
            print(f'Please enter a valid number between 1 and {len(source_dictionary)}.')
            continue

        break
    
    print('\n')
    # This picks keys from a random sample of the source dictionary keys
    # word_count times, and puts it into quiz_dict. The value of quiz dic
    # is a list with corresponding spanish word(s) aswell as false. The false
    # signifies whether or not the user answers the question correctly later. 
    for key in random.sample(list(source_dictionary.keys()), word_count):
        quiz_dict[key] = [source_dictionary[key], False]

    # Quiz the user on the words in the list
    quiz_user(quiz_dict, source_dictionary)
    
    # Goes through the quiz_dict and counts the times False got changed to True
    correct = 0
    for key in quiz_dict:
        if quiz_dict[key][1]:
            correct += 1

    print(f'{correct} out of {word_count} correct.')
    output_file = input("Enter an output file (or press enter to quit): ")
    print('\nBye!')

    if output_file != '':
        make_quiz_file(name, date, quiz_dict)

# Method to quiz the user on the words they chose
def quiz_user(quiz_dict, source_dictionary):
    # Gets english word in quiz_dict
    for english_word in quiz_dict:
        # The amount of words needed for each question
        spanish_word_count = len(quiz_dict[english_word][0])

        # Collection of user's answers
        spanish_inputs = []
        print(f'English word: {english_word}')
        print(f'Enter {spanish_word_count} equivalent Spanish word(s).')

        # Goes through and appends the user input spanish_word_count times
        for i in range(spanish_word_count):
            spanish_inputs.append(input(f'Word [{i + 1}]:'))

        # Calls function to see if the words that they submitted are correct
        # if they are, set the false bool to true
        if check_quiz_words(source_dictionary, english_word, spanish_inputs):
            quiz_dict[english_word][1] = True

        print('\n---\n')

# Receives a filename as input and returns a dictionary with key being English word
# and item being list of spanish words
def get_dic(filename):
    source_dictionary = {}
    try:
        with open(filename) as f:
            for line in f:
                key, value = line.strip().split(':')
                # Some english words have multiple spanish words, so you must 
                # split them again based on comma. 
                values = value.split(',')
                # Removes whitespace from every word in the dict.
                source_dictionary[key] = [word.strip() for word in values]

    except FileNotFoundError:
        print(f"The file name {filename} does not exist")
        print("\nBye!")
        quit()

    return source_dictionary

# Exports quiz information into external file
def make_quiz_file(user_name, date, quiz_dict):
    with open('quiz.txt', 'w') as f:
        f.write(f'Name: {user_name}\n')
        f.write(f'Date: {date}\n')
        correct = 0
        total = len(quiz_dict)
        for key, value in quiz_dict.items():
            # This index is a bool, that is true or false, whether or not
            # the word was correct or not in the quiz. 
            if value[1]:
                correct += 1
            words = ', '.join(str(word) for word in value[0])
            f.write(f'{key}:{words}\n')

        f.write(f'Score: {correct} out of {total} correct\n')
            
    
# Returns true or false depending on whether or not the user answered the question correctly
def check_quiz_words(source_dictionary, eng_word, spa_words):
    entered_words = []
    for word in spa_words:
        entered_words.append(word)
        # If the word isn't one of the correct words then return false.
        if word not in source_dictionary[eng_word]:
            print("Incorrect.")
            return False

        # If the list of the inputted words length is not equal to the set
        # That means that they must have repeated words.
        if len(set(entered_words)) != len(entered_words): 
            print("Incorrect.")
            return False

    # If passes every check return true
    print("Correct!")
    return True

# Run program
if __name__ == '__main__':
    main()
