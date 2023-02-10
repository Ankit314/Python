text=input("Enter the text=\n")
if("if make a loat of money" in text):
  spam = True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True    
elif("subscribe this" in text):
    spam=True
else:
    spam=False
if(spam):
    print("this text is spam")
else:
    print("This text is not spam")                