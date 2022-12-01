import random
class osztaly():
    name=''
    tries=None
    numbers=None
    guess=None
    numberofGuesses=None
    number=None
    guessesLeft=None
    def __init__(self):
        self.name='Player'
        self.tries=5
        self.numbers=50
        self.guess=0
        self.numberofGuesses=0
        self.number = 0
    def szam(self):
        self.number = random.randint(0, self.numbers)
        return self.number
    def kitalalas(self):
            number = self.number
            while self.numberofGuesses < self.tries:

                #self.guess = int(input("Válasz egy számot"))
                self.numberofGuesses=self.numberofGuesses+1
                self.guessesLeft = self.tries - self.numberofGuesses

                if self.guess < number:
                    guessesLeft = str(self.guessesLeft)
                    print("Probálkozott szám alacsony! Neked " + guessesLeft + " probálkozásod van")
                    return self.guessesLeft

                elif self.guess > number:
                    guessesLeft = str(self.guessesLeft)
                    print("Probálkozott szám magas! Nekd " + guessesLeft + " probálkozásod van")
                    return self.guessesLeft

            if self.guess == number:
                numberofGuesses = str(self.numberofGuesses)
                print('Kitaláltad '+numberofGuesses+' probálkozás alatt')
                return numberofGuesses

            if self.guess != number:
                number = str(number)
                print('A helyes szám '+number+' volt.')
                return number
if __name__=="__main__":
    gs=osztaly()
    gs.szam()
    print(gs.kitalalas())