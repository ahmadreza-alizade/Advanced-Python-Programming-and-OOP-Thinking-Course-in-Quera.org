
class Reverse:
    def __init__(self, ls):
        self.ls = ls
        
    def __iter__(self):
        return(reversed(self.ls))
    
    def __next__(self):
        return(next(self.ls))

myls = Reverse([1, 2, 3, 4, 5, 6, 7])

for item in myls:
    print(item)
