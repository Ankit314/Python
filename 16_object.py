class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def myfunc(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
x=student("Ankit","Kumar")
x.myfunc()        
                    
        