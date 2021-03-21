class Gui:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,y):
        self.num = y

class Pool:
    def __init__(self,x,y):
        self.gui = Gui(x)
        self.fish = Fish(y)
    def print_num(self):
        print(' %d  %d '% (self.gui.num,self.fish.num))
    
    
    
