FILE_NAME = "dictionary.txt"

def GetDictionaryFromFile():
    file = open(FILE_NAME, "r")
    dictionary = []
    for line in file:
        words = line.split("\t")
        englishWords = words[0].split(",")
        spanishWords = words[1].split(",")
        spanishWords[len(spanishWords)-1] = spanishWords[len(spanishWords)-1].strip("\n")
        dictionary.append([englishWords, spanishWords])
    file.close()
    return dictionary

def AddDictionaryToFile(dictionary):
    file = open(FILE_NAME, "w")
    for wordEntry in dictionary:
        line = ""
        for englishWord in wordEntry[0]:
            line += (englishWord + ",")
        line = line[:len(line)-1]
        line += "\n"
        file.write(line)
    file.close()

def AddWordEntry(english, spanish):
    file = open(FILE_NAME, "a")
    newLine = english.lower() + "\t" + spanish.lower() + "\n"
    file.write(newLine)
    file.close()

def GetSpanishWord(englishWord):
    dictionary = GetDictionaryFromFile()
    for line in dictionary:
        for word in line[0]:
            if (word == englishWord):
                return line[1]
    print(englishWord + " not found in dictionary")
    return None

def GetEnglishWord(spanishWord):
    dictionary = GetDictionaryFromFile()
    for line in dictionary:
        for word in line[1]:
            if (word == spanishWord):
                return line[0]
    print(spanishWord + " not found in dictionary")
    return None

def ValidateAnswer(correctAnswers, userAnswer):
    for answer in correctAnswers:
        if answer == userAnswer:
            return True
    return False

def RunTests(numTests):
    import random
    dictionary = GetDictionaryFromFile()
    random.shuffle(dictionary)
    for i in range(numTests):
        line = dictionary[i % (len(dictionary) - 1)]
        englishWords = line[0]
        spanishWords = line[1]
        language = random.randint(0,1)
        
        userAnswer = ""
        correctAnswers = []
        if (language == 0):
            word = englishWords[random.randint(0, len(englishWords) - 1)]
            userAnswer = input("What is the Spanish word for " + word + "? ")
            correctAnswers = spanishWords
        else:
            word = spanishWords[random.randint(0, len(spanishWords) - 1)]
            userAnswer = input("What is the English word for " + word + "? ")
            correctAnswers = englishWords
        if (ValidateAnswer(correctAnswers, userAnswer)):
            print("Correct!")
        else:
            print("Wrong. The answer was ", end="")
            for w in correctAnswers:
                print(w, end=" ")
            print("")
            

def AskUserAction():
    answer = ""
    while (answer != "x" and answer != "t" and answer != "a" and answer != "s" and answer != "e"):
        answer = input("Exit (X), Run tests(T), Add to dictionary (A), get spanish translation (S), get english translation (E): ").lower()
    if (answer == "x"):
        return False
    elif (answer == "t"):
        num = int(input("How many tests would you like to run? "))
        RunTests(num)
    elif (answer == "a"):
        english = input("English word: ")
        spanish = input("Spanish word: ")
        AddWordEntry(english, spanish)
    elif (answer == "s"):
        words = None
        english = input("English word: " )
        words = GetSpanishWord(english)
        if (words != None):
            for word in words: print(word)
    elif (answer == "e"):
        words = None
        spanish = input("Spanish word: " )
        words = GetEnglishWord(spanish)
        if (words != None):
            for word in words: print(word)
    return True

def main():
    while(AskUserAction()):
        print("")
    
    
        

main()
