import random

board = ["""
H A N G M A N - Fruit Edition

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

def getRandomWord():

    ## ALL WORDS
    words = ['paris', 'marseille', 'lyon', 'toulouse', 'nice', 'nantes', 'strasbourg', 'montpellier', 'bordeaux', 'lille', 'rennes', 'reims', 'toulon', 'grenoble', 'dijon', 'angers', 'nîmes', 'saint-Denis', 'caen']

    word = random.choice(words)
    return word

def displayBoard(board, missedLetters, correctLetters, secretWord):
    print(board[len(missedLetters)])
    print()
    
    print('Missed Letters: ', end='')

    for letter in missedLetters:
        print(letter, end='')
        print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end='')
    print("\n")

def getGuess(alreadyGuessed):
    while True:
        guess = input('Trouve une lettre: ')
        guess = guess.lower()

        ## TEST & VERIFICATION
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Choose a min letter')
        else: 
            return guess
        
def playAgain():
    return input("\n Do you want to play again? ").lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False


while True:
    displayBoard(board, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
            break
        if foundAllLetters:
            print('\n Yes! The secret word is "' + secretWord + '! You have won!')
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(board) - 1:
                displayBoard(board, missedLetters, correctLetters, secretWord)
                print('You have run of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                
                gameIsDone = True
        
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord()
            else:
                break
        
    