# Project No.: 3
# Author: Zane Rickert
# Description: This program will ask the user how many strings of text they 
#              want to enter, it will then compress the string into just
#              letters, and print the amount of times each letter shows up
#              in their passage of text. It will also check if the text is 
#              a palindrone in an external function. 
import testModule
def main():
    numberList = [0] * 26 
    lettersList=[(chr(ord('a')+i)) for i in range(26)]
    
    while True:
        try:
            m = int(input("Enter the number of strings you want to read: "))
        except ValueError:
            continue
        if m <= 0:
            continue
        else:
            break
        
    print(m)

    combinedString = userString(m) 
    showString(combinedString) 
    
    lowerCaseString = convertStringLower(combinedString)

    stringList = stringToList(lowerCaseString)
    
    compressedList = compressList(stringList)
    frequencyCount(numberList, lettersList, compressedList)

    palindrome = testModule.checkPalindrome(compressedList)
    if palindrome:
        print("These letters do form a palindrome.")
    else:
        print("These letters do not form a palindrome.")
    print('')
    showFrequency(numberList, lettersList)

def userString(iterator):
    st = ''
    for i in range(iterator):
        strInput = input(f"Enter string {i + 1}: ")
        st += strInput

    return st

def showString(string):
    print(string)

def convertStringLower(string):
    return string.lower() 

def stringToList(string):
    strList = [] 
    for char in string:
        strList.append(char)

    print(''.join(strList))
    return strList

def compressList(originalList):
    compressedList = [] 
    for letter in originalList:
        if 'a' <= letter  <= 'z':
            compressedList.append(letter) 

    print(''.join(compressedList))
    return compressedList

def frequencyCount(numberArray, lettersArray, string):
    for char in string:
        numberArray[ord(char) - 97] += 1

def showFrequency(freqDistributionList, lettersArray):
    print("Folliwing is the frequency distribution for the letters in the list.")
    for i, letter in enumerate(lettersArray):
        print(letter, "*" * freqDistributionList[i])

if __name__ == '__main__':
    main()
