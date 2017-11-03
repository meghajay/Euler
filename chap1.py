

class Fraction():
    def __init__(self,top,bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, otherfract):
        newDen = self.denominator * otherfract.denominator
        newNumera = self.denominator * otherfract.numerator + otherfract.denominator * self.numerator
        val =  newNumera/newDen
        return Fraction(newNumera,newDen)


if __name__ == "__main__":
    f1 = Fraction(1,4)
    f2 = Fraction(2,6)
    f3 = f1+f2
    print f3
