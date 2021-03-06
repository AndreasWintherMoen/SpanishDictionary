FILE_NAME = "dictionary.txt"

def GetDictionaryFromFile():
    file = open(FILE_NAME, "r", encoding="latin-1")
    dictionary = []
    for line in file:
        words = line.split("\t")
        englishWords = words[0].split(",")
        if "," in words[1]:
            spanishWords = words[1].split(",")
        else:
            spanishWords = [words[1]]
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
        line += "\t"
        for spanishWord in wordEntry[1]:
            line += (spanishWord + ",")
        line = line[:len(line)-1]
        line += "\n"
        file.write(line)
    file.close()

def WordExistsInDictionary(word, language):
    dictionary = GetDictionaryFromFile()
    if (language.lower() == "english"):
        for line in dictionary:
            for dicWord in line[0]:
                if dicWord == word:
                    return True
    elif (language.lower() == "spanish"):
        for line in dictionary:
            for dicWord in line[1]:
                if dicWord == word:
                    return True
    else:
        raise NameError("Illegal language name in WordExistsInDictionary(word, language)")
    return False

def AddWordEntry(english, spanish):
    englishExists = WordExistsInDictionary(english, "english")
    spanishExists = WordExistsInDictionary(spanish, "spanish")
    newLine = ""
    if (englishExists and spanishExists):
        # Exact same word entry already exists, so we just return
        print(english + "/" + spanish + " already exists in dictionary")
        return
    elif (englishExists):
        # The english word already exists, but with another translation. So, we want to add a new translation
        dictionary = GetDictionaryFromFile()
        found = False
        for line in dictionary:
            if (found): break
            for word in line[0]:
                if word == english:
                    found = True
                    line[1].append(spanish)
                    break
        AddDictionaryToFile(dictionary)
        print(english + " already exists in dictionary. " + spanish + " was added as an alternative translation")
    elif (spanishExists):
        # Spanish exists already, but not English. 
        dictionary = GetDictionaryFromFile()
        found = False
        for line in dictionary:
            if (found): break
            for word in line[1]:
                if word == spanish:
                    line[1].append(english)
                    found = True
                    break
        AddDictionaryToFile(dictionary)
        print(spanish + " already exists in dictionary. " + english + " was added as an alternative translation")
    else:
        # Word entry is entirely new, so we just append directly to the file
        file = open(FILE_NAME, "a")
        newLine = english.lower() + "\t" + spanish.lower() + "\n"
        file.write(newLine)
        file.close()
        print(english + "/" + spanish + " successfully added to dictionary")

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
    if (numTests == 0):
        print("The program will continue indefinitely. Type 'forcequit' to exit")
    i = 0
    while (i < numTests or numTests == 0):
        line = dictionary[i % (len(dictionary) - 1)]
        englishWords = line[0]
        spanishWords = line[1]
        language = random.randint(0,1)
        i += 1
        
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
        if (userAnswer.lower() == "forcequit"):
            return
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
        num = int(input("How many tests would you like to run (0 for infinite)? "))
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
