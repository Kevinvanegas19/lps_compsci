wordsFile = open('words.txt')

myWord = wordsFile.readline()
wordsList = []

while myWord != '':
	#as long as there are more words
	#put the word in the list & read another

	wordsList.append(myWord)
	myWord = wordsFile.readline()

print(wordsList[666])
