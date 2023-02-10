from webbrowser import get


dict = {
     "fan":"pankha",
     "dog":"kuta",
     "mobile":"fan",
     "watch":"ghadi"

 }
print("option are my dictionary=\n",dict.keys())
a = input("enter number\n")
print(a)
print("The meaning of english word=\n",dict)
print("my dictionary=\n",dict.get(a))