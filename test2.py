from test import test

class test2:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.txt = test(id,score)
        self.txt.prints(self.id,self.score)



