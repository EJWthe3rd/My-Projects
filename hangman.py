import random

words = ['Elephant', 'Pizza', 'Sunshine', 'Guitar', 'Butterfly', 'Chocolate', 'Computer', 'Rainbow', 'Library',
         'Adventure', 'Ocean', 'Moonlight', 'Football', 'Banana', 'Happiness', 'Puzzle', 'Mountain', 'Fireworks',
         'Lemonade', 'Carousel']

incorrectGuesses = 0
lettersGuessed = []

randomNumber = random.randint(0, 19)
trueWord = words[randomNumber].lower()
trueWordLength = len(trueWord)

blankWord = "_" * trueWordLength

while True:
    print("Your word is %s." % blankWord)

    userGuess = input("Enter a letter: ").lower()

    while not userGuess.isalpha() or len(userGuess) != 1:
        print("Please only enter a single letter.")
        userGuess = input("Enter a letter: ").lower()

    if userGuess in lettersGuessed:
        print("You have already guessed that letter. Try again.")
        continue

    lettersGuessed.append(userGuess)

    if userGuess in trueWord:
        print("You guessed correctly!")
        updatedBlankWord = ""
        for i in range(trueWordLength):
            if trueWord[i] == userGuess:
                updatedBlankWord += userGuess
            else:
                updatedBlankWord += blankWord[i]
        blankWord = updatedBlankWord

        if blankWord == trueWord:
            print("Congratulations! You guessed the word correctly. You win!")
            break
    else:
        incorrectGuesses += 1
        print("Your guess is incorrect. You have guessed incorrectly %d times." % incorrectGuesses)

        if incorrectGuesses == 7:
            print("You have guessed incorrectly 7 times. You lose!")
            break
