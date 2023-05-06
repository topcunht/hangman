import random
import string

with open('hangman_words.txt') as f:
    contents = f.read()
    wordsList = contents.split(",")
    newList = []
def getValidateWords():
    # removing invalid words
    for words in wordsList:
        newList.append(words[1:len(words)-1])
        for word in newList:
            if "-" in word or " " in word:
                newList.remove(word)
    # choosing random word
    comp_word = random.choice(newList)
    return comp_word.upper()
def hangman():
    computer_word = getValidateWords()
    word_letter = set(computer_word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set() 
    live = 6
    while len(word_letter) > 0 and live > 0:
        print("You have ", live ,"lives and used these words: ", "".join(guessed_letters))
        printedWord = []
        for letter in computer_word:
            if letter in guessed_letters:
                printedWord.append(letter)
            else:
                printedWord.append("-")
        print("Guessed word is now:","".join(printedWord)) 
        user_letter = input("Enter a letter: ").upper()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                live -= 1
                
        elif user_letter in guessed_letters:
            print("You already enter this letter. Try another letter.")    
        else:
            print("Invalid input.")
    if live == 0:
        print("You died. :(( The word was", computer_word, "")
    else:
        print(f"Congrats!!! You find the right word {computer_word}")
hangman()   
    
    
                

    