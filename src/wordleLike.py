# wordleLike, a game inspired by wordle by Josh Wardle.

from wlFunctions import getGuess, getInteger, wordGuess
import random, sys, colorama

colorama.init() # load colours

# loading letters

try:
    wordsFile = open("words.txt", "r+")
    words = wordsFile.readlines()
    wordsFile.close()
except(FileNotFoundError):
    print("Words file not found.")
    sys.exit()

five_letters = []
seven_letters = []
nine_letters = []

for w in words:
    newWord = w.replace("\n", "").lower()

    if len(newWord) == 5:
        five_letters.append(newWord)
    elif len(newWord) == 7:
        seven_letters.append(newWord)
    elif len(newWord) == 9:
        nine_letters.append(newWord)

print("v1.0.0")
print("wordleLike, a game inspired by wordle by Josh Wardle.")
print("Developed by Andrea Di Antonio.\n")

print("Words count.")
print("\tFive letters: " + str(len(five_letters)))
print("\tSeven letters: " + str(len(seven_letters)))
print("\tNine letters: " + str(len(nine_letters)) + "\n")

print("Difficulty selection.")
print("\t0 - Easy")
print("\t1 - Normal")
print("\t2 - Hard")
print("\t3 - Hard AF")

try:
    difficulty = getInteger("\nSelect difficulty [0, 3]: ", range(4))
    
except(KeyboardInterrupt, EOFError):
    print("\n\nExited.")
    sys.exit(0)

if difficulty == 3:
    print("So you have chosen death.\n")
else:
    print()

while True:
    print("Starting new game.")
    print("Exit with Ctrl+C or EOF")

    try: # game interface
        length = getInteger("\nSelect word length {5, 7, 9}: ", range(5, 10, 2))
        print("\nPlaying with " + str(length) + " letters words on difficulty " + str(difficulty) + ".")

        wordList = five_letters
        letters = list("abcdefghijklmnopqrstuvwxyz")

        if length == 5:
            wordList = five_letters
        elif length == 7:
            wordList = seven_letters
        elif length == 9:
            wordList = nine_letters

        word = random.choice(wordList)

        print("It's your turn to guess the word.\n\n")

        winFlag = False
        results = []

        for r in range(length + 1):
            if len(results) > 1:
                print("Just as a reminder of your last plays...\n")

                for res in results:
                    print("\t" + res + "\n")

                print() # needed separator

            if length + 1 - r != 1:
                print("You have " + str(length + 1 - r) + " guesses.\n")
            else:
                print("You only have 1 guess.")
                print("Use it wisely.\n")

            if difficulty < 2:
                availableLetters = ""

                for l in letters:
                    availableLetters += l + " "

                if difficulty == 0:
                    print(str(len(letters)) + " letters available: " + str(availableLetters))
                else:
                    print("Letters available: " + str(availableLetters))

            guess = getGuess(length, wordList, difficulty)
            guessResult, toBeExcluded, newResult = wordGuess(word, guess, difficulty, letters)

            results.append(newResult)

            for l in toBeExcluded:
                try:
                    letters.remove(l)
                except(ValueError):
                    continue

            print("\n") # needed separator

            if guessResult == 1:
                winFlag = True
                break
        
        print("The game has ended.")
        print("This was your game.\n")

        for res in results:
            print("\t" + res + "\n")                
        
        if not winFlag:
            print("Sadly you didn't win...")
            print("The word was " + word.upper() + "\n\n")
        else:
            print("\nYou've guessed the word.")
            print("It was indeed " + word.upper() + ".\n\n")

    except(KeyboardInterrupt, EOFError):
        print("\n\nExited.")
        break