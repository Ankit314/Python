dict={
'name': str(input("Enter your name :")),
'course': str(input("Enter your course:")),
'age':int(input("Enter your age :")),
'uid':int(input("Enter your uid :")),
'addres':str(input("Enter your addres"))

}
user={
    "Name":'name',
    "Course":'course',
    "Age":'age',
    "UID":'uid',
    "Addres":'addres'



}
print(user.get(dict))
