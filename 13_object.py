class person:
    def __init__(self,name,age) :

        self.name=name
        self.age=age
    def myfunc(self):
     print("Persons age :"+self.age)
p1=person("johan",38)
p1.age=49
print(p1.age)

