

class doublePrec():

    def __init__(self, mantissa, exponent, sign):
        self.mantissa = mantissa
        self.exponent = exponent
        self.sign = sign


    def getMantissa(self):
        return self.mantissa

    
    def getExponent(self):
        return self.exponent


    def getSign(self):
        return self.sign

    def __mul__(self, other):
        new_man = self.mantissa * other.mantissa
        new_exp = self.exponent + other.exponent
        new_sign = self.sign * other.sign
        return new_man, new_exp, new_sign

def convertDouble(num):
    a = 0.1
    b = 0.2
    c = a * b
    d = a/b
    print(c)
    print(d)
    
        

def main():
        num = doublePrec(1.2,10,-1)
        num2 = doublePrec(6.0, 0.1, -1)
        print
   


main()
