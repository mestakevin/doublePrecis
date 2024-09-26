

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
    
    def __truediv__(self, other):
        new_man = self.mantissa / other.mantissa
        new_exp = self.exponent - other.exponent
        new_sign = self.sign * other.sign
        return new_man, new_exp, new_sign

    def __add__(self, other):
        if self.exponent != other.exponent:
            diff_exp = self.exponent - other.exponent
            new_exp  = other.exponent + diff_exp
            mew_man = other.mantissa * (10** -diff_exp)
            new_man = other.sign * mew_man + self.sign * self.mantissa
            if new_man < 0:
                new_sign = -1
            else:
                new_sign = 1
            return new_man, new_exp, new_sign

        else:
            new_man = self.sign * self.mantissa + other.sign * other.mantissa
            new_exp = self.exponent
            if new_man < 0:
                new_sign = -1
            else:
                new_sign = 1
            return new_man, new_exp, new_sign    


        


def convertDouble():
    a = -1.2e10
    b = -6.0e7
    c = a * b
    d = a/b
    print("Alg")
    print("mult: ", c)
    print("div: ", d)
    
        

def main():
        num = doublePrec(1.2,10,-1)
        num2 = doublePrec(6.0, 7, -1)
        num3 = num * num2
        print("our number: ", num3)
        
        convertDouble()
   


main()
