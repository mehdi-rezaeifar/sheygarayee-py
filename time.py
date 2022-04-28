class Time:
    def __init__(self,h,m,s):
        self.hours = h
        self.min = m
        self.sec = s

    def show(self):
        print(self.hours, ":" ,self.min, ":" , self.sec)

    def add(self,B):
        result = Time(0 ,0 ,0)
        result.hours = self.hours + B.hours
        result.min = self.min + B.min
        result.sec = self.sec + B.sec
        return result

    def sub(self,B):
        result = Time(0 ,0 ,0)
        result.hours = self.hours - B.hours
        result.min = self.min - B.min
        result.sec = self.sec - B.sec
        return result

    def fix(self):
        if self.sec >= 60 :
            self.sec -= 60
            self.min += 1

        if self.min >= 60 :
            self.min -= 60
            self.hours += 1

        if self.sec < 0:
            self.min -= 1
            self.sec +=60

        if self.min < 0:
            self.hours -= 1
            self.min += 60

        
t1 = Time(2,30,30)
t2 = Time(3,45,12)

t1.show()
t2.show()

output  = t1.add(t2)
output.fix()
output.show()

output2 = t1.sub(t2)
output2.fix()
output2.show()

