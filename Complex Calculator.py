class Complex:
    def __init__(self, r,i):
        self.real = r
        self.imaginary = i
# Calculating Addition of Complex Number    
    def __add__(self,c):
        return (f"Addition of {self.real}+{self.imaginary}i and {c.real}+{c.imaginary}i = {self.real + c.real}+{self.imaginary+c.imaginary}i")
    
# Calulating Subtraction of Complex Number    
    def __sub__(self,c):
        return (f"Subtraction of {self.real}+{self.imaginary}i and {c.real}+{c.imaginary}i = {self.real - c.real}+{self.imaginary-c.imaginary}i")
    
#  Calulating Multiplication of Complex Number      
    def __mul__(self,c):
        return (f"Multiplication of {self.real}+{self.imaginary}i and {c.real}+{c.imaginary}i = {(self.real*c.real)-(self.imaginary*c.imaginary)}+{self.real*c.imaginary+self.imaginary*c.real}i")

# Calculating Division of Complex Number    
    def __truediv__(self,c):
        return (f"Division of {self.real}+{self.imaginary}i and {c.real}+{c.imaginary}i = {(self.real*c.real+self.imaginary*c.imaginary)}/{(c.real**2+c.imaginary**2)}+{self.imaginary*c.real-self.real*c.imaginary}/{c.real**2+c.imaginary**2}i")

# Instructing User To Input Complex Number

c1,c2=eval(input("Enter First Complex Number's RealPart, ImaginaryPart = "))
c3,c4=eval(input("Enter Second Complex Number's RealPart,ImaginaryPart = "))
c5=Complex(c1,c2)
c6=Complex(c3,c4)
print(c5 + c6)
print(c5 - c6)
print(c5 * c6)
print(c5 / c6)
