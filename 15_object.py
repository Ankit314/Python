class preson:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student:
    pass        
x=preson("Ankit","Kumar")
x.printname()

