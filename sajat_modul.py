import random
class osztaly():
    name=''
    tries=None
    numbers=None
    guess=None
    def __init__(self):
        self.name='Player'
        self.tries=5
        self.numbers=50

    def kitalalas(self):
            number = random.randint(0,self.numbers)
            numberofGuesses=0
            while numberofGuesses < self.tries:
                self.guess = int(input("Take a guess"))
                numberofGuesses=numberofGuesses+1
                guessesLeft = self.tries - numberofGuesses

                if self.guess < number:
                    guessesLeft = str(guessesLeft)
                    print("Your guess is too low! You have " + guessesLeft + " guesses left")

                if self.guess > number:
                    guessesLeft = str(guessesLeft)
                    print("Your guess is too high! You have " + guessesLeft + " guesses left")

            if self.guess == number:
                numberofGuesses = str(numberofGuesses)
                return numberofGuesses

            if self.guess != number:
                number = str(number)
                return number
if __name__=="__main__":
    gs=osztaly()
    print(gs.kitalalas())