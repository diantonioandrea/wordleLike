# worldleLike functions

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def getInteger(request: str, rng: list) -> int:
    while True:
        try:
            integer = int(input(request))

            if integer in rng:
                return integer
                
        except:
            continue

def getGuess(length: int, wordList: list, diff: int) -> str:
    while True:
        guess = str(input("\nMake a guess: "))

        if guess not in wordList and diff != 0:
            print("Word not in word-list.\n")
            continue

        if len(guess) == length:
            return guess.lower()

def wordGuess(word: str, guess: str, diff: int, availableLetters: list) -> int:
    print("\nGuess: " + guess + "\n")
    length = len(word)

    letters = list(word)
    toBeExcluded = []

    result = []

    for l in range(length):
        if word[l] == guess[l] and diff < 3:
            letters.remove(word[l])
            result.append(bcolors.GREEN + guess[l].upper() + bcolors.ENDC)

        else:
            result.append(guess[l].upper())

        
    if diff < 2:
        for l in range(length):
            if guess[l] in letters and guess[l] != word[l]:
                letters.remove(guess[l])
                result[l] = bcolors.YELLOW + guess[l].upper() + bcolors.ENDC
        
    if diff < 2:

        if diff == 0:
            for l in range(length):
                if guess[l] not in availableLetters:
                    result[l] = bcolors.RED + guess[l].upper() + bcolors.ENDC

        for l in range(length):
            if guess[l] not in word:
                toBeExcluded.append(guess[l])

    resultString = ""

    for r in result:
        resultString += r + " "
    
    print("The result is: " + resultString)

    if word == guess:
        return 1, [], resultString

    return -1, toBeExcluded, resultString