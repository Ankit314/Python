n1=int(input("Enter 1st sub marks"))
n2=int(input("Enter 2nd sub marks"))
n3=int(input("Enter 3rd sub marks"))
n4=int(input("Enter 4th sub marks"))
if(n1<33 or n2<33 or n3<33 or n4<33):
    print("You are fail in one subject")
elif(n1+n2+n3+n4)/4 <160:
    print("YOU are Fail")
 
else:
    print("Congratulation! you  pass this exam")
