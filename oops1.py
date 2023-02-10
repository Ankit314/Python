class B:
    marks=90
    def fun(self):
        "Document....."
        name="Ankit...."
        print(name)
obj= B()
obj.fun()
print(obj.fun.__doc__)
print(obj.marks)
print(B.marks)
