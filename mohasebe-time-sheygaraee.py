class Time:
    def __init__(self, h1, m1, s1, h2, m2, s2):
        self.second1 = s1
        self.minute1 = m1
        self.hour1 = h1
        
        self.second2 = s2
        self.minute2 = m2
        self.hour2 = h2
        
    
    def add(self):
        if(self.minute1 <= 60 and self.minute2 <= 60 and self.second1 <= 60 and self.second2 <= 60):
            
                hours = (self.hour1 + self.hour2)
                min = (self.minute1 + self.minute2)
                sec = (self.second1 + self.second2)
                if(min > 60 ):
                    hours = +1
                    print("Time: ",hours,":",min,":",sec)
                elif(sec > 60) :  
                   min = +1
                   print("Time: ",hours,":",min,":",sec)

    def sub(self):
        if(self.minute1 <= 60 and self.minute2 <= 60 and self.second1 <= 60 and self.second2 <= 60):
            
                hours = (self.hour1 - self.hour2)
                min = (self.minute1 - self.minute2)
                sec = (self.second1 - self.second2)
                if(min > 60 ):
                    hours = +1
                    print("Time is: ",hours,":",min,":",sec)
                elif(sec > 60) :  
                   min = +1
                   print("Time is: ",hours,":",min,":",sec)
    
   

sample = Time(2,30,20,1,30,20)
sample.add()
sample.sub()
