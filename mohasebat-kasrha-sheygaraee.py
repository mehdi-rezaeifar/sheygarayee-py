class Fraction:
    def __init__(self,a1,a2):
        self.sorat = a1
        self.sorat = a2
        

    def add(self,b):
        k1=(self.makhraj * b.makhraj)
        k2=(self.sorat * b.makhraj)
        k3=(b.sorat * self.makhraj)
        print = (k2 + k3 / k1)

    def sub(self,b):
        k1=(self.makhraj * b.makhraj)
        k2=(self.sorat1 * b.makhraj)
        k3=(b.sorat * self.makhraj)
        print = (k2 - k3 / k1)

    def multiply(self,b):
        k1=(self.sorat * b.sorat)
        k2=(self.makhraj * b.makhraj)
        print = (k1 / k2) 

    def div(self,b):
        k1=(self.sorat * b.makhraj)
        k2=(self.makhraj * b.sorat)
        print = (k1 / k2) 

a1 = Fraction(2,3)
a2 = Fraction(3,3)

a1.show()
a2.show()

output  = a1.add(a2)
output.show()

output2 = a1.sub(a2)
output2.show()

output3 = a1.multiply(a2)
output3.show()

output4 = a1.div(a2)
output4.show()