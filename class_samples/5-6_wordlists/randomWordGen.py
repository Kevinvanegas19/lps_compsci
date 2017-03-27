wordsFile = open('words.txt')

myWord = wordsFile.readline()
wordsList = []

while myWord != '':
	wordsList.append(myWord)
        myWord = wordsFile.readline()

wordsListLength = len(wordsList)

import random

myRandWord = random.randint(0,wordsListLength)

print(wordsList[myRandWord])
