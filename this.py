def remove(string , word):
    newstr= string.replace(word,"")
    return newstr.strip()


this = "    this ankit    "
n=remove(this,"this")
print(n)
# print(this)
# print(this.strip())
