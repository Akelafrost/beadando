import random
class osztaly():
    name=''
    tries=None
    numbers=None

    def __init__(self):
        self.name='Player'
        self.tries=5
        self.numbers=50

    def kitalalas(self):
            number = random.randint(0,self.numbers)
            numberofGuesses=0
            while numberofGuesses < self.tries:
                guess = int(input("Take a guess"))
                numberofGuesses=numberofGuesses+1
                guessesLeft = self.tries - numberofGuesses

                if guess < number:
                    guessesLeft = str(guessesLeft)
                    print("Your guess is too low! You have " + guessesLeft + " guesses left")

                if guess > number:
                    guessesLeft = str(guessesLeft)
                    print("Your guess is too high! You have " + guessesLeft + " guesses left")

                if guess == number:
                    break

            if guess == number:
                numberofGuesses = str(numberofGuesses)
                print("Good job "+self.name+"! You guessed the number in " + numberofGuesses + " tries :)")

            if guess != number:
                number = str(number)
                print("Sorry. The number I was thinking of was " + number + " :)")

gs=osztaly()
gs.kitalalas()