def main():
    numberList = [0] * 26 
    lettersList=[(chr(ord('a')+i)) for i in range(26)]
    
    while True:
        try:
            repeatAmount = int(input("Enter a positve integer: "))
        except ValueError:
            continue
        if repeatAmount <= 0:
            continue
        else:
            break
        
    combinedString = userString(repeatAmount) 
    showString(combinedString) 
    
    lowerCaseString = convertStringLower(combinedString)

    stringList = stringToList(lowerCaseString)
    
    compressedString = compressList(stringList)
    frequencyCount(numberList, lettersList, compressedString)
    print(numberList)

def userString(iterator):
    combinedString = ''
    print("Input {} strings.".format(iterator))
    for i in range(iterator):
        strInput = input("Enter a string: ")
        combinedString += strInput

    return combinedString

def showString(string):
    print(string)

def convertStringLower(string):
    return string.lower() 

def stringToList(string):
    strList = [] 
    for char in string:
        strList.append(char)

    print(strList)
    return strList

def compressList(listItem):
    stringConvert = ''
    for item in listItem:
        if 'a' <= item  <= 'z':
            stringConvert += item

    return stringConvert

def frequencyCount(numberArray, lettersArray, string):
    for char in string:
        numberArray[ord(char) - 97] += 1

def showFrequency():
    pass


if __name__ == '__main__':
    main()
