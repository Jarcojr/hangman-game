"""
Name: Michael Jarvis
Purpose: Develop a program that reads from a file
    uses decsison and repetition structures to solve a problem
    implements a modular design
Authenticity: I made this program by myself at home.
Last edited: 11/16/25
"""
import random

def readWords(file):
    #this function opens a text file and reads the data. It assumes the words are seperated by new lines.
    input_file = open(file, "r")
    data = input_file.read().split("\n")
    word_list = []
    #add words from list to words_list
    for word in data:
        word_list.append(word)
    #close the file
    input_file.close()
    return word_list

def randomWord(words):
    #this function accepts a list of words and selects a random word from that list and returns the single word as a string
    ran_word = random.choice(words)
    return ran_word

def getGuess(guessedLetters):
    #while loop that only exits when a valid guess is entered
    while True:
        #recieve input from use and convert input to lowercase
        guess = input("Guess a single letter: ").lower()
        #if the user enters more than one letter
        if len(guess) != 1:
            #print error and restart loop
            print("Error: You entered more than one letter")
            continue
        #if the user entered a letter already guessed
        elif guess in guessedLetters:
            #print error and restart loop
            print("Error: That letter has already been guessed")
            continue
        #add valid guess to guessedLetters list
        guessedLetters.append(guess)
        return guess

def blanks(word, guessedLetters):
    #empty string to add the display to
    display_string = ""
    #iterates through each letter in the secret word
    for letter in word:
        #checks if the letter in the secret word is in the guessedletters list
        if letter in guessedLetters:
            #if the letter is in the list, add that letter to the display string and a space
            display_string += letter + " "
        #if the letter is not in the list, add an underscore and space
        else:
            display_string += "_" + " "
    #return the display to the player (sliced out the extra blank at the end of the word)
    return display_string[:-1]
    
def gameWon(blanks):
    #iterates through each character in the blanks string
    for char in blanks:
        #if an underscore is found, the game is not won, return False
        if char == "_":
            return False
    #if the loop completes without returning False that means there are no more underscores
    #and therefore the game is won, return True.
    return True

def playGame():
    print("Lets play hangman!\n-----------------------")
    #this whole first section before the while loop initializes some key variables of the game
    #blank list for guessed letters
    guessedLetters=[]
    #read in list of words. Assumes text file is called hangman_words.txt and the file contains a list of words seperated by new lines.
    words = readWords("hangman_words.txt")
    #select random word from list
    word = randomWord(words)
    #set max guesses to 7 and incorrect guesses to 0
    max_guesses = 7
    incorrect_guesses = 0
    #used for testing
    #print("Random word is:", word)
    #initialize display
    display = blanks(word, guessedLetters)
    #while loop that runs until the game is won the amount of guesses is exceeded
    while gameWon(display) is False and incorrect_guesses < max_guesses:
        #Make a new string for the incorrect letters to be added to later
        incorrect_letters = ""
        #loop through the letters in guessedletters list
        for letter in guessedLetters:
            #if a letter in guessed letters is not in the secret word, add it to the incorrect letters string
            if letter not in word:
                incorrect_letters += letter + " "
        
        #turn status tracker that contains the display, how many guesses player has left, and the incorrect guesses so far
        print("----- Turn Status -----")
        print(f"Word: {display}")
        print(f"Guesses remaining: {max_guesses - incorrect_guesses}")
        print(f"Incorrect guesses: {incorrect_letters}")
        print()

        #get a new guess from the player
        new_guess = getGuess(guessedLetters)

        #if that guess is in the word
        if new_guess in word:
            print(f"{new_guess} is correct!")
            print()
        #if that guess is not in the word add 1 to the incorrect guesses tracker
        else:
            print(f"{new_guess} was incorrect.")
            print()
            incorrect_guesses += 1
        
        #update the display with the new guess
        display = blanks(word, guessedLetters)

    #when the game exits the while loop if the gameWon conditions are true, display victory message
    if gameWon(display):
        print(f"Word: {display}")
        print(f"Congratulations! You won!")
    #if the gameWon conditions are not true, then the player ran out of guesses. Game over message
    else:
        print("Game over! You ran out of guesses.")
        print(f"The secret word was: {word}.")
        
if __name__ == "__main__":
    playGame()