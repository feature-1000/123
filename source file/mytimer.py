import time as t

class Mytime():
    def __init__(self):
        self.unit = [' years',' months',' day',' hour',' minutes','  second']
        self.prompt = 'Unstart timing !'
        self.lasted = []
        self.begin = 0
        self.end = 0

    
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    

    
    def start(self):
        self.begin = t.localtime()
        print('Time starts ')

    def stop(self):
        self.end = t.localtime()
        self._calc()
        print('End of timing ')

    def _calc(self):
        self.lasted = []
        self.prompt = 'all pass '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            
            if self.lasted[index]:               
                self.prompt += (str(self.lasted[index])+self.unit[index])

   
             
