x=int(input("Enter your num1:"))
y=int(input("Enter your num2:"))
z=int(input("Enter your num3:"))
if x>y:
    if x>z:
        largest=x
    else:
        largest=z
else:
    if x>z:
        largest=x
    else:
        largest=z
print("Largest number:",largest)            
