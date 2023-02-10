class Student:
    def getStudentDetails(self):
        self.name=input("Enter name Number : ")
        self.UID = input("Enter UID : ")
        self.python_marks =int(input("Enter python Marks : "))
        self.COURSE = input("Enter COURSE Marks : ")
        self.section = input("Enter section : ")
        self.group=input("Enter your group")

    def printResult(self):
        # self.percentage = (int)( (self.physics + self.chemistry + self.maths) / 300 * 100 ); 
        print(self.name,self.UID, self.python_marks,self.COURSE,self.section,self.group)

S1=Student()
S1.getStudentDetails()

print("DETAILS : ")
S1.printResult()



print("DETAILS after adding VALUE")
S1.printResult()
