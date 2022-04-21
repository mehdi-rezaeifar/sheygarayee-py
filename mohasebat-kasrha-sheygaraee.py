class Fraction:
    def __init__(self,a1,b1,a2,b2) :
        self.sorat1 = a1
        self.sorat2 = a2
        self.makhraj1 = b2
        self.makhraj2 = b2

    def add(self):
        k1=(self.makhraj1 * self.makhraj2)
        k2=(self.sorat1 * self.makhraj2)
        k3=(self.sorat2 * self.makhraj1)
        print=(k2 + k3 / k1)

    def sub(self)  :
        k1=(self.makhraj1 * self.makhraj2)
        k2=(self.sorat1 * self.makhraj2)
        k3=(self.sorat2 * self.makhraj1)
        print=(k2 - k3 / k1)

    def multiply(self)  :
        k1=(self.sorat1 * self.sorat2)
        k2=(self.makhraj1 * self.makhraj2)
        print=(k1 / k2) 

    def div(self)  :
        k1=(self.sorat1 * self.makhraj2)
        k2=(self.makhraj1 * self.sorat2)
        print=(k1 / k2) 

test=Fraction(3,2,2,3)
test.add()
test.sub()
test.multiply()
test.div()