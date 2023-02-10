class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my Name is  :"+self.name )
p1=person("Johan",36)
p1.myfunc()


    