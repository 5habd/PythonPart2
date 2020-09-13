def countwordsFromFile ():
    fileName = input("enter a file name: ")
    noOfWords = 0
    file = open (fileName,"r")
    for  line in file :
        words = line.split()
        noOfWords = noOfWords + len(words)
    print("number of words in the file is: ")
    print(noOfWords)
countwordsFromFile()