# wordcreator, words creator utility for wordleLike

wordsFile = open("words.txt", "r+")
words = wordsFile.readlines()
wordsFile.close()

newWords = []

for w in words:
    if len(w.replace("\n", "")) in [5, 7, 9] and w not in newWords:
        newWords.append(w.lower())

wordsFile = open("words.txt", "w+")
wordsFile.writelines(newWords)
wordsFile.close()