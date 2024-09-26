

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
        return doublePrec(new_man, new_exp, new_sign)
    
    def __truediv__(self, other):
        new_man = self.mantissa / other.mantissa
        new_exp = self.exponent - other.exponent
        new_sign = self.sign * other.sign
        return doublePrec(new_man, new_exp, new_sign)

    def __add__(self, other):
            # Align exponents
            if self.exponent > other.exponent:
                diff_exp = self.exponent - other.exponent
                adjusted_other_man = other.mantissa * (10 ** diff_exp)
                new_man = self.sign * self.mantissa + other.sign * adjusted_other_man
                new_exp = self.exponent
            else:
                diff_exp = other.exponent - self.exponent
                adjusted_self_man = self.mantissa * (10 ** diff_exp)
                new_man = self.sign * adjusted_self_man + other.sign * other.mantissa
                new_exp = other.exponent
    
            new_sign = -1 if new_man < 0 else 1
            return doublePrec(abs(new_man), new_exp, new_sign)

    def __str__(self):
        # Display number in scientific notation
        return f"{self.sign * self.mantissa}e{self.exponent}"    


def convertDouble():
    a = -1.2e10
    b = -6.0e7
    c = a * b
    d = a/b
    print("Standard Python:")
    print("Mult:", c)
    print("Div:", d)
    
        

def main():
        num = doublePrec(1.2,10,-1)
        num2 = doublePrec(6.0, 7, -1)
        num3 = num * num2
        print("Our number (custom class):", num3)
        
        convertDouble()
   


main()
