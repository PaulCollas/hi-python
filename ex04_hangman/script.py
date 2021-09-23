import random


# ALL DRAW FOR MISSES
hang = ["""
H A N G M A N - Biggest French cities Edition

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Biggest French cities Edition

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Biggest French cities Edition

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Biggest French cities Edition

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Biggest French cities Edition

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Biggest French cities Edition

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Biggest French cities Edition

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():

    # LIST OF ALL CITIES
    cities = ['paris', 'marseille', 'lyon', 'toulouse', 'nice', 'nantes', 'strasbourg', 'montpellier', 'bordeaux', 'lille', 'rennes', 'reims', 'toulon', 'grenoble', 'dijon', 'angers', 'nîmes', 'saint-Denis', 'caen']

    # CHOICE OF ONE CITY
    city = random.choice(cities)
    return city


def displayBoard(hang, missedLetters, correctLetters, secretCity):

    # PUT FIRST DRAW 
    print(hang[len(missedLetters)])
    print()

    # PUT THE SPACE WHERE MISSED LETTERS
    print('Lettres déjà dites:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    # BLANKS IS TO PUT _ INDEED NAME OF THE SECRETCITY
    blanks = '_' * len(secretCity)

    # REMPLACE BANKS WITH CORRECT LETTERS
    for i in range(len(secretCity)): 
        if secretCity[i] in correctLetters:
            blanks = blanks[:i] + secretCity[i] + blanks[i+1:]

    # SHOW THE SECRETCITY INDEED BLANK
    for letter in blanks:  
        print(letter, end=' ')
    print("\n")


# CONTROL OF INPUT
def getGuess(alreadyGuessed):
    while True:
        guess = input('Donnes une lettre: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Entre une seule lettre !')
        elif guess in alreadyGuessed:
            print('Tu as déjà dis cette lettre. donnes en une autre.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Entre une lettre minuscule !')
        else:
            return guess


# SET VALUES TO '' FOR DEFAULT
missedLetters = ''
correctLetters = ''

# SET THE SECRETCITY
secretCity = getRandomWord()

gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretCity)

    guess = getGuess(missedLetters + correctLetters)

    # CONDTION WHERE USER GUESS SECRETCITY
    if guess in secretCity:
        correctLetters = correctLetters + guess

        # PUT VALUE TO FOUND ALL LETTERS
        foundAllLetters = True
        for i in range(len(secretCity)):
            if secretCity[i] not in correctLetters:
                foundAllLetters = False
                break

        # CONDITION & PRINT WHEN USER GUESS CITY
        if foundAllLetters:
            print('\nBien joué la ville est: "' +
                  secretCity + '"! Vous avez gagné!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # CONDITION WHEN USER DON'T GUESS SECRETCITY
        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters, correctLetters, secretCity)
            print('Vous avez perdu!\nAprès ' + str(len(missedLetters)) + ' de mauvaises lettres et de ' +
                  str(len(correctLetters)) + ' bonnes lettres, la ville était "' + secretCity + '"')
            gameIsDone = True